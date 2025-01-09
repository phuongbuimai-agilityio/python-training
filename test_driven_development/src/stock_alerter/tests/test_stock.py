import datetime
import unittest

from ..stock import Stock


class StockTest(unittest.TestCase):
    def setUp(self) -> None:
        self.goog = Stock("GOOG")

    def test_price_of_a_new_stock_class_should_be_None(self):
        """
        Test that a newly created Stock instance has its price attribute set to None.

        This test verifies the initial state of a Stock object when it is first instantiated.
        Ensures that when a Stock is created with only a stock symbol, its price is not
        automatically assigned a default value, but remains None until explicitly set.

        Args:
            self: The test case instance.

        Asserts:
            The price attribute of a new Stock object is None.
        """
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        """An update should set the price on the stock object
        We will be using the `datetime` module for the timestamp
        """
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        """Test that updating a Stock with a negative price raises a ValueError"""
        """
        # Option 1:
        try:
            self.goog.update(datetime(2014, 2, 13), -1)
        except ValueError:
            return
        self.fail("ValueError was not raised")"""
        """
        # Option 2:
        self.assertRaises(ValueError, self.goog.update, datetime(2014, 2, 13), -1)"""

        with self.assertRaises(ValueError):
            self.goog.update(datetime(2014, 2, 13), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2014, 2, 13), price=10)
        self.goog.update(datetime(2014, 2, 14), price=8.4)
        # The delta is 0.0001, which means that the test will pass
        # if the price between 8.3999 and 8.4001
        self.assertAlmostEqual(8.4, self.goog.price, delta=0.0001)


class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock("GOOG")

    def given_a_series_of_prices(self, prices):
        timestamps = [
            datetime(2014, 2, 12),
            datetime(2014, 2, 13),
            datetime(2014, 2, 14),
        ]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_true_if_price_increase_for_3_updates(self):
        self.given_a_series_of_prices([10, 11, 12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_descreases(self):
        self.given_a_series_of_prices([8, 12, 10])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices([8, 10, 10])
        self.assertFalse(self.goog.is_increasing_trend())
