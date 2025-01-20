from .timeseries import TimeSeries
from .stock_signal_enum import StockSignal


class Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5

    def __init__(self, symbol):
        self.symbol = symbol
        self.history = TimeSeries()

    def update(self, timestamp, price):
        """
        Update the price of the stock at a given timestamp

        >>> from datetime import datetime
        >>> stock = Stock("GOOG")
        >>> stock.update(datetime(2011, 10, 3), 10)
        >>> stock.price
        10

        The method will raise a ValueError exception if the price is negative

        >>> stock.update(datetime(2011, 10, 3), -1)
        Traceback (most recent call last):
            ...
        ValueError: Price must be positive
        """
        if price < 0:
            raise ValueError("Price must be positive")
        self.history.update(timestamp, price)
        self.updated.fire(self)

    @property
    def price(self):
        """Returns the current price of the Stock
        >>> from datetime import datetime
        >>> stock = Stock("GOOG")
        >>> stock.update(datetime(2011, 10, 3), 10)
        >>> stock.price
        10
        The method will return the latest price by timestamp, so even
        if updates are out of order, it will return the latest one
        >>> stock = Stock("GOOG")
        >>> stock.update(datetime(2011, 10, 3), 10)
        Now, let us do an update with a date that is earlier than the
        previous one
        >>> stock.update(datetime(2011, 10, 2), 5)
        And the method still returns the latest price
        >>> stock.price
        10
        If there are no updates, then the method returns None
        >>> stock = Stock("GOOG")
        >>> print(stock.price)
        None
        """
        try:
            return self.history[-1].value
        except IndexError:
            return None

    def is_increasing_trend(self):
        """Returns True if the past three values have been strictly
        increasing
        Returns False if there have been less than three updates
        so far
        >>> stock = Stock("GOOG")
        >>> stock.is_increasing_trend()
        False
        """
        try:
            return (
                self.history[-3].value < self.history[-2].value < self.history[-1].value
            )
        except IndexError:
            return False

    def _is_short_term_crossover_below_to_above(
        self, prev_short_term_ma, prev_long_term_ma, short_term_ma, long_term_ma
    ):
        return prev_long_term_ma > prev_short_term_ma and long_term_ma < short_term_ma

    def _is_short_term_crossover_above_to_below(
        self, prev_short_term_ma, prev_long_term_ma, short_term_ma, long_term_ma
    ):
        return prev_long_term_ma < prev_short_term_ma and long_term_ma > short_term_ma

    def get_crossover_signal(self, on_date):
        NUM_DAYS = self.LONG_TERM_TIMESPAN + 1
        closing_price_list = self.history.get_closing_price_list(on_date, NUM_DAYS)

        # Return Neutral signal if there is no crossover
        if len(closing_price_list) < NUM_DAYS:
            return StockSignal.neutral

        long_term_series = closing_price_list[-self.LONG_TERM_TIMESPAN :]
        prev_long_term_series = closing_price_list[-self.LONG_TERM_TIMESPAN - 1 : -1]
        short_term_series = closing_price_list[-self.SHORT_TERM_TIMESPAN :]
        prev_short_term_series = closing_price_list[-self.SHORT_TERM_TIMESPAN - 1 : -1]

        long_term_ma = (
            sum([update.value for update in long_term_series]) / self.LONG_TERM_TIMESPAN
        )
        prev_long_term_ma = (
            sum([update.value for update in prev_long_term_series])
            / self.LONG_TERM_TIMESPAN
        )
        short_term_ma = (
            sum([update.value for update in short_term_series])
            / self.SHORT_TERM_TIMESPAN
        )
        prev_short_term_ma = (
            sum([update.value for update in prev_short_term_series])
            / self.SHORT_TERM_TIMESPAN
        )

        # Check if there is a Buy Signal
        if self._is_short_term_crossover_below_to_above(
            prev_short_term_ma, prev_long_term_ma, short_term_ma, long_term_ma
        ):
            return StockSignal.buy

        # Check if there is a Sell Signal
        if self._is_long_term_crossover_above_to_below(
            prev_short_term_ma, prev_long_term_ma, short_term_ma, long_term_ma
        ):
            return StockSignal.sell

        # Return Neutral signal
        return StockSignal.neutral
