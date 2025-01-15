from datetime import datetime

from .stock import Stock
from .rule import PriceRule


class AlertProcessor:
    def __init__(self, autorun=True, exchange=None):
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

    def run(self):
        updates = self.parse_file()
        self.do_updates(updates)

    def do_updates(self, updates):
        for symbol, timestamp, price in updates:
            stock = self.exchange[symbol]
            stock.update(timestamp, price)

    def parse_file(self) -> list:
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

    def print_action(self, stock, rule):
        print(stock.symbol, stock.price) if rule.matches(self.exchange) else None
