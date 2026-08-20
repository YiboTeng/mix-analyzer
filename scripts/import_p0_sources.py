#!/usr/bin/env python3
"""Package only the P0 source notes referenced by decision cards."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(r"C:\Projects\aizen-knowledge-base"))
    parser.add_argument(
        "--knowledge-root", type=Path,
        default=Path(__file__).resolve().parents[1] / "skills" / "prescribe-mix-actions" / "knowledge",
    )
    args = parser.parse_args()
    cards_path = args.knowledge_root / "p0" / "decision-cards.json"
    payload = json.loads(cards_path.read_text(encoding="utf-8"))
    relative_paths = sorted({
        item for card in payload["cards"] for item in card.get("provenance", {}).get("source_paths", [])
    })
    output = args.knowledge_root / "p0" / "evidence"
    entries = []
    missing = []
    for relative in relative_paths:
        source = args.source_root / Path(relative)
        if not source.is_file():
            missing.append(relative)
            continue
        target = output / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        entries.append({
            "source_path": relative.replace("\\", "/"),
            "packaged_path": str(target.relative_to(args.knowledge_root)).replace("\\", "/"),
            "sha256": sha256(target),
        })
    manifest = {
        "schema_version": "1.0",
        "source_root": str(args.source_root.resolve()),
        "referenced_count": len(relative_paths),
        "packaged_count": len(entries),
        "missing": missing,
        "entries": entries,
    }
    manifest_path = args.knowledge_root / "p0" / "source-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"packaged": len(entries), "missing": len(missing)}, ensure_ascii=False))
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

