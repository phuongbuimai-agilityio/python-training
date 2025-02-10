import unittest
from unittest.mock import patch

from converters.base import BaseConverter


class TestBaseConverter(unittest.TestCase):
    def setUp(self):
        self.converter = BaseConverter("length")
        # Mock the BaseConverter with a sample configuration
        self.mock_rates = {
            "length": {"meters": {"kilometers": 0.001}, "kilometers": {"meters": 1000}},
            "temperature": {"celsius": {"fahrenheit": {"formula": "value * 9/5 + 32"}}},
        }

    def test_convert_same_unit(self):
        """Test conversion when source and target units are the same"""
        # Action
        result = self.converter.convert("meters", "meters", 10)
        # Assert
        self.assertEqual(result, 10)

    def test_convert_simple_rate(self):
        """Test conversion with a simple conversion rate"""
        # Action
        result = self.converter.convert("meters", "kilometers", 1000)
        # Assert
        self.assertEqual(result, 1.0)

    def test_convert_temperature_formula(self):
        """Test conversion using a complex formula (temperature)."""
        # Temporarily patch the BaseConverter to use temperature rates
        with patch.object(self.converter, "rates", self.mock_rates["temperature"]):
            # Action
            result = self.converter.convert("celsius", "fahrenheit", 0)
            # Assert
            self.assertEqual(result, 32.0)
