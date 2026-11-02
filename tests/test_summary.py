from copy import deepcopy
import unittest
from loglab.summary import summarize_records


class SummaryAcceptance(unittest.TestCase):
    def setUp(self):
        self.records = [dict(severity=s, component=c, message="synthetic", extra=[1])
                        for c, s in [("worker", "ERROR"), ("api", "INFO"),
                                     ("worker", "INFO"), ("API", "WARNING"),
                                     ("api", "ERROR"), ("worker", "ERROR"),
                                     ("cache", "DEBUG")]]
        self.expected = [
            {"component": "worker", "total": 3, "severities": {"ERROR": 2, "INFO": 1}},
            {"component": "api", "total": 2, "severities": {"INFO": 1, "ERROR": 1}},
            {"component": "API", "total": 1, "severities": {"WARNING": 1}},
            {"component": "cache", "total": 1, "severities": {"DEBUG": 1}}]

    def test_counts_observed_severities_and_ranking(self):
        self.assertEqual(summarize_records(self.records), self.expected)

    def test_ties_are_case_sensitive_component_order(self):
        records = [dict(component=c, severity="INFO", message="x")
                   for c in ("api", "worker", "API")]
        self.assertEqual([r["component"] for r in summarize_records(records)], ["API", "api", "worker"])

    def test_top_limits(self):
        for n in (0, 1, 2, 10):
            with self.subTest(top_n=n):
                self.assertEqual(summarize_records(self.records, top_n=n), self.expected[:n])
        self.assertEqual(summarize_records(self.records, top_n=None), self.expected)

    def test_empty_input(self):
        self.assertEqual(summarize_records([]), [])
        self.assertEqual(summarize_records([], top_n=0), [])

    def test_no_mutation(self):
        original = deepcopy(self.records)
        summarize_records(self.records, top_n=1)
        self.assertEqual(self.records, original)
