#!/usr/bin/env python3
"""Import the compact, deployable P1 runtime snapshot from Aizen Knowledge Base.

The importer deliberately excludes WAV/ALS/render directories. It copies the 40 L3
adapters, their human-readable cards, source notes, validation summaries and small
result JSON files, rewrites evidence pointers, and records SHA-256 provenance.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def section(markdown: str, heading: str) -> str:
    match = re.search(
        rf"(?ms)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)", markdown
    )
    return match.group(1).strip() if match else ""


def bullet_lines(text: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"(?m)^-\s+(.+)$", text)]


def parse_controls(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 3 or cells[0] in {"控制", "---"} or set(cells[0]) == {"-"}:
            continue
        rows.append({"name": cells[0], "meaning": cells[1], "action": cells[2]})
    return rows


def copy_evidence(source_root: Path, output_root: Path, relative: str, category: str) -> dict[str, str]:
    source = source_root / Path(relative)
    if not source.is_file():
        raise FileNotFoundError(f"P1 evidence missing: {source}")
    target = output_root / "evidence" / category / source.name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return {
        "source_path": relative.replace("\\", "/"),
        "packaged_path": str(target.relative_to(output_root)).replace("\\", "/"),
        "sha256": sha256(target),
    }


def load_inventory(inventory_csv: Path) -> dict[str, dict[str, str]]:
    with inventory_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["family_id"]: row for row in csv.DictReader(handle)}


def import_snapshot(source_root: Path, output_root: Path) -> dict[str, Any]:
    p1 = source_root / "projects" / "p1-plugin-knowledge-base"
    adapters = p1 / "adapters"
    profiles_dir = output_root / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    provenance: list[dict[str, Any]] = []
    for adapter_path in sorted((adapters / "plugins").glob("*.json")):
        adapter = read_json(adapter_path)
        evidence = adapter["evidence"]
        card_meta = copy_evidence(source_root, output_root, evidence["card"], "cards")
        source_meta = copy_evidence(source_root, output_root, evidence["source_note"], "sources")
        report_meta = copy_evidence(source_root, output_root, evidence["validation_report"], "validation")
        result_meta = [copy_evidence(source_root, output_root, item, "results") for item in evidence["result_files"]]
        card_path = output_root / card_meta["packaged_path"]
        card_text = card_path.read_text(encoding="utf-8")
        latency_section = section(card_text, "延迟、相位与过采样")
        profile = {
            **adapter,
            "local_guidance": {
                "signal_position": bullet_lines(section(card_text, "信号流位置")),
                "routing": bullet_lines(section(card_text, "路由")),
                "controls": parse_controls(section(card_text, "控制语义")),
                "parameter_start_points": bullet_lines(section(card_text, "参数起点")),
                "listen_for": bullet_lines(section(card_text, "调整时听什么")),
                "stop": bullet_lines(section(card_text, "何时停止")),
                "latency": [latency_section] if latency_section else [],
            },
            "evidence": {
                **evidence,
                "source_root": str(source_root),
                "packaged": {
                    "card": card_meta,
                    "source_note": source_meta,
                    "validation_report": report_meta,
                    "result_files": result_meta,
                },
            },
        }
        target = profiles_dir / adapter_path.name
        write_json(target, profile)
        provenance.append({
            "adapter_id": adapter["adapter_id"],
            "profile": str(target.relative_to(output_root)).replace("\\", "/"),
            "profile_sha256": sha256(target),
            "source_adapter": str(adapter_path.relative_to(source_root)).replace("\\", "/"),
            "source_adapter_sha256": sha256(adapter_path),
        })

    for folder in ("schema", "indexes", "fixtures", "snapshots"):
        source_dir = adapters / folder
        target_dir = output_root / folder
        target_dir.mkdir(parents=True, exist_ok=True)
        for source in source_dir.glob("*.json"):
            shutil.copy2(source, target_dir / source.name)

    final_audit = read_json(p1 / "audit" / "results" / "final-audit.json")
    state = read_json(p1 / "state.json")
    manifest = {
        "schema_version": "1.0",
        "snapshot_name": "aizen-p1-v1-runtime",
        "source_root": str(source_root),
        "source_state": {
            "overall_status": state.get("overall_status"),
            "last_verified_at": state.get("last_verified_at"),
            "current_checkpoint": state.get("current_checkpoint"),
        },
        "source_audit": {
            "status": final_audit.get("status"),
            "failure_count": final_audit.get("failure_count"),
            "sha256": sha256(p1 / "audit" / "results" / "final-audit.json"),
        },
        "profile_count": len(provenance),
        "excluded": ["validation/renders", "validation/projects", "validation/fixtures audio", "DAW project files"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "profiles": provenance,
    }
    write_json(output_root / "runtime-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(r"C:\Projects\aizen-knowledge-base"))
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "skills" / "prescribe-mix-actions" / "knowledge" / "p1",
    )
    args = parser.parse_args()
    manifest = import_snapshot(args.source_root.resolve(), args.output_root.resolve())
    print(json.dumps({"profile_count": manifest["profile_count"], "output": str(args.output_root)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
