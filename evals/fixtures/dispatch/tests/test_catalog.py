import unittest

from catalog import Request, list_requests, search_requests


class CatalogTests(unittest.TestCase):
    def test_list_preserves_input_order(self):
        rows = [Request("B", "안전모", "보류"), Request("A", "장갑", "접수")]
        self.assertEqual(list_requests(rows), rows)

    def test_search_matches_part_of_title(self):
        gloves = Request("A", "작업 장갑", "접수")
        helmet = Request("B", "안전모", "접수")
        self.assertEqual(search_requests([gloves, helmet], "장갑"), [gloves])
