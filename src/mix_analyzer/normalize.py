from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from statistics import median
from typing import Any

from .constants import ANALYZER_VERSION, CONFIDENCE_SCORES, DIAGNOSIS_SCHEMA_VERSION, PLUGIN_ID
from .io import read_json


VOCAL_FEATURE_MAP: dict[str, dict[str, str]] = {
    "integrated_lufs": {"high": "loudness_bias_check", "low": "loudness_bias_check"},
    "rms_dbfs": {"high": "loudness_bias_check", "low": "loudness_bias_check"},
    "crest_factor_db": {"high": "fast_peak_control", "low": "overcompressed_vocal"},
    "active_range_db": {"high": "macro_level_inconsistency", "low": "overcompressed_vocal"},
    "presence_db": {"high": "harshness", "low": "presence_dullness"},
    "air_db": {"high": "sibilance", "low": "lack_of_air"},
    "low_mid_masking_db": {"high": "mud", "low": "vocal_weight_deficit"},
    "macro_range_db": {"high": "macro_level_inconsistency", "low": "overcompressed_vocal"},
    "micro_range_db": {"high": "fast_peak_control", "low": "overcompressed_vocal"},
    "upper_harmonic_share": {"high": "harsh_consonants", "low": "harmonic_density"},
    "harmonic_concentration": {"high": "harshness", "low": "harmonic_density"},
    "spectral_flatness": {"high": "broadband_stationary_noise"},
    "side_mid_db": {"high": "vocal_width_excess", "low": "vocal_width_deficit"},
    "lr_correlation": {"low": "mono_translation_risk"},
    "width_tails_db": {"high": "vocal_width_excess", "low": "vocal_depth"},
    "width_core_db": {"high": "vocal_width_excess", "low": "vocal_width_deficit"},
}

MIX_FEATURE_MAP: dict[str, dict[str, str]] = {
    "LUFS-I": {"high": "loudness_bias_check", "low": "loudness_bias_check"},
    "PLR": {"high": "master_peak_excess", "low": "master_overlimited"},
    "Sub": {"high": "master_low_end_excess", "low": "master_low_end_deficit"},
    "Presence": {"high": "master_presence_excess", "low": "master_presence_deficit"},
    "High Side": {"high": "master_high_side_excess", "low": "master_high_side_deficit"},
    # Mono fold loss 通常是负值：数值更低/更负才代表折叠损失更大。
    "Mono Loss": {"low": "mono_translation_risk"},
}

MIX_SINGLE_REFERENCE_FLOORS: dict[str, float] = {
    "LUFS-I": 1.0,
    "PLR": 1.0,
    "Sub": 1.5,
    "Presence": 1.0,
    "High Side": 1.5,
    "Mono Loss": 0.5,
}


def _confidence(value: Any) -> float:
    if isinstance(value, (int, float)):
        return max(0.0, min(float(value), 1.0))
    return CONFIDENCE_SCORES.get(str(value), 0.5)


def _finding(
    diagnosis_id: str,
    *,
    direction: str,
    severity: float,
    confidence: float,
    scope: str,
    evidence: list[dict[str, Any]],
    calibration_required: bool = True,
) -> dict[str, Any]:
    return {
        "diagnosis_id": diagnosis_id,
        "direction": direction,
        "severity": round(max(0.0, min(severity, 1.0)), 4),
        "confidence": round(max(0.0, min(confidence, 1.0)), 4),
        "scope": scope,
        "calibration_required": calibration_required,
        "evidence": evidence,
    }


def normalize_vocal(payload: dict[str, Any], source_path: str | None = None) -> dict[str, Any]:
    gate = _reference_gate(payload, "vocal-reference")
    findings: list[dict[str, Any]] = []
    for key, summary in payload.get("features", {}).items():
        mapping = VOCAL_FEATURE_MAP.get(key)
        if not mapping:
            continue
        delta = float(summary.get("target_minus_reference_median", 0.0))
        floor = max(float(summary.get("practical_floor", 1.0)), 1e-9)
        direction = "high" if delta > 0 else "low"
        diagnosis = mapping.get(direction)
        if not diagnosis or abs(delta) < floor:
            continue
        outside = summary.get("outside_reference_iqr") or summary.get("outside_reference_range")
        if not outside and abs(delta) < floor * 1.5:
            continue
        findings.append(_finding(
            diagnosis,
            direction=direction,
            severity=abs(delta) / (floor * 3.0),
            confidence=min(_confidence(summary.get("confidence")), gate["confidence_cap"]),
            scope="target-vocal",
            evidence=[{
                "metric": key,
                "target": summary.get("target"),
                "reference_median": summary.get("reference_median"),
                "delta": delta,
                "unit": summary.get("unit"),
                "threshold_basis": "legacy practical_floor; requires corpus calibration",
            }],
        ))
    findings.extend(_gate_finding(gate))
    return _canonical(payload, "vocal-reference", findings, source_path, gate)


