#!/usr/bin/env python3
"""Validate P0/P1 schemas and generate one treatment-plan contract fixture."""

from __future__ import annotations

import json
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:
    raise SystemExit("Install the dev extra or jsonschema>=4.23 to run schema validation.") from exc

from mix_analyzer.decision import prescribe  # noqa: E402


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(instance: dict, schema: dict, label: str) -> list[str]:
    validator = Draft202012Validator(schema)
    return [f"{label}: {'/'.join(str(x) for x in error.path)}: {error.message}" for error in validator.iter_errors(instance)]


def main() -> int:
    errors: list[str] = []
    knowledge = ROOT / "skills" / "prescribe-mix-actions" / "knowledge"
    p0 = load(knowledge / "p0" / "decision-cards.json")
    errors += validate(p0, load(ROOT / "schemas" / "p0-decision-card.schema.json"), "p0")
    adapter_schema = load(knowledge / "p1" / "schema" / "adapter.schema.json")
    for path in sorted((knowledge / "p1" / "profiles").glob("*.json")):
        errors += validate(load(path), adapter_schema, path.name)
    supplemental_manifest = load(knowledge / "p1" / "supplemental" / "manifest.json")
    supplemental_schema = load(ROOT / "schemas" / "p1-supplemental-profile.schema.json")
    for entry in supplemental_manifest.get("entries", []):
        path = knowledge / entry["profile"]
        profile = load(path)
        errors += validate(profile, supplemental_schema, path.name)
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append(f"{path.name}: supplemental profile hash mismatch")
        packaged = profile.get("evidence", {}).get("packaged", {})
        for evidence_entry in [packaged.get("card"), packaged.get("source_note")]:
            if not evidence_entry:
                continue
            evidence_path = knowledge / evidence_entry["packaged_path"]
            if not evidence_path.is_file():
                errors.append(f"{path.name}: missing supplemental evidence {evidence_path}")
            elif hashlib.sha256(evidence_path.read_bytes()).hexdigest() != evidence_entry["sha256"]:
                errors.append(f"{path.name}: supplemental evidence hash mismatch {evidence_path.name}")
    diagnosis = {
        "schema_version": "1.0", "analysis_mode": "manual", "context": {},
        "findings": [{
            "diagnosis_id": "parallel_distortion", "direction": "missing",
            "severity": 0.7, "confidence": 0.7, "scope": "lead-vocal",
            "calibration_required": True,
            "evidence": [{"listening_confirmation": "grain missing"}],
        }],
    }
    errors += validate(diagnosis, load(ROOT / "schemas" / "diagnosis-evidence.schema.json"), "diagnosis")
    plan = prescribe(diagnosis, knowledge)
    errors += validate(plan, load(ROOT / "schemas" / "treatment-plan.schema.json"), "plan")
    if errors:
        print("\n".join(errors))
        return 1
    print(json.dumps({
        "status": "passed", "p0_cards": len(p0["cards"]),
        "p1_profiles": len(list((knowledge / "p1" / "profiles").glob("*.json"))),
        "p1_supplemental_profiles": len(supplemental_manifest.get("entries", [])),
        "fixture_actions": len(plan["actions"]),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
