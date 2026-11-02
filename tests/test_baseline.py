import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from loglab.__main__ import main
from loglab.input import read_records

ROOT = Path(__file__).resolve().parents[1]


class Baseline(unittest.TestCase):
    def invoke(self, args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(args)
        return code, out.getvalue(), err.getvalue()

    def test_sample_and_plain_cli(self):
        records = read_records(ROOT / "data/sample.jsonl")
        self.assertEqual(len(records), 15)
        code, out, err = self.invoke([str(ROOT / "data/sample.jsonl")])
        self.assertEqual((code, err), (0, ""))
        self.assertEqual([json.loads(line) for line in out.splitlines()], records)

    def test_help(self):
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as caught:
            main(["--help"])
        self.assertEqual(caught.exception.code, 0)

    def test_input_validation(self):
        for text in ('not json', '[]', '{}', '{"severity":"error","component":"x","message":"x"}',
                     '{"severity":"INFO","component":"","message":"x"}'):
            with self.subTest(text=text), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "input.jsonl"
                path.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "line 1"):
                    read_records(path)

    def test_blank_lines_empty_file_and_extra_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.jsonl"
            path.write_text("\n", encoding="utf-8")
            self.assertEqual(read_records(path), [])
            record = dict(severity="INFO", component="api", message="x", extra=42)
            path.write_text("\n" + json.dumps(record), encoding="utf-8")
            self.assertEqual(read_records(path), [record])

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            code, out, err = self.invoke([str(Path(directory) / "missing")])
        self.assertEqual((code, out), (2, ""))
        self.assertIn("loglab:", err)

    def test_unfinished_error_is_clear(self):
        with patch("loglab.__main__.filter_records", side_effect=NotImplementedError("workshop: unfinished")):
            with self.assertRaisesRegex(NotImplementedError, "workshop: unfinished"):
                self.invoke([str(ROOT / "data/sample.jsonl")])
