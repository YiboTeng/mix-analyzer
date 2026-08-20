from __future__ import annotations

import json
import hashlib
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
P1 = ROOT / "skills" / "prescribe-mix-actions" / "knowledge" / "p1"

from mix_analyzer.catalog import _latency_ms, _version_matches, load_profiles  # noqa: E402


class CatalogSnapshotTests(unittest.TestCase):
    def test_p0_sources_are_packaged_without_missing_paths(self):
        manifest = json.loads((P1.parent / "p0" / "source-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual([], manifest["missing"])
        self.assertEqual(manifest["referenced_count"], manifest["packaged_count"])
        for entry in manifest["entries"]:
            path = P1.parent / entry["packaged_path"]
            self.assertTrue(path.is_file())
            self.assertEqual(entry["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())

    def test_snapshot_has_40_profiles_and_passed_source_audit(self):
        manifest = json.loads((P1 / "runtime-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(40, manifest["profile_count"])
        self.assertEqual("passed", manifest["source_audit"]["status"])
        self.assertEqual(40, len(list((P1 / "profiles").glob("*.json"))))
        supplemental = json.loads((P1 / "supplemental" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(7, supplemental["count"])

    def test_packaged_evidence_exists_and_has_no_audio(self):
        for profile_path in (P1 / "profiles").glob("*.json"):
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            packaged = profile["evidence"]["packaged"]
            entries = [packaged["card"], packaged["source_note"], packaged["validation_report"], *packaged["result_files"]]
            for entry in entries:
                self.assertTrue((P1 / entry["packaged_path"]).is_file(), entry)
                evidence_path = P1 / entry["packaged_path"]
                self.assertEqual(entry["sha256"], hashlib.sha256(evidence_path.read_bytes()).hexdigest())
        forbidden = {".wav", ".flac", ".mp3", ".als", ".song"}
        self.assertFalse(any(path.suffix.lower() in forbidden for path in P1.rglob("*")))

    def test_profiles_include_structured_parameter_start_points(self):
        profiles = [json.loads(path.read_text(encoding="utf-8")) for path in (P1 / "profiles").glob("*.json")]
        with_starts = sum(bool(item["local_guidance"]["parameter_start_points"]) for item in profiles)
        self.assertGreaterEqual(with_starts, 35)

    def test_runtime_catalog_excludes_supplemental_manifest(self):
        profiles = load_profiles(P1.parent)
        self.assertEqual(47, len(profiles))
        self.assertTrue(all(item.get("adapter_id") for item in profiles))

    def test_supplemental_profiles_and_evidence_match_manifest_hashes(self):
        manifest = json.loads((P1 / "supplemental" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(7, len(manifest["entries"]))
        for entry in manifest["entries"]:
            profile_path = P1.parent / entry["profile"]
            self.assertEqual(entry["sha256"], hashlib.sha256(profile_path.read_bytes()).hexdigest())
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            for key in ("card", "source_note"):
                evidence = profile["evidence"]["packaged"][key]
                evidence_path = P1.parent / evidence["packaged_path"]
                self.assertTrue(evidence_path.is_file())
                self.assertEqual(evidence["sha256"], hashlib.sha256(evidence_path.read_bytes()).hexdigest())

    def test_version_alternatives_match_individually(self):
        self.assertTrue(_version_matches("v2.0", "1.0 | 2.0 | 3.0"))
        self.assertFalse(_version_matches("4.0", "1.0 | 2.0 | 3.0"))
        self.assertFalse(_version_matches(None, "1.0"))

    def test_latency_does_not_parse_effect_delay_as_host_latency(self):
        profiles = load_profiles(P1.parent)
        doubler = next(item for item in profiles if item["identity"]["product"] == "Doubler")
        timeless = next(item for item in profiles if item["identity"]["product"] == "Timeless 3")
        proq = next(item for item in profiles if item["identity"]["product"] == "Pro-Q 3")
        self.assertIsNone(_latency_ms(doubler, {}))
        self.assertIsNone(_latency_ms(timeless, {}))
        self.assertEqual(0.0, _latency_ms(proq, {}))
        self.assertEqual(106.7, _latency_ms(proq, {"plugin_modes": {"497c2536aeff": "linear-phase-max"}}))
        self.assertEqual(3.5, _latency_ms(doubler, {"host_latency_ms": {"4bceae9f0a6f": 3.5}}))


if __name__ == "__main__":
    unittest.main()
