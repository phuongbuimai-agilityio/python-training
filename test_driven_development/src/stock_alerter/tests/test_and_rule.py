import unittest
import datetime
from stock_alerter.stock import Stock


class AndRuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        goog = Stock("GOOG")
        goog.update(datetime(2014, 2, 10), 8)
        goog.update(datetime(2014, 2, 11), 10)
        goog.update(datetime(2014, 2, 12), 12)
        msft = Stock("MSFT")
        msft.update(datetime(2014, 2, 10), 10)
        msft.update(datetime(2014, 2, 11), 10)
        msft.update(datetime(2014, 2, 12), 12)
        redhat = Stock("RHT")
        redhat.update(datetime(2014, 2, 10), 7)
        cls.exchange = {"GOOG": goog, "MSFT": msft, "RHT": redhat}
