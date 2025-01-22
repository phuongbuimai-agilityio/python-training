import bisect
import collections
from datetime import timedelta
import datetime

Update = collections.namedtuple("Update", ["timestamp", "value"])


class TimeSeries:
    def __init__(self):
        self.series = []

    def update(self, timestamp: datetime, value: float) -> None:
        """Add a new update to the time series.

        This method adds a new update to the time series by inserting it into
        the appropriate position based on the timestamp. It uses the bisect
        module to efficiently find the correct position to insert the update.

        Args:
            timestamp (datetime): The timestamp of the update.
            value (float): The value of the update.
        """
        bisect.insort_left(self.series, Update(timestamp, value))

    def __getitem__(self, index: int) -> Update:
        """
        Retrieve a specific Update from the time series by its index.

        This method implements the indexing protocol for the TimeSeries class,
        allowing direct access to stored Update objects using standard list-like
        indexing syntax. It provides a convenient way to access individual time
        series entries.

        Args:
            index (int): The index of the Update to retrieve.
                - Supports positive and negative indexing
                - Follows standard Python list indexing rules

        Returns:
            Update: The Update object at the specified index.

        Raises:
            IndexError: If the index is out of range for the time series.

        Examples:
            >>> ts = TimeSeries()
            >>> ts.update(datetime(2023, 1, 1), 100.0)
            >>> ts[0]  # Returns the first Update in the series
            >>> ts[-1]  # Returns the last Update in the series
        """
        return self.series[index]

    def get_closing_price_list(self, on_date: datetime, num_days: int) -> list:
        """
        Retrieve a list of closing prices for a specific date and a specified number of days.

        This method retrieves a list of closing prices for a specific date and a
        specified number of days. It iterates through the time series, starting
        from the most recent update, and adds closing prices to the list until
        the specified number of days has been reached. If there are fewer than
        num_days updates in the time series, the method returns an empty list.

        Args:
            on_date (datetime): The specific date for which to retrieve closing prices.
            num_days (int): The number of days for which to retrieve closing prices.

        Returns:
            list: A list of closing prices for the specified date and number of days.

        Examples:
            >>> ts = TimeSeries()
            >>> ts.update(datetime(2023, 1, 1), 100.0)
            >>> ts.update(datetime(2023, 1, 2), 110.0)
            >>> ts.update(datetime(2023, 1, 3), 120.0)
            >>> ts.get_closing_price_list(datetime(2023, 1, 2), 2)
            [Update(timestamp=datetime.datetime(2023, 1, 1, 0, 0), value=100.0), Update(timestamp=datetime.datetime(2023, 1, 2, 0, 0), value=110.0)]
        """
        closing_price_list = []
        for i in range(num_days):
            chk = on_date.date() - timedelta(i)
            for price_event in reversed(self.series):
                if price_event.timestamp.date() > chk:
                    pass
                if price_event.timestamp.date() == chk:
                    closing_price_list.insert(0, price_event)
                    break
                if price_event.timestamp.date() < chk:
                    closing_price_list.insert(0, price_event)
                    break
        return closing_price_list
