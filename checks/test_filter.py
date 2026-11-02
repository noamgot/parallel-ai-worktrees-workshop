from copy import deepcopy
import unittest
from loglab.filtering import filter_records


class FilterAcceptance(unittest.TestCase):
    def test_contract(self):
        records = [dict(severity=s, component="api", message=str(i))
                   for i, s in enumerate(("ERROR", "INFO", "ERROR", "CRITICAL"))]
        original = deepcopy(records)
        selected = filter_records(records, "ERROR")
        self.assertEqual(selected, [records[0], records[2]])
        self.assertIsNot(selected, records)
        self.assertEqual(records, original)
        all_records = filter_records(records)
        self.assertEqual(all_records, records)
        self.assertIsNot(all_records, records)
        self.assertEqual(filter_records(records, "DEBUG"), [])
        self.assertEqual(filter_records([], "ERROR"), [])
