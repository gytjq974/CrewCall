import unittest
from unittest.mock import Mock, call

from transport import fetch_request, submit_request


class TransportTests(unittest.TestCase):
    def test_fetch_retries_once_after_timeout(self):
        send = Mock(side_effect=[TimeoutError(), {"number": "A"}])
        self.assertEqual(fetch_request(send, "A"), {"number": "A"})
        self.assertEqual(send.call_args_list, [call("GET", "/requests/A")] * 2)

    def test_submit_does_not_resend_after_timeout(self):
        send = Mock(side_effect=TimeoutError())
        payload = {"title": "장갑"}
        with self.assertRaises(TimeoutError):
            submit_request(send, payload)
        send.assert_called_once_with("POST", "/requests", payload)
