import argparse
import json
import tempfile
import unittest
from pathlib import Path

from ovc.cli import (
    create_result,
    detect_hardware,
    detect_software,
    generate_report,
    load_benchmark_results,
    parse_apple_chip,
    parse_nvidia_smi,
    validate_result,
    write_json,
)


class CliTests(unittest.TestCase):
    def test_detect_metadata_has_required_fields(self):
        hardware = detect_hardware()
        software = detect_software()

        self.assertTrue(hardware["platform"])
        self.assertTrue(software["python"])

    def test_parse_nvidia_smi_output(self):
        output = "NVIDIA GeForce RTX 4090, 24564\nNVIDIA GeForce RTX 3090, 24576\n"

        result = parse_nvidia_smi(output)

        self.assertEqual("NVIDIA GeForce RTX 4090; NVIDIA GeForce RTX 3090", result["gpu"])
        self.assertEqual(24.0, result["vram_gb"])

    def test_parse_apple_chip_output(self):
        output = """
Hardware:

    Hardware Overview:

      Chip: Apple M4 Pro
      Total Number of Cores: 14 (10 performance and 4 efficiency)
      Memory: 48 GB
"""

        result = parse_apple_chip(output)

        self.assertEqual("Apple M4 Pro integrated GPU", result["gpu"])
        self.assertEqual(48.0, result["ram_gb"])

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

    def test_load_benchmark_results_skips_invalid_records(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = root / "results" / "wan2.1" / "valid.json"
            invalid = root / "results" / "wan2.1" / "invalid.json"
            write_json(valid, self._valid_result("alice", "RTX 4090", 42))
            write_json(invalid, {"schema_version": "0.1.0"})

            results = load_benchmark_results(root / "results")

            self.assertEqual(1, len(results))
            self.assertEqual("alice", results[0]["contributor"]["github"])

    def test_generate_report_contains_summary_table(self):
        results = [
            self._valid_result("alice", "RTX 4090", 42),
            self._valid_result("bob", "Apple M4", 84),
        ]

        report = generate_report(results, title="Test Report")

        self.assertIn("# Test Report", report)
        self.assertIn("- Hardware profiles: 2", report)
        self.assertIn("| wan2.1 | RTX 4090 | motion-basic-v1 | success | 42.0s | alice |", report)
        self.assertIn("| wan2.1 | Apple M4 | motion-basic-v1 | success | 84.0s | bob |", report)

    def _valid_result(self, github: str, gpu: str, generation_time_sec: float):
        args = argparse.Namespace(
            github=github,
            model="wan2.1",
            model_version="starter",
            model_source="",
            prompt_set="motion-basic-v1",
            prompt_set_version="1.0.0",
            task_id=f"benchmark-{github}",
            generation_time_sec=generation_time_sec,
            output_hash=None,
            log_hash=None,
            output_uri=None,
            command="ovc benchmark --model wan2.1",
            notes="test run",
            success=True,
        )
        result = create_result(args)
        result["hardware"]["gpu"] = gpu
        return result


if __name__ == "__main__":
    unittest.main()
