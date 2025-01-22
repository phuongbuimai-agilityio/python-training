import unittest
from datetime import datetime
from unittest import mock

from ..alert import Alert
from ..rule import PriceRule
from ..stock import Stock
from ..event import Event


class TestAction:
    executed = False

    def execute(self, description):
        self.executed = True


class AlertTest(unittest.TestCase):
    def test_action_is_executed_when_rule_matches(self):
        """
        Verify that an action is executed when a stock update triggers a matching rule.

        This test ensures the core functionality of the Alert system:
        1. Create a mock stock with an event system
        2. Set up a rule that matches the stock update
        3. Confirm that the associated action is executed when the rule matches

        Test Steps:
        1. Create a mock Stock object with an event system
        2. Configure the stock's update method to fire an event
        3. Create a mock exchange with the stock
        4. Create a mock PriceRule that always returns True for matches
        5. Create a mock action
        6. Connect the alert to the exchange
        7. Simulate a stock update
        8. Assert that the action is executed with the correct alert description


        Key Interactions:
        - Stock update fires an event
        - Rule matches the stock condition
        - Action is executed with the alert description

        Note:
            - Uses mock objects to simulate complex interactions
            - Verifies the entire alert notification workflow
        """
        goog = mock.MagicMock(spec=Stock)
        goog.updated = Event()
        goog.update.side_effect = lambda date, value: goog.updated.fire(self)
        exchange = {"GOOG": goog}
        rule = mock.MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = mock.MagicMock()
        alert = Alert("Test Alert", rule, action)
        alert.connect(exchange)
        exchange["GOOG"].update(datetime(2014, 2, 10), 11)
        action.execute.assert_called_with
