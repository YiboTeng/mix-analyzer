#!/usr/bin/env python3
"""Import seven P1 L2/deferred profiles without promoting them to L3."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

from import_p1_snapshot import bullet_lines, parse_controls, section


SPECS = [
    ("iZotope/RX 10 Breath Control.md", "iZotope/RX 10 Breath Control资料.md", "e4502ba6e6cb", "iZotope", "RX 10 Breath Control", "10.4.2", "restoration-breath", ["breath_too_loud", "breath_level_inconsistent"], "unavailable", ["evidence_level_l2_not_l3", "host_load_failure_0x3"]),
    ("iZotope/RX 10 De-plosive.md", "iZotope/RX 10 De-plosive资料.md", "5a5ddef31a66", "iZotope", "RX 10 De-plosive", "10.4.2", "restoration-plosive", ["plosive_low_frequency_event"], "unavailable", ["evidence_level_l2_not_l3", "host_load_failure_0x3"]),
    ("iZotope/RX 10 Mouth De-click.md", "iZotope/RX 10 Mouth De-click资料.md", "8f1bf189fac1", "iZotope", "RX 10 Mouth De-click", "10.4.2", "restoration-mouth-click", ["mouth_click_or_short_impulse"], "unavailable", ["evidence_level_l2_not_l3", "host_load_failure_0x3"]),
    ("PreSonus/Pro EQ.md", "PreSonus/Pro EQ资料.md", "e482c5d14f03", "PreSonus", "Pro EQ", "4.0.0", "eq-native-baseline", ["mud", "tonal_imbalance", "resonance"], "host-native-cache", ["evidence_level_l2_not_l3", "studio_one_runtime_unavailable"]),
    ("SoundToys/Decapitator.md", "SoundToys/Decapitator资料.md", "bc411ff14519", "SoundToys", "Decapitator", "5.0.1.0", "saturation-character", ["parallel_distortion", "vocal_density", "harmonic_density", "midrange_character"], "current-filesystem-match", ["evidence_level_l2_not_l3", "vst2_host_validation_deferred"]),
    ("SoundToys/LittleAlterBoy.md", "SoundToys/LittleAlterBoy资料.md", "3e3b26a92fe1", "SoundToys", "LittleAlterBoy", "5.0.1.0", "pitch-formant-creative", ["creative_octave_layer", "formant_character", "robotic_voice"], "current-filesystem-match", ["evidence_level_l2_not_l3", "vst2_host_validation_deferred"]),
    ("SoundToys/MicroShift.md", "SoundToys/MicroShift资料.md", "f9e0e7aeb790", "SoundToys", "MicroShift", "5.0.1.0", "width-micro-pitch", ["adlib_width", "mono_to_stereo_effect", "subtle_parallel_space"], "current-filesystem-match", ["evidence_level_l2_not_l3", "vst2_host_validation_deferred"]),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(r"C:\Projects\aizen-knowledge-base"))
    parser.add_argument("--knowledge-root", type=Path, default=Path(__file__).resolve().parents[1] / "skills" / "prescribe-mix-actions" / "knowledge")
    args = parser.parse_args()
    out = args.knowledge_root / "p1" / "supplemental"
    evidence_root = args.knowledge_root / "p1" / "evidence" / "supplemental"
    entries = []
    for card_rel, source_rel, family, vendor, product, version, primary, diagnoses, availability, warnings in SPECS:
        card = args.source_root / "notes" / "音乐制作" / "插件" / Path(card_rel)
        source = args.source_root / "sources" / "音乐制作" / "插件资料" / Path(source_rel)
        if not card.is_file() or not source.is_file():
            raise FileNotFoundError(f"Missing supplemental source: {card} or {source}")
        card_target = evidence_root / "cards" / card.name
        source_target = evidence_root / "sources" / source.name
        card_target.parent.mkdir(parents=True, exist_ok=True)
        source_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(card, card_target)
        shutil.copy2(source, source_target)
        text = card.read_text(encoding="utf-8")
        profile = {
            "schema_version": "1.0",
            "adapter_id": f"l2-{family}--{slug(product)}",
            "family_id": family,
            "identity": {"vendor": vendor, "product": product, "version_range": version, "formats": ["VST2"], "availability": availability, "tested_host": "deferred / not L3"},
            "capabilities": {"primary": primary, "secondary": [], "diagnoses": diagnoses, "not_for": []},
            "routing": [{"position": item, "when": diagnoses[0]} for item in bullet_lines(section(text, "路由"))] or [{"position": "follow card routing", "when": diagnoses[0]}],
            "parameter_strategy": {"targets": bullet_lines(section(text, "调整目标")) or ["smallest effective change"], "controls": [{"name": item["name"], "action": item["action"]} for item in parse_controls(section(text, "控制语义"))], "no_universal_values": True},
            "input_requirements": ["explicitly accept L2/deferred evidence", "level-matched comparison"],
            "risks": bullet_lines(section(text, "常见失败")) or ["unvalidated host behavior"],
            "stop_conditions": bullet_lines(section(text, "何时停止")) or ["audible side effects exceed benefit"],
            "alternatives": [],
            "version_policy": {"match": "L2 control knowledge only; no L3 host guarantee.", "mismatch": "Suppress exact controls and require revalidation."},
            "evidence": {"level": "L2", "card": str(card), "source_note": str(source), "validation_report": "not-L3", "result_files": [], "packaged": {"card": {"packaged_path": str(card_target.relative_to(args.knowledge_root)).replace('\\','/'), "sha256": sha(card_target)}, "source_note": {"packaged_path": str(source_target.relative_to(args.knowledge_root)).replace('\\','/'), "sha256": sha(source_target)}}},
            "p0_contract": {"diagnosis_inputs": diagnoses, "outputs": ["plugin", "route", "parameter_targets", "stop_conditions", "side_effects", "retest_metrics"]},
            "conflict_rules": [{"if": "host_load_failure", "action": "reject until revalidated"}] if availability == "unavailable" else [],
            "validation": {"status": "deferred-l2", "matrix_status": "not-l3", "boundary": "Official/control research only; no successful L3 host render."},
            "catalog_warnings": warnings,
            "local_guidance": {
                "signal_position": bullet_lines(section(text, "信号流位置")), "routing": bullet_lines(section(text, "路由")),
                "controls": parse_controls(section(text, "控制语义")), "parameter_start_points": bullet_lines(section(text, "参数起点")),
                "listen_for": bullet_lines(section(text, "调整时听什么")), "stop": bullet_lines(section(text, "何时停止")),
                "latency": [section(text, "延迟、相位与过采样")] if section(text, "延迟、相位与过采样") else [],
            },
        }
        target = out / f"l2-{family}--{slug(product)}.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        entries.append({"family_id": family, "profile": str(target.relative_to(args.knowledge_root)).replace('\\','/'), "sha256": sha(target)})
    manifest = {"schema_version": "1.0", "evidence_level": "L2/deferred", "count": len(entries), "entries": entries}
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"supplemental_profiles": len(entries)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

