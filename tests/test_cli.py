import argparse
import json
import tempfile
import unittest
from pathlib import Path

from ovc.cli import create_result, detect_hardware, detect_software, validate_result, write_json


class CliTests(unittest.TestCase):
    def test_detect_metadata_has_required_fields(self):
        hardware = detect_hardware()
        software = detect_software()

        self.assertTrue(hardware["platform"])
        self.assertTrue(software["python"])

    def test_create_result_is_valid(self):
        args = argparse.Namespace(
            github="alice",
            model="wan2.1",
            model_version="",
            model_source="",
            prompt_set="motion-basic-v1",
            prompt_set_version="1.0.0",
            task_id="benchmark-test-001",
            generation_time_sec=12.5,
            output_hash="sha256:test",
            log_hash=None,
            output_uri=None,
            command="ovc benchmark --model wan2.1",
            notes="test run",
            success=True,
        )

        result = create_result(args)

        self.assertEqual([], validate_result(result))
        self.assertEqual("benchmark-test-001", result["task_id"])
        self.assertEqual("success", result["run"]["status"])

    def test_validate_result_reports_missing_fields(self):
        errors = validate_result({"schema_version": "0.1.0"})

        self.assertIn("Missing required field: task_id", errors)
        self.assertIn("Missing required field: model", errors)

    def test_write_json_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "result.json"
            write_json(path, {"schema_version": "0.1.0"})

            self.assertTrue(path.exists())
            self.assertEqual({"schema_version": "0.1.0"}, json.loads(path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
