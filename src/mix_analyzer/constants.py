from __future__ import annotations

PLUGIN_ID = "mix-analyzer"
ANALYZER_VERSION = "legacy-compat-0.1"
DECISION_ENGINE_VERSION = "0.1.0"
DIAGNOSIS_SCHEMA_VERSION = "1.0"
TREATMENT_SCHEMA_VERSION = "1.0"

CONFIDENCE_SCORES = {
    "证据不足": 0.0,
    "低": 0.25,
    "中低": 0.4,
    "中": 0.6,
    "中高": 0.8,
    "高": 0.95,
    "low": 0.25,
    "medium-low": 0.4,
    "medium": 0.6,
    "medium-high": 0.8,
    "high": 0.95,
}

CHAIN_STAGE_ORDER = {
    "reference-gate": 0,
    "editing-restoration": 10,
    "pitch-timing": 20,
    "corrective-eq": 30,
    "leveling": 40,
    "peak-dynamics": 50,
    "spectral-dynamics": 60,
    "deessing": 70,
    "harmonic-tone": 80,
    "width-layering": 90,
    "space-delay": 100,
    "bus-balance": 110,
    "clip-limit": 120,
    "metering": 130,
}

