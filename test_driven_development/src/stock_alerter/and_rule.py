class AndRule:
    def __init__(self, *args):
        self.rules = args

    def matches(self, exchange):
        return all([rule.matches(exchange) for rule in self.rules])
