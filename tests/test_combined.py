import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CombinedAcceptance(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-m", "loglab", *map(str, args)],
                              cwd=ROOT, capture_output=True, text=True)

    def assert_output(self, args, expected):
        result = self.run_cli(ROOT / "data/sample.jsonl", *args)
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, expected, ""))

    def test_filter_then_summary(self):
        self.assert_output(["--severity", "ERROR", "--summary"],
                           "api: total=2 ERROR=2\nworker: total=2 ERROR=2\nAPI: total=1 ERROR=1\n")

    def test_repeatable_filters_message_and_top(self):
        self.assert_output(["--severity", "ERROR", "--severity", "INFO",
                            "--component", "api", "--component", "worker",
                            "--message", "rejected", "--summary", "--top", "1"],
                           "api: total=2 ERROR=2\n")

    def test_unfiltered_summary_ranking_and_severity_order(self):
        self.assert_output(["--summary"],
                           "worker: total=5 CRITICAL=1 DEBUG=1 ERROR=2 INFO=1\n"
                           "api: total=4 ERROR=2 INFO=1 WARNING=1\n"
                           "cache: total=3 DEBUG=1 INFO=1 WARNING=1\n"
                           "scheduler: total=2 INFO=1 WARNING=1\n"
                           "API: total=1 ERROR=1\n")

    def test_filtered_json_keeps_extra_fields_and_order(self):
        result = self.run_cli(ROOT / "data/sample.jsonl", "--component", "api", "--message", "accepted")
        self.assertEqual((result.returncode, result.stderr), (0, ""))
        self.assertEqual([json.loads(line) for line in result.stdout.splitlines()], [
            dict(severity="INFO", component="api", message="Synthetic request accepted", request_id="demo-001")])

    def test_case_sensitive_message_and_component(self):
        self.assert_output(["--component", "API", "--message", "Request", "--summary"],
                           "API: total=1 ERROR=1\n")

    def test_empty_results_and_top_zero(self):
        for args in (["--component", "missing"], ["--message", "missing", "--summary"],
                     ["--summary", "--top", "0"]):
            with self.subTest(args=args):
                self.assert_output(args, "")

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.jsonl"
            path.write_text("", encoding="utf-8")
            for args in ([], ["--summary"], ["--severity", "ERROR", "--summary"]):
                result = self.run_cli(path, *args)
                self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))

    def test_invalid_top(self):
        for args in (["--top", "1"], ["--summary", "--top", "-1"],
                     ["--summary", "--top", "nope"]):
            with self.subTest(args=args):
                result = self.run_cli(ROOT / "data/sample.jsonl", *args)
                self.assertEqual((result.returncode, result.stdout), (2, ""))
                self.assertIn("--top", result.stderr)
