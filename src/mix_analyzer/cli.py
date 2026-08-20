from __future__ import annotations

import argparse
import json
from pathlib import Path

from .decision import prescribe
from .io import default_knowledge_root, write_json
from .normalize import normalize_metrics
from .render import render_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Normalize analyzer metrics and build an evidence-driven mix treatment plan.")
    parser.add_argument("--input", required=True, type=Path, help="Legacy metrics JSON or canonical diagnosis JSON")
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--knowledge-root", type=Path, default=default_knowledge_root())
    parser.add_argument("--max-actions", type=int, default=6)
    parser.add_argument("--realtime", action="store_true")
    parser.add_argument("--latency-budget-ms", type=float)
    parser.add_argument("--context-json", type=Path, help="Runtime context JSON (inventory, versions, host, sample rate, preferences)")
    parser.add_argument("--installed-version", action="append", default=[], metavar="FAMILY_ID=VERSION")
    parser.add_argument("--available-family-id", action="append", default=[])
    parser.add_argument("--host")
    parser.add_argument("--format")
    parser.add_argument("--sample-rate-hz", type=int)
    parser.add_argument("--trust-catalog-snapshot", action="store_true", help="Use packaged P1 version mappings without a live inventory recheck")
    parser.add_argument("--require-jsonschema", action="store_true", help="Fail unless Draft 2020-12 schema validation is available and passes")
    return parser


def _validate_json_schema(instance: dict, schema_path: Path, *, required: bool) -> bool:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        if required:
            raise RuntimeError("jsonschema>=4.23 is required by --require-jsonschema")
        return False
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda item: list(item.path))
    if errors:
        detail = "; ".join(f"{'/'.join(str(x) for x in item.path)}: {item.message}" for item in errors)
        raise ValueError(f"Schema validation failed for {schema_path.name}: {detail}")
    return True


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    diagnosis = normalize_metrics(args.input)
    context = {}
    if args.context_json:
        context = json.loads(args.context_json.read_text(encoding="utf-8-sig"))
        if not isinstance(context, dict):
            raise ValueError("--context-json must contain a JSON object")
    context.update({"max_actions": args.max_actions, "realtime": args.realtime})
    installed_versions = dict(context.get("installed_versions", {}))
    for item in args.installed_version:
        if "=" not in item:
            raise ValueError("--installed-version must use FAMILY_ID=VERSION")
        family_id, version = item.split("=", 1)
        installed_versions[family_id.strip()] = version.strip()
    if installed_versions:
        context["installed_versions"] = installed_versions
    if args.available_family_id:
        context["available_family_ids"] = args.available_family_id
    if args.host:
        context["host"] = args.host
    if args.format:
        context["format"] = args.format
    if args.sample_rate_hz:
        context["sample_rate_hz"] = args.sample_rate_hz
    if args.trust_catalog_snapshot:
        context["trust_catalog_snapshot"] = True
    if args.latency_budget_ms is not None:
        context["latency_budget_ms"] = args.latency_budget_ms
    plan = prescribe(diagnosis, args.knowledge_root, context)
    project_root = Path(__file__).resolve().parents[2]
    _validate_json_schema(diagnosis, project_root / "schemas" / "diagnosis-evidence.schema.json", required=args.require_jsonschema)
    _validate_json_schema(plan, project_root / "schemas" / "treatment-plan.schema.json", required=args.require_jsonschema)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    diagnosis_path = write_json(args.out_dir / "diagnosis-evidence.json", diagnosis)
    plan_path = write_json(args.out_dir / "treatment-plan.json", plan)
    report_path = args.out_dir / "treatment-plan.md"
    report_path.write_text(render_markdown(plan), encoding="utf-8")
    print(f"diagnosis={diagnosis_path}")
    print(f"plan={plan_path}")
    print(f"report={report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
