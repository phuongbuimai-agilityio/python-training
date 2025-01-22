class PriceRule:
    """PriceRule is a rule that triggers when a stock price
    satisfies a condition (usually greater, equal or lesser
    than a given value)"""

    def __init__(self, symbol: str, condition: callable) -> None:
        self.symbol = symbol
        self.condition = condition

    def matches(self, exchange: dict) -> bool:
        """Checks if the current exchange matches the defined rule.

        Args:
            exchange (dict): The current exchange data.

        Returns:
            bool: True if the rule matches, False otherwise.
        """
        try:
            stock = exchange[self.symbol]
        except KeyError:
            return False
        return self.condition(stock) if stock.price else False

    def depends_on(self) -> set:
        """
        Returns the set of stocks that this rule depends on.

        Returns:
            set: A set of stock symbols that this rule depends on.
        """
        return {self.symbol}


class AndRule:
    def __init__(self, *args):
        self.rules = args

    def matches(self, exchange: dict) -> bool:
        """
        Checks if the current exchange matches the defined rule.

        Args:
            exchange (dict): The current exchange data.

        Returns:
            bool: True if the rule matches, False otherwise.
        """
        return all([rule.matches(exchange) for rule in self.rules])
