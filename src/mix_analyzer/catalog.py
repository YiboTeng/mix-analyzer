from __future__ import annotations

from pathlib import Path
from typing import Any

from .io import read_json


# Host latency is a separate runtime property from an effect's musical delay time.
# Values below are explicit 48 kHz observations from the packaged P1 validation
# snapshot; unlisted products remain unknown instead of being guessed from prose.
RUNTIME_CONSTRAINTS: dict[str, dict[str, Any]] = {
    "497c2536aeff": {
        "latency_status": "mode-dependent-measured", "measurement_sample_rate_hz": 48000,
        "default_mode": "zero-latency", "host_latency_ms_by_mode": {"zero-latency": 0.0, "linear-phase-max": 106.7},
    },
    "7a146380912e": {
        "latency_status": "measured", "measurement_sample_rate_hz": 48000,
        "default_mode": "default", "host_latency_ms_by_mode": {"default": 42.7},
    },
    "7b4d8c94b025": {
        "latency_status": "measured", "measurement_sample_rate_hz": 48000,
        "default_mode": "default", "host_latency_ms_by_mode": {"default": 55.6},
    },
    "98d9ac6060f6": {
        "latency_status": "mode-dependent-measured", "measurement_sample_rate_hz": 48000,
        "default_mode": None,
        "host_latency_ms_by_mode": {"validated-high-quality-mode": 64.9},
    },
    "ad123c8856d3": {
        "latency_status": "measured", "measurement_sample_rate_hz": 48000,
        "default_mode": "default", "host_latency_ms_by_mode": {"default": 734.0},
    },
    "4bceae9f0a6f": {
        "latency_status": "host-latency-unknown", "effect_delay_ms_range": [0.0, 24.0],
    },
    "83165b3547f7": {
        "latency_status": "host-latency-unknown", "effect_delay_ms_is_musical_parameter": True,
    },
}


def load_profiles(knowledge_root: Path) -> list[dict[str, Any]]:
    root = knowledge_root / "p1" / "profiles"
    profiles = [read_json(path) for path in sorted(root.glob("*.json"))]
    supplemental = knowledge_root / "p1" / "supplemental"
    profiles.extend(
        read_json(path) for path in sorted(supplemental.glob("*.json"))
        if path.name != "manifest.json"
    )
    for profile in profiles:
        runtime = dict(RUNTIME_CONSTRAINTS.get(profile.get("family_id"), {}))
        tested_host = profile.get("identity", {}).get("tested_host", "")
        if "48 kHz" in tested_host:
            runtime.setdefault("tested_sample_rate_hz", 48000)
        profile["runtime_constraints"] = runtime
    return profiles


def _version_matches(installed: str | None, observed: str) -> bool:
    if not installed:
        return False
    normalized_installed = installed.strip().lower().removeprefix("v")
    alternatives = [item.strip().lower().removeprefix("v") for item in observed.split("|")]
    return normalized_installed in alternatives


def _latency_ms(profile: dict[str, Any], context: dict[str, Any]) -> float | None:
    observed = context.get("host_latency_ms", {}).get(profile.get("family_id"))
    if observed is not None:
        return float(observed)
    runtime = profile.get("runtime_constraints", {})
    modes = runtime.get("host_latency_ms_by_mode", {})
    selected = context.get("plugin_modes", {}).get(profile.get("family_id")) or runtime.get("default_mode")
    if selected is None:
        return None
    value = modes.get(selected)
    return float(value) if value is not None else None


