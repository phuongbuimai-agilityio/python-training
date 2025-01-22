from .rule import PriceRule


class Alert:
    """Maps a Rule to an Action, and triggers the action if the rule matches on any stock update"""

    def __init__(self, description: str, rule: PriceRule, action: callable) -> None:
        self.description = description
        self.rule = rule
        self.action = action

    def connect(self, exchange: dict) -> None:
        """Connects the alert to the given exchange.

        Args:
            exchange (dict): The exchange to connect to.
        """
        self.exchange = exchange
        dependent_stocks = self.rule.depends_on()
        for stock in dependent_stocks:
            exchange[stock].updated.connect(self.check_rule)

    def check_rule(self) -> None:
        """
        Checks if the current exchange matches the defined rule and executes the associated action.

        This method performs two key operations:
        1. Checks if the current exchange matches the predefined rule using the `matches` method.
        2. If the rule matches, executes the associated action with the provided description.
        """
        if self.rule.matches(self.exchange):
            self.action.execute(self.description)
