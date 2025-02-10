import unittest
from unittest.mock import patch
from handler.input_handler import InputHandler
from constants import CONVERSION_TYPES


class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()

    @patch("builtins.input", side_effect=["e"])
    def test_get_options_input_exit(self, mock_input):
        """Test the exit behavior of get_options_input."""
        # Action
        self.input_handler.get_options_input()

        # Assert
        mock_input.assert_called_once()

    @patch("builtins.input", side_effect=["1"])
    @patch("handler.input_handler.validate_options_input", return_value=True)
    def test_get_valid_options_input(self, mock_validate_options_input, mock_input):
        """Test getting a valid conversion type option"""
        # Action
        result = self.input_handler.get_options_input()

        # Assert
        self.assertEqual(result, 1)
        mock_validate_options_input.assert_called_once()

    # TODO: Through the ValueError when the input is invalid, need to update logic in get_options_input
    # @patch("builtins.input", side_effect=["abc", "1"])
    # @patch("handler.input_handler.validate_options_input", side_effect=[False, True])
    # def test_get_invalid_options_input(self, mock_validate_options_input, mock_input):
    #     """Test getting an invalid conversion type option"""
    #     result = self.input_handler.get_options_input()
    #     self.assertEqual(result, 1)

    #     # Ensure input() was called two times due to one invalid inputs
    #     self.assertEqual(mock_input.call_count, 2)
    #     # Ensure validate_options_input() was called two times as well
    #     self.assertEqual(mock_validate_options_input.call_count, 2)

    @patch("builtins.input", side_effect=["meters"])
    @patch("handler.input_handler.validate_single_unit", return_value=True)
    def test_get_valid_unit_input(self, mock_validate_single_unit, mock_input):
        """Test getting a valid unit for a conversion type"""
        # Arrange
        conversion_option = CONVERSION_TYPES[0]["option"]

        # Action
        result = self.input_handler.get_unit("source", conversion_option)

        # Assert
        self.assertEqual(result, "meters")
        mock_validate_single_unit.assert_called_once()

    @patch("builtins.input", side_effect=["abc", "meters"])
    @patch("handler.input_handler.validate_single_unit", side_effect=[False, True])
    def test_get_invalid_unit_input(self, mock_validate_single_unit, mock_input):
        """Test getting an invalid unit for a conversion type"""
        # Arrange
        conversion_option = CONVERSION_TYPES[0]["option"]

        # Action
        result = self.input_handler.get_unit("source", conversion_option)

        # Assert
        self.assertEqual(result, "meters")
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_validate_single_unit.call_count, 2)

    @patch("builtins.input", side_effect=["10.5"])
    @patch("handler.input_handler.validate_value", return_value=True)
    def test_get_valid_value_input(self, mock_validate_value, mock_input):
        """Test getting a valid value for a conversion type"""
        # Action
        result = self.input_handler.get_value()

        # Assert
        self.assertEqual(result, 10.5)
        mock_input.assert_called_once()
        mock_validate_value.assert_called_once()

    @patch("builtins.input", side_effect=["abc", "10.5"])
    @patch("handler.input_handler.validate_value", side_effect=[False, True])
    def test_get_invalid_value_input(self, mock_validate_value, mock_input):
        """Test getting an invalid value for a conversion type"""
        # Action
        result = self.input_handler.get_value()

        # Assert
        self.assertEqual(result, 10.5)
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_validate_value.call_count, 2)

    @patch("builtins.input", side_effect=["y", "n"])
    def test_ask_save_to_history_with_valid_input(self, mock_input):
        # Action
        result = self.input_handler.ask_save_to_history()
        # Assert
        self.assertIn(result, ["y", "n"])
        mock_input.assert_called()

    @patch("builtins.input", side_effect=["a", "y"])
    def test_ask_save_to_history_with_invalid_input(self, mock_input):
        # Action
        result = self.input_handler.ask_save_to_history()
        # Assert
        self.assertIn(result, ["y", "n"])
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["y", "n"])
    def test_ask_view_history_with_valid_input(self, mock_input):
        # Action
        result = self.input_handler.ask_view_history()
        # Assert
        self.assertIn(result, ["y", "n"])
        mock_input.assert_called()