def normalize_mix(payload: dict[str, Any], source_path: str | None = None) -> dict[str, Any]:
    gate = _reference_gate(payload, "mix-reference")
    findings: list[dict[str, Any]] = []
    for key, summary in payload.get("reference_set", {}).get("features", {}).items():
        mapping = MIX_FEATURE_MAP.get(key)
        if not mapping:
            continue
        consistency = float(summary.get("direction_consistency", 0.0))
        single_reference = gate["reference_count"] == 1
        if single_reference:
            target = summary.get("target")
            reference_median = summary.get("reference_median")
            delta_value = summary.get("target_minus_reference_median")
            if delta_value is None and target is not None and reference_median is not None:
                delta_value = float(target) - float(reference_median)
            if delta_value is None:
                continue
            delta = float(delta_value)
            direction = "high" if delta > 0 else "low"
            diagnosis = mapping.get(direction)
            floor = MIX_SINGLE_REFERENCE_FLOORS[key]
            if not diagnosis or abs(delta) < floor:
                continue
            severity = min(abs(delta) / (floor * 3.0), 0.65)
            evidence = {
                "metric": key,
                "target": target,
                "reference_median": reference_median,
                "delta": delta,
                "robust_deviation": None,
                "direction_consistency": consistency,
                "statistical_status": "single_reference_raw_delta_only",
                "threshold_basis": f"single-reference raw delta >= {floor:g}; conditional hypothesis only",
            }
        else:
            deviation_value = summary.get("robust_deviation")
            if deviation_value is None:
                continue
            deviation = float(deviation_value)
            direction = "high" if deviation > 0 else "low"
            diagnosis = mapping.get(direction)
            if not diagnosis or abs(deviation) < 1.0 or consistency < 0.6:
                continue
            severity = abs(deviation) / 3.0
            evidence = {
                "metric": key,
                "target": summary.get("target"),
                "reference_median": summary.get("reference_median"),
                "robust_deviation": deviation,
                "direction_consistency": consistency,
                "threshold_basis": "robust deviation >= 1; requires genre/section calibration",
            }
        findings.append(_finding(
            diagnosis,
            direction=direction,
            severity=severity,
            confidence=min(gate["confidence_cap"], 0.45 + 0.5 * consistency),
            scope="mix-master",
            evidence=[evidence],
        ))
    findings.extend(_normalize_mix_stems(payload, gate["confidence_cap"]))
    findings.extend(_gate_finding(gate))
    return _canonical(payload, "mix-reference", findings, source_path, gate)


def _reference_labels(payload: dict[str, Any], mode: str) -> list[str]:
    references = payload.get("references", [])
    if mode == "vocal-reference":
        return [str(item.get("path") or item.get("label")) for item in references if isinstance(item, dict)]
    return [str(item) for item in references]


