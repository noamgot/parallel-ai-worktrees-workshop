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

    def test_filter_then_summary(self):
        result = self.run_cli(ROOT / "data/sample.jsonl", "--severity", "ERROR", "--summary")
        self.assertEqual((result.returncode, result.stdout, result.stderr),
                         (0, "api: 1\nworker: 2\n", ""))

    def test_unfiltered_and_empty_summary(self):
        result = self.run_cli(ROOT / "data/sample.jsonl", "--summary")
        self.assertEqual((result.returncode, result.stdout), (0, "api: 2\ncache: 1\nworker: 3\n"))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.jsonl"
            path.write_text("", encoding="utf-8")
            result = self.run_cli(path, "--severity", "ERROR", "--summary")
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, "", ""))
