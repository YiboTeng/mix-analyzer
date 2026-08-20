from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mix_analyzer.decision import prescribe  # noqa: E402


KNOWLEDGE = ROOT / "skills" / "prescribe-mix-actions" / "knowledge"


def diagnosis(*ids: str, mode: str = "manual") -> dict:
    return {
        "schema_version": "1.0",
        "analysis_mode": mode,
        "context": {},
        "findings": [
            {
                "diagnosis_id": item,
                "direction": "high",
                "severity": 0.8,
                "confidence": 0.75,
                "scope": "lead-vocal",
                "calibration_required": True,
                "evidence": [{"listening_confirmation": item}],
            }
            for item in ids
        ],
    }


class DecisionTests(unittest.TestCase):
    def test_parallel_distortion_has_concrete_l3_plugin_guidance(self):
        out = prescribe(diagnosis("parallel_distortion"), KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(1, out["summary"]["action_count"])
        action = out["actions"][0]
        products = [item["product"] for item in action["plugin_options"]]
        self.assertIn("Abbey Road Saturator", products)
        selected = next(item for item in action["plugin_options"] if item["product"] == "Abbey Road Saturator")
        self.assertTrue(selected["start_points"])
        self.assertTrue(any("Mix" in point or "Input" in point for point in selected["start_points"]))
        self.assertEqual("send-return", action["routing_contract"]["routing_type"])
        self.assertIn("100% Wet", action["routing_contract"]["wet_policy"])
        self.assertEqual("D", action["provenance"]["p0_action_suitability_grade"])
        self.assertEqual("mixed:L2/L3", action["provenance"]["p1_control_validation_level"])

    def test_explicit_decapitator_preference_uses_l2_with_warning(self):
        out = prescribe(
            diagnosis("parallel_distortion"), KNOWLEDGE,
            {"preferred_family_ids": ["bc411ff14519"], "trust_catalog_snapshot": True},
        )
        selected = out["actions"][0]["plugin_options"][0]
        self.assertEqual("Decapitator", selected["product"])
        self.assertTrue(any("evidence_level_l2" in warning for warning in selected["runtime_warnings"]))
        self.assertTrue(selected["start_points"])

    def test_deess_is_ordered_before_harmonic_processing(self):
        out = prescribe(diagnosis("parallel_distortion", "sibilance"), KNOWLEDGE)
        stages = [item["chain_stage"] for item in out["actions"]]
        self.assertLess(stages.index("deessing"), stages.index("harmonic-tone"))
        harmonic = next(item for item in out["actions"] if item["chain_stage"] == "harmonic-tone")
        self.assertTrue(any("齿音" in warning for warning in harmonic["chain_warnings"]))
        deess = next(item for item in out["actions"] if item["chain_stage"] == "deessing")
        self.assertEqual("D", deess["provenance"]["p0_action_suitability_grade"])

    def test_version_mismatch_suppresses_exact_controls(self):
        context = {"installed_versions": {"497c2536aeff": "99.0"}}
        out = prescribe(diagnosis("mud"), KNOWLEDGE, context)
        proq = next(item for item in out["actions"][0]["plugin_options"] if item["family_id"] == "497c2536aeff")
        self.assertFalse(proq["exact_controls_allowed"])
        self.assertEqual([], proq["start_points"])
        self.assertTrue(any("version_mismatch" in warning for warning in proq["runtime_warnings"]))

    def test_realtime_breath_rejects_high_latency_debreath(self):
        out = prescribe(
            diagnosis("breath_too_loud"), KNOWLEDGE,
            {"realtime": True, "latency_budget_ms": 10},
        )
        action = out["actions"][0]
        self.assertEqual([], action["plugin_options"])
        self.assertTrue(any("latency_budget_exceeded" in reason for item in action["rejected_plugins"] for reason in item["reasons"]))
        self.assertTrue(any("Clip Gain" in step for step in action["operation"]["steps"]))

    def test_plosive_gets_dynamic_eq_not_dialogue_denoise(self):
        out = prescribe(diagnosis("plosive_low_frequency_event"), KNOWLEDGE)
        products = [item["product"] for item in out["actions"][0]["plugin_options"]]
        self.assertTrue("Pro-Q 3" in products or "F6" in products)
        self.assertNotIn("WNS", products)

    def test_mix_mode_does_not_treat_manual_as_wildcard(self):
        item = diagnosis("sibilance", mode="mix-reference")
        item["context"]["reference_gate"] = {"passed": True, "reasons": []}
        out = prescribe(item, KNOWLEDGE)
        self.assertEqual(0, out["summary"]["action_count"])
        self.assertEqual("no_mode_and_scope_safe_p0_card", out["unresolved"][0]["reason"])

    def test_master_scope_never_receives_vocal_low_mid_parameters(self):
        item = diagnosis("master_low_end_excess", mode="mix-reference")
        item["findings"][0]["scope"] = "mix-master"
        item["context"]["reference_gate"] = {"passed": True, "reasons": []}
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual("p0-master-low-end-excess", out["actions"][0]["card_id"])
        rendered = " ".join(out["actions"][0]["operation"]["parameter_start_ranges"])
        self.assertNotIn("男/低音域人声", rendered)
        self.assertIn("禁止套用人声高通", rendered)
        plugin_text = " ".join(
            point for plugin in out["actions"][0]["plugin_options"] for point in plugin["start_points"]
        )
        self.assertNotIn("60–90", plugin_text)
        self.assertTrue(all(not plugin["exact_controls_allowed"] for plugin in out["actions"][0]["plugin_options"]))

    def test_unknown_runtime_suppresses_exact_controls(self):
        out = prescribe(diagnosis("parallel_distortion"), KNOWLEDGE)
        self.assertTrue(out["actions"][0]["plugin_options"])
        self.assertTrue(all(not item["exact_controls_allowed"] for item in out["actions"][0]["plugin_options"]))

    def test_version_alone_does_not_unlock_exact_controls(self):
        out = prescribe(diagnosis("mud"), KNOWLEDGE, {"installed_versions": {"497c2536aeff": "3.2.3.0"}})
        proq = next(item for item in out["actions"][0]["plugin_options"] if item["family_id"] == "497c2536aeff")
        self.assertFalse(proq["exact_controls_allowed"])
        self.assertTrue(any("host_unconfirmed" in item for item in proq["runtime_warnings"]))

    def test_full_runtime_context_unlocks_matching_controls(self):
        out = prescribe(diagnosis("mud"), KNOWLEDGE, {
            "installed_versions": {"497c2536aeff": "3.2.3.0"},
            "host": "Ableton Live 11.3.43", "format": "VST3", "sample_rate_hz": 48000,
        })
        proq = next(item for item in out["actions"][0]["plugin_options"] if item["family_id"] == "497c2536aeff")
        self.assertTrue(proq["exact_controls_allowed"])
        self.assertEqual("live-context-confirmed", proq["runtime_confirmation"]["status"])

    def test_explicit_empty_inventory_rejects_all_plugins(self):
        out = prescribe(diagnosis("parallel_distortion"), KNOWLEDGE, {"available_family_ids": []})
        self.assertEqual([], out["actions"][0]["plugin_options"])
        self.assertTrue(any("not_in_runtime_inventory" in item["reasons"] for item in out["actions"][0]["rejected_plugins"]))

    def test_top_k_respects_destructive_prerequisite(self):
        item = diagnosis("sibilance", "parallel_distortion")
        item["findings"][0]["severity"] = 0.05
        item["findings"][0]["confidence"] = 0.3
        item["findings"][1]["severity"] = 1.0
        item["findings"][1]["confidence"] = 0.9
        out = prescribe(item, KNOWLEDGE, {"max_actions": 1})
        self.assertEqual("sibilance", out["actions"][0]["diagnosis_id"])
        self.assertEqual("prerequisite_not_delivered_within_action_budget", out["deferred_actions"][0]["reason"])

    def test_top_k_still_uses_value_when_no_dependency(self):
        item = diagnosis("broadband_stationary_noise", "adlib_width")
        item["findings"][0]["severity"] = 0.05
        item["findings"][0]["confidence"] = 0.3
        item["findings"][1]["severity"] = 1.0
        item["findings"][1]["confidence"] = 0.9
        item["findings"][1]["scope"] = "chorus-adlib"
        out = prescribe(item, KNOWLEDGE, {"max_actions": 1})
        self.assertEqual("adlib_width", out["actions"][0]["diagnosis_id"])

    def test_reference_gate_blocks_precise_actions(self):
        item = diagnosis("parallel_distortion", mode="vocal-reference")
        item["findings"][0]["scope"] = "target-vocal"
        item["context"]["reference_gate"] = {"passed": False, "reasons": ["fewer_than_two_independent_references"]}
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(0, out["summary"]["action_count"])
        self.assertEqual("reference_gate_failed", out["unresolved"][0]["reason"])

    def test_failed_gate_emits_only_one_gate_action(self):
        item = diagnosis("master_low_end_excess", "reference_mismatch", mode="mix-reference")
        item["findings"][0]["scope"] = "mix-master"
        item["findings"][1]["scope"] = "reference-set"
        item["context"]["reference_gate"] = {"passed": False, "reasons": ["fewer_than_two_independent_references"]}
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(1, out["summary"]["action_count"])
        self.assertEqual("reference_mismatch", out["actions"][0]["diagnosis_id"])

    def test_single_reference_emits_conditional_actions_without_exact_controls(self):
        item = diagnosis("master_low_end_excess", "reference_mismatch", mode="mix-reference")
        item["findings"][0]["scope"] = "mix-master"
        item["findings"][0]["confidence"] = 0.35
        item["findings"][1]["scope"] = "reference-set"
        item["findings"][1]["confidence"] = 0.35
        item["context"]["reference_gate"] = {
            "passed": False,
            "reasons": ["fewer_than_two_independent_references"],
            "reference_count": 1,
            "confidence_cap": 0.35,
        }
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(2, out["summary"]["action_count"])
        gate = next(action for action in out["actions"] if action["diagnosis_id"] == "reference_mismatch")
        conditional = next(action for action in out["actions"] if action["diagnosis_id"] == "master_low_end_excess")
        self.assertEqual("standard", gate["action_status"])
        self.assertEqual("conditional-hypothesis", conditional["action_status"])
        self.assertTrue(conditional["chain_warnings"])
        self.assertTrue(conditional["plugin_options"])
        self.assertTrue(all(not plugin["exact_controls_allowed"] for plugin in conditional["plugin_options"]))
        self.assertTrue(all(not plugin["start_points"] for plugin in conditional["plugin_options"]))

    def test_single_reference_merges_loudness_observation_into_reference_gate(self):
        item = diagnosis("loudness_bias_check", "reference_mismatch", mode="mix-reference")
        item["findings"][0]["scope"] = "mix-master"
        item["findings"][1]["scope"] = "reference-set"
        item["context"]["reference_gate"] = {
            "passed": False,
            "reasons": ["fewer_than_two_independent_references"],
            "reference_count": 1,
            "confidence_cap": 0.35,
        }
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(1, out["summary"]["action_count"])
        gate = out["actions"][0]
        self.assertEqual("reference_mismatch", gate["diagnosis_id"])
        self.assertEqual(
            ["loudness_bias_check", "reference_mismatch"], gate["diagnosis_ids"]
        )
        self.assertEqual("standard", gate["action_status"])
        self.assertEqual(2, len(gate["why"]["finding"]["evidence"]))

    def test_low_compatibility_still_blocks_single_reference_actions(self):
        item = diagnosis("master_low_end_excess", mode="mix-reference")
        item["findings"][0]["scope"] = "mix-master"
        item["context"]["reference_gate"] = {
            "passed": False,
            "reasons": ["fewer_than_two_independent_references", "low_reference_compatibility"],
            "reference_count": 1,
        }
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(0, out["summary"]["action_count"])
        self.assertEqual("reference_gate_failed", out["unresolved"][0]["reason"])

    def test_reference_mode_canonical_without_gate_defaults_to_blocked(self):
        item = diagnosis("master_low_end_excess", mode="mix-reference")
        item["findings"][0]["scope"] = "mix-master"
        out = prescribe(item, KNOWLEDGE, {"trust_catalog_snapshot": True})
        self.assertEqual(0, out["summary"]["action_count"])
        self.assertEqual(["missing_reference_gate"], out["context"]["reference_gate"]["reasons"])

    def test_user_reported_band_is_first_audition_window(self):
        item = diagnosis("sibilance")
        item["findings"][0]["evidence"] = [{
            "evidence_kind": "user_report", "reported_band_hz": [7000, 10000],
            "listening_confirmation": "7–10 kHz 辅音刺耳",
        }]
        out = prescribe(item, KNOWLEDGE)
        self.assertIn("7000–10000 Hz", out["actions"][0]["disambiguation_tests"][0])
        self.assertIn("3–5 个最坏", out["actions"][0]["verification_protocol"]["measurement_window"])

    def test_relationship_cards_require_stems(self):
        item = diagnosis("frequency_masking")
        item["findings"][0]["scope"] = "vocal-instrument-relationship"
        blocked = prescribe(item, KNOWLEDGE)
        self.assertEqual(0, blocked["summary"]["action_count"])
        allowed = prescribe(item, KNOWLEDGE, {"stems_available": True})
        self.assertEqual("p0-vocal-beat-masking", allowed["actions"][0]["card_id"])

    def test_relationship_scope_suppresses_unscoped_plugin_recipes(self):
        item = diagnosis("frequency_masking")
        item["findings"][0]["scope"] = "vocal-instrument-relationship"
        out = prescribe(item, KNOWLEDGE, {"stems_available": True, "trust_catalog_snapshot": True})
        plugins = out["actions"][0]["plugin_options"]
        self.assertTrue(plugins)
        self.assertTrue(all(not plugin["exact_controls_allowed"] for plugin in plugins))
        self.assertFalse(any("60–90" in point for plugin in plugins for point in plugin["start_points"]))
        self.assertTrue(all(
            route["when"] == "frequency_masking" for plugin in plugins for route in plugin["route_options"]
        ))

    def test_prerequisite_and_sibilance_route_are_scope_specific(self):
        item = diagnosis("sibilance", "parallel_distortion")
        item["findings"][0]["scope"] = "vocal-bus"
        item["findings"][0]["severity"] = 0.1
        item["findings"][1]["scope"] = "lead-vocal"
        item["findings"][1]["severity"] = 1.0
        out = prescribe(item, KNOWLEDGE, {"max_actions": 1})
        self.assertEqual("parallel_distortion", out["actions"][0]["diagnosis_id"])
        deess_only = prescribe(diagnosis("sibilance"), KNOWLEDGE)
        self.assertEqual("lead-vocal insert", deess_only["actions"][0]["routing_contract"]["target_bus"])
        bus_item = diagnosis("sibilance")
        bus_item["findings"][0]["scope"] = "vocal-bus"
        bus = prescribe(bus_item, KNOWLEDGE)
        self.assertEqual("vocal-bus insert", bus["actions"][0]["routing_contract"]["target_bus"])


if __name__ == "__main__":
    unittest.main()