def _reference_gate(payload: dict[str, Any], mode: str) -> dict[str, Any]:
    labels = _reference_labels(payload, mode)
    count = int(payload.get("cohort", {}).get("count") or len(labels))
    normalized = [item.casefold() for item in labels if item]
    duplicates = list(payload.get("cohort", {}).get("duplicate_reference_paths", []))
    if len(normalized) != len(set(normalized)):
        duplicates.append("duplicate reference label/path")
    compatibility = payload.get("compatibility", {})
    compatibility_scores = [
        float(item["score"]) for item in compatibility.values()
        if isinstance(item, dict) and item.get("score") is not None
    ]
    median_compatibility = float(median(compatibility_scores)) if compatibility_scores else None
    outliers = payload.get("reference_set", {}).get("outliers", {})
    severe_outliers = [label for label, score in outliers.items() if float(score) >= 3.0]
    separated_count = 0
    if mode == "vocal-reference":
        separated_count = sum(
            bool(item.get("separated")) for item in payload.get("references", []) if isinstance(item, dict)
        )
    limitations: list[str] = []
    if separated_count:
        if count and separated_count == count:
            limitations.append("all_references_source_separated")
        elif separated_count >= (count + 1) // 2:
            limitations.append("majority_references_source_separated")
        else:
            limitations.append("some_references_source_separated")
    reasons: list[str] = []
    if count < 2:
        reasons.append("fewer_than_two_independent_references")
    if duplicates:
        reasons.append("duplicate_references")
    if median_compatibility is not None and median_compatibility < 50.0:
        reasons.append("low_reference_compatibility")
    if severe_outliers and len(severe_outliers) >= max(1, count // 2):
        reasons.append("reference_cohort_outlier_risk")
    confidence_cap = 0.35 if count < 2 else 0.5 if count == 2 else 0.7 if count < 5 else 0.82
    if median_compatibility is not None:
        confidence_cap = min(confidence_cap, max(0.3, median_compatibility / 100.0))
    if duplicates or severe_outliers:
        confidence_cap = min(confidence_cap, 0.4)
    if "all_references_source_separated" in limitations or "majority_references_source_separated" in limitations:
        confidence_cap = min(confidence_cap, 0.45)
    elif limitations:
        confidence_cap = min(confidence_cap, 0.6)
    return {
        "passed": not reasons,
        "reasons": reasons,
        "reference_count": count,
        "duplicate_references": duplicates,
        "median_compatibility": median_compatibility,
        "severe_outliers": severe_outliers,
        "limitations": limitations,
        "source_separated_reference_count": separated_count,
        "confidence_cap": round(confidence_cap, 4),
    }


def _gate_finding(gate: dict[str, Any]) -> list[dict[str, Any]]:
    if gate["passed"]:
        return []
    return [_finding(
        "reference_mismatch",
        direction="uncertain",
        severity=1.0,
        confidence=max(0.3, float(gate["confidence_cap"])),
        scope="reference-set",
        calibration_required=False,
        evidence=[{"reference_gate": gate}],
    )]


def _stem_confidence(origin: str) -> float:
    return {
        "original_stems": 0.9,
        "official_stems": 0.78,
        "source_separated": 0.45,
    }.get(origin, 0.35)


def _normalize_mix_stems(payload: dict[str, Any], confidence_cap: float = 1.0) -> list[dict[str, Any]]:
    records = payload.get("records", {})
    target_label = payload.get("target")
    target = records.get(target_label, {}).get("stems") if target_label in records else None
    refs = [records.get(label, {}).get("stems") for label in payload.get("references", [])]
    refs = [item for item in refs if item]
    if not target or len(refs) < 2:
        return []
    stem_cohort_cap = 0.5 if len(refs) == 2 else 0.7 if len(refs) < 5 else 0.82
    confidence = min(
        confidence_cap, stem_cohort_cap,
        *[_stem_confidence(target.get("origin", "master_only")), *[_stem_confidence(x.get("origin", "master_only")) for x in refs]],
    )
    findings: list[dict[str, Any]] = []

    def compare(metric: str, diagnosis: str, threshold: float, direction: str = "high") -> None:
        target_value = target.get(metric)
        ref_values = [item.get(metric) for item in refs if item.get(metric) is not None]
        if target_value is None or not ref_values:
            return
        ref_median = float(median(float(x) for x in ref_values))
        delta = float(target_value) - ref_median
        active = delta > threshold if direction == "high" else delta < -threshold
        if not active:
            return
        findings.append(_finding(
            diagnosis,
            direction=direction,
            severity=abs(delta) / (threshold * 3.0),
            confidence=confidence,
            scope="vocal-instrument-relationship",
            evidence=[{
                "metric": f"stems.{metric}", "target": target_value,
                "reference_median": ref_median, "delta": delta,
                "stem_origin": target.get("origin"),
                "stem_reference_count": len(refs),
                "threshold_basis": "initial engineering threshold; requires aligned-stem calibration",
            }],
        ))

    compare("presence_mask_risk", "frequency_masking", 0.05, "high")
    compare("hat_sibilance_mask_risk", "frequency_masking", 0.05, "high")
    compare("vir_median_db", "presence_dullness", 1.5, "low")
    compare("spatial_width_gap_db", "vocal_instrument_width_gap", 1.5, "high")

    target_bass = target.get("bass") or {}
    ref_bass = [item.get("bass") for item in refs if item.get("bass")]
    if target_bass.get("side_mid_db") is not None and ref_bass:
        ref_values = sorted(float(item["side_mid_db"]) for item in ref_bass if item.get("side_mid_db") is not None)
        if ref_values:
            ref_median = float(median(ref_values))
            delta = float(target_bass["side_mid_db"]) - ref_median
            if delta > 1.0:
                findings.append(_finding(
                    "low_frequency_mono", direction="high", severity=delta / 3.0,
                    confidence=confidence, scope="bass-stem",
                    evidence=[{
                        "metric": "stems.bass.side_mid_db", "target": target_bass["side_mid_db"],
                        "reference_median": ref_median, "delta": delta,
                        "threshold_basis": "initial engineering threshold; requires aligned-stem calibration",
                    }],
                ))
    return findings


def _canonical(
    source: dict[str, Any], mode: str, findings: list[dict[str, Any]], source_path: str | None,
    gate: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": DIAGNOSIS_SCHEMA_VERSION,
        "plugin_id": PLUGIN_ID,
        "analyzer_version": ANALYZER_VERSION,
        "analysis_mode": mode,
        "source": {
            "path": source_path,
            "schema": source.get("schema"),
            "plugin_id": source.get("plugin_id"),
        },
        "context": {
            "reference_count": (gate or {}).get("reference_count", source.get("cohort", {}).get("count")
            or len(source.get("references", []))),
            "reference_gate": gate,
            **_stem_context(source, mode),
            "automatic_thresholds_calibrated": False,
        },
        "findings": _merge_findings(findings),
    }


def _stem_context(source: dict[str, Any], mode: str) -> dict[str, Any]:
    if mode != "mix-reference":
        return {"stems_available": False, "stem_source_confidence": None}
    records = source.get("records", {})
    target_stems = records.get(source.get("target"), {}).get("stems")
    reference_stems = [records.get(label, {}).get("stems") for label in source.get("references", [])]
    reference_stems = [item for item in reference_stems if item]
    if not target_stems or len(reference_stems) < 2:
        return {"stems_available": False, "stem_source_confidence": None, "stem_reference_count": len(reference_stems)}
    confidence = min(
        _stem_confidence(target_stems.get("origin", "master_only")),
        *[_stem_confidence(item.get("origin", "master_only")) for item in reference_stems],
    )
    return {"stems_available": True, "stem_source_confidence": confidence, "stem_reference_count": len(reference_stems)}


def _merge_findings(findings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str, str], dict[str, Any]] = {}
    for finding in findings:
        key = (finding["diagnosis_id"], finding["scope"], finding.get("direction", "unknown"))
        if key not in merged:
            merged[key] = finding
            continue
        current = merged[key]
        current["severity"] = max(current["severity"], finding["severity"])
        current["confidence"] = min(current["confidence"], finding["confidence"])
        current["evidence"].extend(finding["evidence"])
    return list(merged.values())


