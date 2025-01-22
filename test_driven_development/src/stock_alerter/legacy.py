from datetime import datetime

from .stock import Stock
from .rule import PriceRule


class AlertProcessor:
    def __init__(self, autorun=True, exchange=None):
        """
        Initialize the AlertProcessor for monitoring stock price rules.

        This method sets up an exchange of stocks and configures predefined price
        rules for monitoring stock price changes. It provides flexibility in
        initializing the exchange and controlling the automatic execution of alerts.

        Args:
            autorun (bool, optional):
                Determines whether the alert processor should automatically start
                processing alerts upon initialization.
                - If True (default), calls self.run() immediately after setup
                - If False, allows manual control of alert processing
                Defaults to True.

            exchange (dict, optional):
                A custom dictionary of stock symbols and Stock objects.
                - If provided, uses the custom exchange
                - If None (default), creates a default exchange with 'GOOG' and 'AAPL' stocks
                Defaults to None.

        Default Exchange Setup:
            - Creates Stock instances for 'GOOG' and 'AAPL'
            - Sets up price rules:
                * GOOG: Alert when price > $10
                * AAPL: Alert when price > $5
            - Connects stock update events to print_action method

        Examples:
            >>> # Default initialization with automatic running
            >>> processor = AlertProcessor()

            >>> # Custom exchange with manual control
            >>> custom_exchange = {'MSFT': Stock('MSFT')}
            >>> processor = AlertProcessor(autorun=False, exchange=custom_exchange)
            >>> processor.run()  # Manually start processing

        Note:
            - Automatically connects stock update events to alert rules
            - Supports both automatic and manual alert processing modes
        """
        self.exchange = (
            exchange if exchange else {"GOOG": Stock("GOOG"), "AAPL": Stock("AAPL")}
        )
        rule_1 = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_2 = PriceRule("AAPL", lambda stock: stock.price > 5)
        self.exchange["GOOG"].updated.connect(
            lambda stock: self.print_action(stock, rule_1)
        )
        self.exchange["AAPL"].updated.connect(
            lambda stock: self.print_action(stock, rule_2)
        )

        if autorun:
            self.run()

    def run(self) -> None:
        """Run the alert processor."""
        updates = self.parse_file()
        self.do_updates(updates)

    def do_updates(self, updates: list) -> None:
        """Process a list of stock updates.

        Args:
            updates (list): A list of stock updates in the format (symbol, timestamp, price).
        """
        for symbol, timestamp, price in updates:
            stock = self.exchange[symbol]
            stock.update(timestamp, price)

    def parse_file(self) -> list:
        """
        Parse the updates.csv file and return a list of stock updates.

        Returns:
            list: A list of stock updates in the format (symbol, timestamp, price).
        """
        updates = []
        with open("updates.csv", "r") as fp:
            for line in fp.readlines():
                symbol, timestamp, price = line.strip().split(",")
                updates.append(
                    (
                        symbol,
                        datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f"),
                        int(price),
                    )
                )
        return updates

    def print_action(self, stock: Stock, rule: PriceRule):
        """
        Print the stock symbol and price if the rule matches.

        Args:
            stock (Stock): The stock object.
            rule (PriceRule): The price rule.

        Returns:
            None
        """
        print(stock.symbol, stock.price) if rule.matches(self.exchange) else None
