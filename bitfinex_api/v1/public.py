from . import PROTOCOL, HOST, VERSION
import requests
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

    def btc_ticker(self):
        return self.ticker('btcusd')