def normalize_metrics(path: str | Path) -> dict[str, Any]:
    payload = read_json(path)
    schema = payload.get("schema")
    if schema == "vocal-reference-set-v1":
        return normalize_vocal(payload, str(Path(path).resolve()))
    if schema == "mix-reference-metrics-v1":
        return normalize_mix(payload, str(Path(path).resolve()))
    if payload.get("schema_version") == DIAGNOSIS_SCHEMA_VERSION and "findings" in payload:
        _validate_canonical(payload)
        return _normalize_manual_confidence(payload) if payload.get("analysis_mode") == "manual" else payload
    raise ValueError(f"Unsupported metrics/diagnosis schema: {schema or payload.get('schema_version')}")


def _validate_canonical(payload: dict[str, Any]) -> None:
    if payload.get("analysis_mode") not in {"vocal-reference", "mix-reference", "manual"}:
        raise ValueError("Canonical diagnosis has an invalid analysis_mode")
    if not isinstance(payload.get("context"), dict) or not isinstance(payload.get("findings"), list):
        raise ValueError("Canonical diagnosis requires object context and array findings")
    if payload.get("analysis_mode") != "manual":
        gate = payload["context"].get("reference_gate")
        if not isinstance(gate, dict) or not isinstance(gate.get("passed"), bool) or not isinstance(gate.get("reasons"), list):
            raise ValueError("Reference-mode canonical diagnosis requires context.reference_gate with passed/reasons")
    for index, finding in enumerate(payload["findings"]):
        required = {"diagnosis_id", "direction", "severity", "confidence", "scope", "evidence"}
        if not isinstance(finding, dict) or not required.issubset(finding):
            raise ValueError(f"Finding {index} is missing required fields")
        if not 0.0 <= float(finding["severity"]) <= 1.0 or not 0.0 <= float(finding["confidence"]) <= 1.0:
            raise ValueError(f"Finding {index} severity/confidence must be in [0, 1]")
        if not str(finding["scope"]).strip() or not isinstance(finding["evidence"], list) or not finding["evidence"]:
            raise ValueError(f"Finding {index} requires a scope and non-empty evidence")


def _normalize_manual_confidence(payload: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(payload)
    for finding in result["findings"]:
        evidence = finding.get("evidence", [])
        kinds = {str(item.get("evidence_kind", "")) for item in evidence if isinstance(item, dict)}
        has_numeric_comparison = any(
            isinstance(item, dict) and item.get("metric") is not None
            and any(key in item for key in ("target", "reference_median", "delta", "measured_value"))
            for item in evidence
        )
        if "repeatable_measurement" in kinds or has_numeric_comparison:
            basis, cap = "repeatable_measurement", 0.8
        elif "equal_loudness_listening_confirmation" in kinds or any(
            isinstance(item, dict) and item.get("listening_confirmation") for item in evidence
        ):
            basis, cap = "equal_loudness_listening_confirmation", 0.7
        elif "user_report" in kinds:
            basis, cap = "user_report", 0.55
        else:
            basis, cap = "unclassified_manual_evidence", 0.45
        finding["confidence"] = round(min(float(finding["confidence"]), cap), 4)
        finding["confidence_basis"] = basis
        finding.setdefault("severity_basis", "user-ranked impact; not a calibrated measurement")
    return result
