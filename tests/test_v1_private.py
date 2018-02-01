#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `bitfinex_api` package - private api, v1 """

import unittest
import os
from bitfinex_api.v1.private import BitfinexPrivateAPIClient


class TestPrivatev1(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        if "BITFINEX_API_KEY" not in os.environ or "BITFINEX_API_SECRET" not in os.environ:
            self.skipTest('"BITFINEX_API_KEY" and "BITFINEX_API_SECRET" must be in your env for this test!')
        else:
            self.client = BitfinexPrivateAPIClient(os.environ['BITFINEX_API_KEY'], os.environ['BITFINEX_API_SECRET'])

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_post_request(self):
        """Test something."""
        payload = {
            "request": "/v1/account_infos",
            "nonce": self.client._nonce,

        }
        json_resp = self.client.post_request("/account_infos", payload)
        self.assertEqual(type(json_resp), list)