def select_profiles(
    diagnosis_id: str,
    preferred_capabilities: list[str],
    profiles: list[dict[str, Any]],
    context: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    usable: list[tuple[float, dict[str, Any]]] = []
    rejected: list[dict[str, Any]] = []
    installed_versions = context.get("installed_versions", {})
    preferred_ids = set(context.get("preferred_family_ids", []))
    available_ids = set(context.get("available_family_ids", []))
    inventory_provided = "available_family_ids" in context
    budget = context.get("latency_budget_ms")
    realtime = bool(context.get("realtime"))
    trust_snapshot = bool(context.get("trust_catalog_snapshot"))
    runtime_host = str(context.get("host", "")).strip()
    runtime_format = str(context.get("format", "")).strip()
    runtime_sample_rate = context.get("sample_rate_hz")
    for profile in profiles:
        caps = profile.get("capabilities", {})
        exact = diagnosis_id in caps.get("diagnoses", [])
        preferred = caps.get("primary") in preferred_capabilities
        if not exact and not preferred:
            continue
        reasons = list(profile.get("catalog_warnings", []))
        family_id = profile.get("family_id")
        availability = profile.get("identity", {}).get("availability")
        if availability == "unavailable":
            reasons.append("unavailable")
        if inventory_provided and family_id not in available_ids:
            reasons.append("not_in_runtime_inventory")
        installed = installed_versions.get(family_id)
        observed = profile.get("identity", {}).get("version_range", "")
        if installed and not _version_matches(installed, observed):
            reasons.append("version_mismatch_exact_controls_suppressed")
        elif not installed and not trust_snapshot:
            reasons.append("runtime_version_unconfirmed_exact_controls_suppressed")
        elif not installed and trust_snapshot:
            reasons.append("catalog_snapshot_used_without_live_reconfirmation")
        tested_host = str(profile.get("identity", {}).get("tested_host", ""))
        if installed and not trust_snapshot and not runtime_host:
            reasons.append("host_unconfirmed_exact_controls_suppressed")
        if installed and not trust_snapshot and not runtime_format:
            reasons.append("format_unconfirmed_exact_controls_suppressed")
        if installed and not trust_snapshot and runtime_sample_rate is None:
            reasons.append("sample_rate_unconfirmed_exact_controls_suppressed")
        if runtime_host and runtime_host.casefold() not in tested_host.casefold():
            reasons.append("host_mismatch_exact_controls_suppressed")
        formats = [str(item).casefold() for item in profile.get("identity", {}).get("formats", [])]
        if runtime_format and runtime_format.casefold() not in formats:
            reasons.append("format_mismatch_exact_controls_suppressed")
        tested_sample_rate = profile.get("runtime_constraints", {}).get("tested_sample_rate_hz")
        if runtime_sample_rate and tested_sample_rate and int(runtime_sample_rate) != int(tested_sample_rate):
            reasons.append("sample_rate_mismatch_exact_controls_suppressed")
        latency = _latency_ms(profile, context)
        if realtime and budget is not None and latency is not None and latency > float(budget):
            reasons.append(f"latency_budget_exceeded:{latency:g}ms")
        if realtime and latency is None:
            reasons.append("latency_unknown_for_realtime")
        for rule in profile.get("conflict_rules", []):
            if rule.get("if") == f"diagnosis={diagnosis_id}" and str(rule.get("action", "")).startswith("reject"):
                reasons.append(rule["action"])
        hard_reasons = [
            r for r in reasons
            if r == "unavailable" or r == "not_in_runtime_inventory"
            or r.startswith("latency_budget_exceeded") or r.startswith("reject")
            or (r == "latency_unknown_for_realtime" and context.get("reject_unknown_latency", True))
        ]
        if hard_reasons:
            rejected.append({"adapter_id": profile.get("adapter_id"), "reasons": reasons})
            continue
        score = 0.0
        score += 4.0 if exact else 0.0
        score += 3.0 if preferred else 0.0
        score += 1.0 if availability == "current-filesystem-match" else 0.3
        score += 1.0 if profile.get("evidence", {}).get("level") == "L3" else 0.0
        score += 5.0 if family_id in preferred_ids else 0.0
        score -= 1.5 if reasons else 0.0
        confirmation_status = "snapshot-explicit" if trust_snapshot else (
            "live-context-confirmed" if installed and runtime_host and runtime_format and runtime_sample_rate else "incomplete"
        )
        runtime_confirmation = {
            "status": confirmation_status,
            "installed_version": installed,
            "host": runtime_host or None,
            "format": runtime_format or None,
            "sample_rate_hz": runtime_sample_rate,
            "inventory_provided": inventory_provided,
        }
        usable.append((score, {
            **profile,
            "runtime_warnings": reasons,
            "estimated_latency_ms": latency,
            "runtime_confirmation": runtime_confirmation,
        }))
    usable.sort(key=lambda item: (-item[0], item[1].get("identity", {}).get("product", "")))
    return [item[1] for item in usable], rejected
