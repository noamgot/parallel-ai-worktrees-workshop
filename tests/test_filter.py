from copy import deepcopy
import unittest
from loglab.filtering import filter_records


class FilterAcceptance(unittest.TestCase):
    def setUp(self):
        self.records = [dict(severity=s, component=c, message=m, extra={"id": i})
                        for i, (s, c, m) in enumerate([
                            ("ERROR", "api", "Request rejected"),
                            ("INFO", "worker", "request accepted"),
                            ("WARNING", "api", "request slow"),
                            ("ERROR", "API", "request rejected"),
                            ("ERROR", "worker", "request rejected")])]

    def test_disabled_filters_return_new_list(self):
        selected = filter_records(self.records, None, None, None)
        self.assertEqual(selected, self.records)
        self.assertIsNot(selected, self.records)

    def test_empty_collections_match_nothing(self):
        self.assertEqual(filter_records(self.records, severities=[]), [])
        self.assertEqual(filter_records(self.records, components=[]), [])

    def test_or_within_and_across_filters_preserves_order(self):
        selected = filter_records(self.records, ["ERROR", "WARNING"], ["api", "worker"], "request")
        self.assertEqual(selected, [self.records[2], self.records[4]])

    def test_exact_case_sensitive_collections(self):
        self.assertEqual(filter_records(self.records, ["error"]), [])
        self.assertEqual(filter_records(self.records, components=["API"]), [self.records[3]])
        self.assertEqual(filter_records(self.records, components=["ap"]), [])

    def test_message_substring_and_case(self):
        self.assertEqual(filter_records(self.records, message="Request"), [self.records[0]])
        self.assertEqual(filter_records(self.records, message="accept"), [self.records[1]])
        self.assertEqual(filter_records(self.records, message=""), self.records)

    def test_no_matches_and_empty_input(self):
        self.assertEqual(filter_records(self.records, message="missing"), [])
        self.assertEqual(filter_records([], ["ERROR"]), [])

    def test_no_mutation_and_new_filtered_list(self):
        original = deepcopy(self.records)
        selected = filter_records(self.records, ["ERROR"])
        self.assertEqual(selected, [self.records[0], self.records[3], self.records[4]])
        self.assertIsNot(selected, self.records)
        self.assertEqual(self.records, original)
