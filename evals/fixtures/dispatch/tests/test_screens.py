import unittest

from app import open_from_list
from catalog import Request


class ScreenTests(unittest.TestCase):
    def test_held_urgent_request_opens_hold_review_from_list(self):
        row = Request("A", "절연 장갑", "보류", urgent=True)
        self.assertEqual(open_from_list([row], "A"), "hold-review")

    def test_open_urgent_request_opens_urgent_desk(self):
        row = Request("B", "안전모", "접수", urgent=True)
        self.assertEqual(open_from_list([row], "B"), "urgent-desk")
