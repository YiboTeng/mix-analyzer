from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "compare-mix-references" / "scripts"
sys.path.insert(0, str(SCRIPTS))

try:
    from compare_mix_references import plot_reference_set, reference_summary
except ImportError as exc:  # CI/local core-only environments may omit audio-analysis dependencies.
    plot_reference_set = reference_summary = None
    IMPORT_ERROR = exc
else:
    IMPORT_ERROR = None


def record(lufs: float, plr: float, sub: float, presence: float, high_side: float, mono_loss: float) -> dict:
    tonal = [sub, 0, 0, 0, 0, presence, presence, 0, high_side, high_side]
    width = [0, 0, 0, 0, 0, 0, 0, high_side, high_side, high_side]
    return {
        "loudness": {"lufs_i": lufs, "plr_db": plr},
        "tonal": {"band_relative_db": tonal},
        "stereo": {"band_side_mid_db": width, "mono_fold_loss_db": mono_loss},
    }


@unittest.skipIf(IMPORT_ERROR is not None, f"analysis dependencies unavailable: {IMPORT_ERROR}")
class MixReferenceStatisticsTests(unittest.TestCase):
    def test_single_reference_has_raw_delta_without_fake_robust_score(self):
        summary = reference_summary({
            "Target": record(-10.0, 10.0, 4.0, -3.0, -7.0, -0.1),
            "Reference": record(-8.0, 8.0, 0.0, -1.0, -8.0, -0.4),
        })
        self.assertEqual("single_reference_raw_delta_only", summary["statistical_status"])
        self.assertEqual({}, summary["outliers"])
        self.assertIsNone(summary["features"]["Sub"]["robust_deviation"])
        self.assertEqual(4.0, summary["features"]["Sub"]["target_minus_reference_median"])

    def test_single_reference_plot_labels_insufficient_outlier_evidence(self):
        records = {
            "Target": record(-10.0, 10.0, 4.0, -3.0, -7.0, -0.1),
            "Reference": record(-8.0, 8.0, 0.0, -1.0, -8.0, -0.4),
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp)
            plot_reference_set(records, reference_summary(records), out_dir)
            chart = out_dir / "M11_reference_intervals.png"
            self.assertTrue(chart.is_file())
            self.assertGreater(chart.stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
