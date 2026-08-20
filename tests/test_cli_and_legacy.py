from __future__ import annotations

import ast
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mix_analyzer.cli import main  # noqa: E402


class CliAndLegacyTests(unittest.TestCase):
    def test_all_python_sources_parse(self):
        for path in [*ROOT.glob("src/**/*.py"), *ROOT.glob("skills/**/scripts/*.py"), *ROOT.glob("scripts/*.py")]:
            ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))

    def test_cli_writes_three_artifacts(self):
        payload = {
            "schema_version": "1.0",
            "analysis_mode": "manual",
            "context": {},
            "findings": [{
                "diagnosis_id": "parallel_distortion",
                "direction": "missing", "severity": 0.7, "confidence": 0.7,
                "scope": "lead-vocal", "calibration_required": True,
                "evidence": [{"listening_confirmation": "grain missing"}],
            }],
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "diagnosis.json"
            source.write_text(json.dumps(payload), encoding="utf-8")
            out = root / "out"
            code = main(["--input", str(source), "--out-dir", str(out)])
            self.assertEqual(0, code)
            for name in ("diagnosis-evidence.json", "treatment-plan.json", "treatment-plan.md"):
                self.assertTrue((out / name).is_file(), name)
            report = (out / "treatment-plan.md").read_text(encoding="utf-8")
            self.assertIn("Abbey Road Saturator", report)
            self.assertIn("复测", report)
            self.assertIn("用户/分析证据", report)
            self.assertIn("grain missing", report)
            self.assertIn("需要语料校准：是", report)
            self.assertIn("打包来源", report)
            self.assertIn("精确旋钮已抑制", report)
            self.assertIn("目标轨/Bus", report)
            self.assertIn("操作化验收", report)


if __name__ == "__main__":
    unittest.main()
