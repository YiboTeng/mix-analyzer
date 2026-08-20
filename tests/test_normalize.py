from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mix_analyzer.normalize import _normalize_manual_confidence, normalize_mix, normalize_vocal  # noqa: E402


class NormalizeTests(unittest.TestCase):
    def test_vocal_feature_creates_calibration_flagged_finding(self):
        payload = {
            "schema": "vocal-reference-set-v1",
            "features": {
                "low_mid_masking_db": {
                    "target": 4.0,
                    "reference_median": 1.0,
                    "target_minus_reference_median": 3.0,
                    "practical_floor": 1.0,
                    "outside_reference_iqr": True,
                    "confidence": "中",
                    "unit": "dB",
                }
            },
            "references": [{"label": "R1"}, {"label": "R2"}, {"label": "R3"}],
        }
        out = normalize_vocal(payload)
        self.assertEqual("mud", out["findings"][0]["diagnosis_id"])
        self.assertTrue(out["findings"][0]["calibration_required"])
        self.assertFalse(out["context"]["automatic_thresholds_calibrated"])

    def test_mix_requires_consistent_robust_deviation(self):
        payload = {
            "schema": "mix-reference-metrics-v1",
            "references": ["R1", "R2", "R3"],
            "reference_set": {"features": {
                "Presence": {
                    "target": 2.0, "reference_median": 0.0,
                    "robust_deviation": 1.8, "direction_consistency": 0.9,
                },
                "Sub": {
                    "target": 2.0, "reference_median": 0.0,
                    "robust_deviation": 2.0, "direction_consistency": 0.4,
                },
            }},
        }
        out = normalize_mix(payload)
        self.assertEqual(["master_presence_excess"], [item["diagnosis_id"] for item in out["findings"]])

    def test_mix_stems_add_masking_and_low_frequency_width_findings(self):
        payload = {
            "schema": "mix-reference-metrics-v1",
            "target": "T",
            "references": ["R1", "R2"],
            "reference_set": {"features": {}},
            "records": {
                "T": {"stems": {
                    "origin": "original_stems", "presence_mask_risk": 0.22,
                    "hat_sibilance_mask_risk": 0.12, "vir_median_db": -4.0,
                    "spatial_width_gap_db": 5.0, "bass": {"side_mid_db": -8.0},
                }},
                "R1": {"stems": {
                    "origin": "official_stems", "presence_mask_risk": 0.10,
                    "hat_sibilance_mask_risk": 0.10, "vir_median_db": -1.0,
                    "spatial_width_gap_db": 2.0, "bass": {"side_mid_db": -12.0},
                }},
                "R2": {"stems": {
                    "origin": "official_stems", "presence_mask_risk": 0.12,
                    "hat_sibilance_mask_risk": 0.09, "vir_median_db": -2.0,
                    "spatial_width_gap_db": 1.0, "bass": {"side_mid_db": -13.0},
                }},
            },
        }
        out = normalize_mix(payload)
        ids = {item["diagnosis_id"] for item in out["findings"]}
        self.assertTrue({"frequency_masking", "presence_dullness", "vocal_instrument_width_gap", "low_frequency_mono"}.issubset(ids))

    def test_low_direction_maps_to_restoration_not_more_reduction(self):
        vocal = normalize_vocal({
            "schema": "vocal-reference-set-v1",
            "cohort": {"count": 3},
            "references": [{"path": "a"}, {"path": "b"}, {"path": "c"}],
            "features": {"crest_factor_db": {
                "target_minus_reference_median": -3.0, "practical_floor": 1.0,
                "outside_reference_iqr": True, "confidence": "中高",
            }},
        })
        self.assertEqual("overcompressed_vocal", vocal["findings"][0]["diagnosis_id"])
        mix = normalize_mix({
            "schema": "mix-reference-metrics-v1", "references": ["a", "b", "c"],
            "reference_set": {"features": {"Sub": {
                "robust_deviation": -2.0, "direction_consistency": 0.9,
            }}},
        })
        self.assertEqual("master_low_end_deficit", mix["findings"][0]["diagnosis_id"])

    def test_single_reference_creates_failed_gate_finding(self):
        out = normalize_mix({
            "schema": "mix-reference-metrics-v1", "references": ["only"],
            "reference_set": {"features": {"Sub": {
                "target": 4.0, "reference_median": 0.0,
                "target_minus_reference_median": 4.0,
                "robust_deviation": None, "direction_consistency": 1.0,
            }}},
        })
        self.assertFalse(out["context"]["reference_gate"]["passed"])
        self.assertIn("reference_mismatch", [item["diagnosis_id"] for item in out["findings"]])
        sub = next(item for item in out["findings"] if item["diagnosis_id"] == "master_low_end_excess")
        self.assertLessEqual(sub["confidence"], 0.35)
        self.assertLessEqual(sub["severity"], 0.65)
        self.assertIsNone(sub["evidence"][0]["robust_deviation"])
        self.assertEqual("single_reference_raw_delta_only", sub["evidence"][0]["statistical_status"])

    def test_safer_mono_fold_does_not_create_risk(self):
        out = normalize_mix({
            "schema": "mix-reference-metrics-v1", "references": ["only"],
            "reference_set": {"features": {"Mono Loss": {
                "target": -0.09, "reference_median": -0.39,
                "target_minus_reference_median": 0.30,
                "robust_deviation": None, "direction_consistency": 1.0,
            }}},
        })
        self.assertNotIn("mono_translation_risk", [item["diagnosis_id"] for item in out["findings"]])

    def test_more_negative_mono_fold_creates_risk(self):
        out = normalize_mix({
            "schema": "mix-reference-metrics-v1", "references": ["only"],
            "reference_set": {"features": {"Mono Loss": {
                "target": -1.0, "reference_median": -0.2,
                "target_minus_reference_median": -0.8,
                "robust_deviation": None, "direction_consistency": 1.0,
            }}},
        })
        risk = next(item for item in out["findings"] if item["diagnosis_id"] == "mono_translation_risk")
        self.assertEqual("low", risk["direction"])

    def test_manual_listening_confidence_is_capped_and_labeled(self):
        payload = {
            "schema_version": "1.0", "analysis_mode": "manual", "context": {},
            "findings": [{
                "diagnosis_id": "sibilance", "direction": "high", "severity": 0.8,
                "confidence": 0.95, "scope": "lead-vocal", "evidence": [{
                    "evidence_kind": "equal_loudness_listening_confirmation",
                    "listening_confirmation": "刺耳",
                }],
            }],
        }
        out = _normalize_manual_confidence(payload)
        self.assertEqual(0.7, out["findings"][0]["confidence"])
        self.assertEqual("equal_loudness_listening_confirmation", out["findings"][0]["confidence_basis"])

    def test_all_separated_vocal_references_cap_confidence(self):
        out = normalize_vocal({
            "schema": "vocal-reference-set-v1",
            "references": [
                {"path": "a", "separated": True}, {"path": "b", "separated": True}, {"path": "c", "separated": True},
            ],
            "cohort": {"count": 3},
            "features": {"air_db": {
                "target_minus_reference_median": 3.0, "practical_floor": 1.0,
                "outside_reference_iqr": True, "confidence": "高",
            }},
        })
        self.assertTrue(out["context"]["reference_gate"]["passed"])
        self.assertIn("all_references_source_separated", out["context"]["reference_gate"]["limitations"])
        self.assertLessEqual(out["findings"][0]["confidence"], 0.45)

    def test_majority_separated_vocal_references_cap_confidence(self):
        out = normalize_vocal({
            "schema": "vocal-reference-set-v1",
            "references": [
                {"path": "a", "separated": True}, {"path": "b", "separated": True}, {"path": "c", "separated": False},
            ],
            "cohort": {"count": 3},
            "features": {"air_db": {
                "target_minus_reference_median": 3.0, "practical_floor": 1.0,
                "outside_reference_iqr": True, "confidence": "高",
            }},
        })
        self.assertIn("majority_references_source_separated", out["context"]["reference_gate"]["limitations"])
        self.assertLessEqual(out["findings"][0]["confidence"], 0.45)

    def test_single_stem_reference_does_not_form_relationship_finding(self):
        out = normalize_mix({
            "schema": "mix-reference-metrics-v1", "target": "T", "references": ["R1", "R2", "R3"],
            "reference_set": {"features": {}},
            "records": {
                "T": {"stems": {"origin": "original_stems", "presence_mask_risk": 0.5}},
                "R1": {"stems": {"origin": "official_stems", "presence_mask_risk": 0.1}},
                "R2": {"stems": None}, "R3": {"stems": None},
            },
        })
        self.assertEqual([], out["findings"])
        self.assertFalse(out["context"]["stems_available"])
        self.assertEqual(1, out["context"]["stem_reference_count"])


if __name__ == "__main__":
    unittest.main()
