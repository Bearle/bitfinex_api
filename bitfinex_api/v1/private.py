import json
import base64
import hmac
import hashlib
import time
import requests
from . import PROTOCOL, HOST, VERSION
from .exceptions import InvalidApiKey, UnknownError


class BitfinexPrivateAPIClient:
    """
    Authenticated client for trading through Bitfinex API
    """

    def __init__(self, key, secret):
        self.URL = "{0:s}://{1:s}/{2:s}".format(PROTOCOL, HOST, VERSION)
        self.KEY = key
        self.SECRET = secret

    @property
    def _nonce(self):
        """
        Returns a nonce
        Used in authentication
        """
        return str(time.time() * 1000000)

    def _sign_payload(self, payload):
        j = json.dumps(payload)
        data = base64.standard_b64encode(j.encode('utf8'))

        h = hmac.new(self.SECRET.encode('utf8'), data, hashlib.sha384)
        signature = h.hexdigest()
        return {
            "X-BFX-APIKEY": self.KEY,
            "X-BFX-SIGNATURE": signature,
            "X-BFX-PAYLOAD": data
        }

    def post_request(self, url, payload):
        signed_payload = self._sign_payload(payload)
        r = requests.post(self.URL + url, headers=signed_payload, verify=True)
        json_resp = r.json()
        if 'message' in json_resp:
            if json_resp['message'] == InvalidApiKey.message:
                raise InvalidApiKey(json_resp['message'])
            else:
                raise UnknownError(json_resp['message'])
        return json_resp

    def place_order(self, amount, price, side, ord_type, symbol='btcusd', exchange='bitfinex'):
        """
        Submit a new order.
        :param amount:
        :param price:
        :param side:
        :param ord_type:
        :param symbol:
        :param exchange:
        :return:
        """
        payload = {
            "request": "/v1/order/new",
            "nonce": self._nonce,
            "symbol": symbol,
            "amount": amount,
            "price": price,
            "exchange": exchange,
            "side": side,
            "type": ord_type

        }
        json_resp = self.post_request("/order/new", payload)

        try:
            json_resp['order_id']
        except KeyError:
            return json_resp['message']

        return json_resp

    def delete_order(self, order_id):
        """
        Cancel an order.
        :param order_id:
        :return:
        """
        payload = {
            "request": "/v1/order/cancel",
            "nonce": self._nonce,
            "order_id": order_id
        }
        json_resp = self.post_request("/order/cancel", payload)
        try:
            json_resp['avg_execution_price']
        except KeyError:
            return json_resp['message']

        return json_resp

    def delete_all_orders(self):
        """
        Cancel all orders.

        :return:
        """
        payload = {
            "request": "/v1/order/cancel/all",
            "nonce": self._nonce,
        }
        json_resp = self.post_request("/order/cancel/all", payload)
        return json_resp

    def status_order(self, order_id):
        """
        Get the status of an order. Is it active? Was it cancelled? To what extent has it been executed? etc.
        :param order_id:
        :return:
        """
        payload = {
            "request": "/v1/order/status",
            "nonce": self._nonce,
            "order_id": order_id
        }
        json_resp = self.post_request("/order/status", payload)
        try:
            json_resp['avg_execution_price']
        except KeyError:
            return json_resp['message']

        return json_resp

    def active_orders(self):
        """
        Fetch active orders
        """

        payload = {
            "request": "/v1/orders",
            "nonce": self._nonce
        }
        json_resp = self.post_request("/orders", payload)

        return json_resp

    def active_positions(self):
        """
        Fetch active Positions
        """

        payload = {
            "request": "/v1/positions",
            "nonce": self._nonce
        }
        json_resp = self.post_request("/positions", payload)
        return json_resp

    def claim_position(self, position_id):
        """
        Claim a position.
        :param position_id:
        :return:
        """
        payload = {
            "request": "/v1/position/claim",
            "nonce": self._nonce,
            "position_id": position_id
        }
        json_resp = self.post_request("/position/claim", payload)

        return json_resp

    def past_trades(self, timestamp=0, symbol='btcusd'):
        """
        Fetch past trades
        :param timestamp:
        :param symbol:
        :return:
        """
        payload = {
            "request": "/v1/mytrades",
            "nonce": self._nonce,
            "symbol": symbol,
            "timestamp": timestamp
        }
        json_resp = self.post_request("/mytrades", payload)
        return json_resp

    def place_offer(self, currency, amount, rate, period, direction):
        """

        :param currency:
        :param amount:
        :param rate:
        :param period:
        :param direction:
        :return:
        """
        payload = {
            "request": "/v1/offer/new",
            "nonce": self._nonce,
            "currency": currency,
            "amount": amount,
            "rate": rate,
            "period": period,
            "direction": direction
        }
        json_resp = self.post_request("/offer/new", payload)
        return json_resp

    def cancel_offer(self, offer_id):
        """

        :param offer_id:
        :return:
        """
        payload = {
            "request": "/v1/offer/cancel",
            "nonce": self._nonce,
            "offer_id": offer_id
        }
        json_resp = self.post_request("/offer/cancel", payload)
        return json_resp

    def status_offer(self, offer_id):
        """

        :param offer_id:
        :return:
        """
        payload = {
            "request": "/v1/offer/status",
            "nonce": self._nonce,
            "offer_id": offer_id
        }

        json_resp = self.post_request("/offer/status", payload)

        return json_resp

    def active_offers(self):
        """
        Fetch active_offers
        :return:
        """
        payload = {
            "request": "/v1/offers",
            "nonce": self._nonce
        }

        json_resp = self.post_request("/offers", payload)

        return json_resp

    def balances(self):
        """
        Fetch balances

        :return:
        """
        payload = {
            "request": "/v1/balances",
            "nonce": self._nonce
        }

        json_resp = self.post_request("/balances", payload)
        return json_resp

    def history(self, currency, since=0, until=9999999999, limit=500, wallet='exchange'):
        """
        View you balance ledger entries
        :param currency: currency to look for
        :param since: Optional. Return only the history after this timestamp.
        :param until: Optional. Return only the history before this timestamp.
        :param limit: Optional. Limit the number of entries to return. Default is 500.
        :param wallet: Optional. Return only entries that took place in this wallet. Accepted inputs are: “trading”,
        “exchange”, “deposit”.
        """
        payload = {
            "request": "/v1/history",
            "nonce": self._nonce,
            "currency": currency,
            "since": since,
            "until": until,
            "limit": limit,
            "wallet": wallet
        }
        json_resp = self.post_request("/history", payload)
        return json_resp

    def history_movements(self, currency, method='bitcoin', since=0, until=9999999999, limit=500):
        """
        View your past deposits/withdrawals.
        :param method: The method of the deposit/withdrawal (can be “bitcoin”, “litecoin”, “darkcoin”, “wire”).
        :param currency: currency to look for
        :param since: Optional. Return only the history after this timestamp.
        :param until: Optional. Return only the history before this timestamp.
        :param limit: Optional. Limit the number of entries to return. Default is 500.
        """
        payload = {
            "request": "/v1/history/movements",
            "nonce": self._nonce,
            "currency": currency,
            "method": method,
            "since": since,
            "until": until,
            "limit": limit,
        }
        json_resp = self.post_request("/history/movements", payload)
        return json_resp
