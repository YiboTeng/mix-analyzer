#!/usr/bin/env python3
"""Record the exact comparator working-tree snapshot used by mix-analyzer."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def run_git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True, encoding="utf-8").strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(r"C:\Projects\mix-reference-comparator"))
    parser.add_argument("--target", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    files = []
    for path in sorted(p for p in source.rglob("*") if p.is_file() and ".git" not in p.parts):
        relative = path.relative_to(source)
        copied = target / relative
        files.append({
            "path": str(relative).replace("\\", "/"),
            "source_sha256": sha256(path),
            "copied_sha256": sha256(copied) if copied.is_file() else None,
        })
    payload = {
        "schema_version": "1.0",
        "source": str(source),
        "source_head": run_git(source, "rev-parse", "HEAD"),
        "source_status_porcelain": run_git(source, "status", "--porcelain=v1"),
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "files": files,
    }
    out = target / "docs" / "provenance" / "comparator-working-tree.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

