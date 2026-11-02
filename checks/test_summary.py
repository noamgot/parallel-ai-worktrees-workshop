from copy import deepcopy
import unittest
from loglab.summary import summarize_records


class SummaryAcceptance(unittest.TestCase):
    def test_counts_and_immutability(self):
        records = [dict(severity="INFO", component=c, message="synthetic")
                   for c in ("worker", "api", "worker", "API")]
        original = deepcopy(records)
        self.assertEqual(summarize_records(records), {"worker": 2, "api": 1, "API": 1})
        self.assertEqual(records, original)
        self.assertEqual(summarize_records([]), {})
