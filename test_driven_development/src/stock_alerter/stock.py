import unittest


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("Price must be positive")
        self.price_history.append(price)

    @property
    def price(self):
        return self.price_history[-1] if self.price_history else None

    def is_increasing_trend(self):
        """Checks if the stock price has increased in the last 3 updates"""
        return self.price_history[-3] < self.price_history[-2] < self.price_history[-1]


if __name__ == "__main__":
    unittest.main()
