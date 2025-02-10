import unittest
from unittest.mock import patch, Mock, call
from main import show_menu, get_conversion_input, perform_conversion, handle_history
from handler.input_handler import InputHandler
from converters.factory import ConverterFactory
from utils.history_manager import HistoryManager


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_input_handler = Mock(spec=InputHandler)
        self.mock_history_manager = Mock(spec=HistoryManager)
        self.mock_converter_factory = Mock(spec=ConverterFactory)


class TestShowMenu(BaseTestCase):
    @patch("main.renderer.render_conversion_options")
    def test_show_menu_valid_input(self, mock_render):
        """
        Test show_menu function with a valid input option.

        Test follows the Arrange-Act-Assert pattern:
        - Arrange: Set up the test input and mock objects
        - Action: Call the method being tested
        - Assert: Verify the expected outcomes
        """
        # Arrange
        self.mock_input_handler.get_options_input.return_value = (
            2  # Example: Weight conversion
        )

        # Action
        result = show_menu(self.mock_input_handler)

        # Assert
        mock_render.assert_called_once()
        self.mock_input_handler.get_options_input.assert_called_once()
        self.assertEqual(result, 2)


class TestGetConversionInput(BaseTestCase):
    @patch("main.renderer.render_unit_by_conversion_type")
    def test_get_conversion_input_length_conversion(self, mock_render):
        """
        Test get_conversion_input for length conversion with mocked inputs.
        """
        # Arrange
        self.mock_input_handler.get_unit.side_effect = ["meters", "kilometers"]
        self.mock_input_handler.get_value.return_value = 10.5

        # Action
        result = get_conversion_input(1, self.mock_input_handler)

        # Assert
        mock_render.assert_called_once_with(1)
        self.mock_input_handler.get_unit.assert_has_calls(
            [call("source", 1), call("target", 1)]
        )
        self.mock_input_handler.get_value.assert_called_once()
        self.assertEqual(result, ("meters", "kilometers", 10.5))


class TestPerformConversion(BaseTestCase):
    @patch("main.renderer.render_result")
    @patch("main.ConverterFactory.create_converter")
    def test_perform_conversion_length_conversion(
        self, mock_create_converter, mock_render
    ):
        """
        Test perform_conversion for length conversion with mocked inputs.
        """
        # Arrange
        mock_converter = Mock()
        mock_converter.convert.return_value = 0.01  # 10 meters = 0.01 kilometers
        mock_create_converter.return_value = mock_converter

        # Action
        result = perform_conversion(1, "meters", "kilometers", 10)

        # Assert
        mock_create_converter.assert_called_once_with(1)
        mock_converter.convert.assert_called_once_with("meters", "kilometers", 10)
        mock_render.assert_called_once_with(10, "meters", "kilometers", 0.01)
        self.assertEqual(result, 0.01)


class TestHandleHistory(BaseTestCase):
    @patch("main.get_conversion_type_name")
    def test_handle_history_save_and_view(self, mock_get_conversion_type_name):
        """
        Test handle_history when user chooses to save and view history.
        """
        # Arrange
        conversion_option = 1  # Length conversion
        source_unit = "meters"
        target_unit = "kilometers"
        value = 10.0
        result = 0.01

        self.mock_input_handler.ask_save_to_history.return_value = "y"
        self.mock_input_handler.ask_view_history.return_value = "y"

        params = {
            "option": conversion_option,
            "source_unit": source_unit,
            "target_unit": target_unit,
            "value": value,
            "result": result,
            "input_handler": self.mock_input_handler,
            "history_manager": self.mock_history_manager,
        }
        # Action
        handle_history(params)

        # Assert
        formatted_conversion_option = mock_get_conversion_type_name(conversion_option)
        self.mock_history_manager.save_to_history.assert_called_once_with(
            formatted_conversion_option, source_unit, target_unit, value, result
        )
        self.mock_history_manager.display_history.assert_called_once()

    @patch("main.get_conversion_type_name")
    def test_handle_history_save_and_not_view(self, mock_get_conversion_type_name):
        """
        Test handle_history when user saves but does not view history
        """
        # Arrange
        conversion_option = 1  # Length conversion
        source_unit = "meters"
        target_unit = "kilometers"
        value = 10.0
        result = 0.01

        self.mock_input_handler.ask_save_to_history.return_value = "y"
        self.mock_input_handler.ask_view_history.return_value = "n"

        params = {
            "option": conversion_option,
            "source_unit": source_unit,
            "target_unit": target_unit,
            "value": value,
            "result": result,
            "input_handler": self.mock_input_handler,
            "history_manager": self.mock_history_manager,
        }

        # Action
        handle_history(params)

        # Assert
        formatted_conversion_option = mock_get_conversion_type_name(conversion_option)
        self.mock_history_manager.save_to_history.assert_called_once_with(
            formatted_conversion_option, source_unit, target_unit, value, result
        )
        self.mock_history_manager.display_history.assert_not_called()

    @patch("main.get_conversion_type_name")
    def test_handle_history_do_not_save_and_not_view(
        self, mock_get_conversion_type_name
    ):
        """
        Test handle_history when user chooses not to save history
        """
        # Arrange
        conversion_option = 2  # Weight conversion
        source_unit = "grams"
        target_unit = "kilograms"
        value = 10.0
        result = 0.01

        self.mock_input_handler.ask_save_to_history.return_value = "n"
        self.mock_input_handler.ask_view_history.return_value = "n"

        params = {
            "option": conversion_option,
            "source_unit": source_unit,
            "target_unit": target_unit,
            "value": value,
            "result": result,
            "input_handler": self.mock_input_handler,
            "history_manager": self.mock_history_manager,
        }
        # Action
        handle_history(params)

        # Assert
        self.mock_history_manager.save_to_history.assert_not_called()
        self.mock_history_manager.display_history.assert_not_called()
