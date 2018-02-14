from . import PROTOCOL, HOST, VERSION
import requests
from urllib.parse import urlencode


class BitfinexPublicAPIClient:
    """
    Un-authenticated API client for Bitfinex
    """

    def __init__(self):
        self.URL = "{0:s}://{1:s}/{2:s}".format(PROTOCOL, HOST, VERSION)

    def symbols(self):
        """
        A list of symbol names.
        :return: [
                  "btcusd",
                  "ltcusd",
                  "ltcbtc",
                  ...
                ]
        """
        r = requests.get(self.URL + "/symbols")
        return r.json()

    def symbols_details(self):
        """
        Get a list of valid symbol IDs and the pair details.
        :return:
            pair	[string]	The pair code
            price_precision	[integer]	Maximum number of significant digits for price in this pair
            initial_margin	[decimal]	Initial margin required to open a position in this pair
            minimum_margin	[decimal]	Minimal margin to maintain (in %)
            maximum_order_size	[decimal]	Maximum order size of the pair
            minimum_order_size	[decimal]	Minimum order size of the pair
            expiration	[string]	Expiration date for limited contracts/pairs
            margin	[boolean]	margin trading enabled for this pair
        """
        r = requests.get(self.URL + "/symbols_details")
        return r.json()

    def ticker(self, pair):
        """
        Return prices & other info about the request currency pair (ticker)
        :param pair: The symbol you want information about.
        You can find the list of valid symbols by calling the /symbols endpoint.
        :return:
            mid	[price]	(bid + ask) / 2
            bid	[price]	Innermost bid
            ask	[price]	Innermost ask
            last_price	[price]	The price at which the last order executed
            low	[price]	Lowest trade price of the last 24 hours
            high	[price]	Highest trade price of the last 24 hours
            volume	[price]	Trading volume of the last 24 hours
            timestamp	[time]	The timestamp at which this information was valid
        """
        r = requests.get(self.URL + "/pubticker/" + pair)
        return r.json()

    def stats(self, pair):
        """
        Various statistics about the requested pair.
        :param pair: The symbol you want information about.
        You can find the list of valid symbols by calling the /symbols endpoint.
        :return:
            period	[integer]	Period covered in days
            volume	[price]	Volume
        """
        r = requests.get(self.URL + "/stats/" + pair)
        return r.json()

    def lends(self, currency, timestamp=None, limit_lends=None):
        """
        Get a list of the most recent funding data for the given currency: total amount provided and Flash Return Rate (in % by 365 days) over time.
        :param currency:
        :param timestamp: Only show data at or after this timestamp
        :param limit_lends: Default - 50, limit the amount of funding data returned. Must be >= 1
        :return:
            rate	[decimal, % by 365 days]	Average rate of total funding received at fixed rates, ie past Flash Return Rate annualized
            amount_lent	[decimal]	Total amount of open margin funding in the given currency
            amount_used	[decimal]	Total amount of open margin funding used in a margin position in the given currency
            timestamp	[time]
        """
        d = {}
        if timestamp:
            d['timestamp'] = timestamp
        if limit_lends:
            d['limit_lends'] = limit_lends

        r = requests.get(self.URL + "/lends/" + currency + urlencode(d))
        return r.json()

    def btc_ticker(self):
        return self.ticker('btcusd')
