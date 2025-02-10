# Built-in imports
import utils.renderer as renderer
from handler.input_handler import InputHandler
from converters.factory import ConverterFactory
from utils.history_manager import HistoryManager
from utils.enum import get_conversion_type_name


# Initialize
def initialize() -> None:
    """
    Initialize and run the main workflow of the Unit Converter application.

    This function orchestrates the entire unit conversion process by:
    1. Displaying a welcome message
    2. Creating instances of InputHandler and HistoryManager
    3. Showing the main menu and getting user's conversion option
    4. Collecting user inputs for source unit, target unit, and value
    5. Performing the requested unit conversion
    6. Saving the conversion to history
    7. Handling potential keyboard interrupts gracefully

    The function supports conversions in the following categories:
    - Length
    - Weight
    - Temperature
    - Liquid Volume

    Raises:
        KeyboardInterrupt: If the user terminates the application (e.g., Ctrl+C)
    """
    print("==============")
    print("Welcome to the Unit Converter")
    print("==============")
    try:
        input_handler = InputHandler()
        history_manager = HistoryManager()

        # Display the main menu and get user selection
        option = show_menu(input_handler)

        # Get user inputs for source unit, target unit, and value
        source_unit, target_unit, value = get_conversion_input(option, input_handler)

        # Perform conversion
        result = perform_conversion(option, source_unit, target_unit, value)

        # Handle history
        params = {
            "option": option,
            "source_unit": source_unit,
            "target_unit": target_unit,
            "value": value,
            "result": result,
            "input_handler": input_handler,
            "history_manager": history_manager,
        }
        handle_history(params)
        print("Thank you for using the Unit Converter!")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return


def show_menu(input_handler: InputHandler) -> int:
    """
    Display the conversion options menu and retrieve the user's selected conversion option.

    Args:
        input_handler (InputHandler): An instance of InputHandler used to
                                      manage and validate user input.

    Returns:
        int: The numeric option representing the user's selected conversion type
             (e.g., 1 for Length, 2 for Weight, etc.).
    """
    renderer.render_conversion_options()
    conversion_option = input_handler.get_options_input()
    return conversion_option


def get_conversion_input(
    conversion_option: int, input_handler: InputHandler
) -> tuple[str, str, float]:
    """
    Collect user inputs for unit conversion: source unit, target unit, and conversion value.

    Args:
        conversion_option (int): The type of conversion selected by the user
                                 (e.g., 1 for Length, 2 for Weight).
        input_handler (InputHandler): An instance of InputHandler used to
                                      manage and validate user input.

    Returns:
        tuple[str, str, float]: A tuple containing:
            - source_unit (str): The unit to convert from
            - target_unit (str): The unit to convert to
            - value (float): The numeric value to be converted

    Example:
        For a length conversion, might return ('meters', 'kilometers', 10.5)
    """
    # Display available units
    renderer.render_unit_by_conversion_type(conversion_option)
    source_unit: str = input_handler.get_unit("source", conversion_option)
    target_unit: str = input_handler.get_unit("target", conversion_option)

    # Get the value and convert
    value = input_handler.get_value()

    return source_unit, target_unit, value


def perform_conversion(
    option: int, source_unit: str, target_unit: str, value: float
) -> float:
    """
    Perform a unit conversion using the appropriate converter based on the conversion type.

    This function dynamically creates a converter using the ConverterFactory,
    executes the conversion, and renders the result using the renderer.

    Args:
        option (int): The type of conversion to perform
                      (e.g., 1 for Length, 2 for Weight).
        source_unit (str): The unit to convert from.
        target_unit (str): The unit to convert to.
        value (float): The numeric value to be converted.

    Returns:
        float: The converted value after applying the unit conversion.

    Example:
        Converting 10 meters to kilometers might return 0.01
    """
    # Create appropriate converter and get result
    converter = ConverterFactory.create_converter(option)
    result = converter.convert(source_unit, target_unit, value)

    # Display result
    renderer.render_result(value, source_unit, target_unit, result)
    return result


def handle_history(params: dict) -> None:
    """
    Manage the saving and viewing of conversion history based on user preferences.

    This function provides an interactive workflow for users to:
    1. Choose whether to save the current conversion to history
    2. Optionally view the entire conversion history

    Args:
        option (int): The type of conversion performed
                      (e.g., 1 for Length, 2 for Weight).
        source_unit (str): The unit converted from.
        target_unit (str): The unit converted to.
        value (float): The original numeric value before conversion.
        result (float): The converted numeric value.
        input_handler (InputHandler): Handles user input for history-related decisions.
        history_manager (HistoryManager): Manages saving and displaying conversion history.

    Returns:
        None: The function performs actions based on user input but does not return a value.
    """
    option = params["option"]
    source_unit = params["source_unit"]
    target_unit = params["target_unit"]
    value = params["value"]
    result = params["result"]
    input_handler = params["input_handler"]
    history_manager = params["history_manager"]
    # Save to history
    save_to_history = input_handler.ask_save_to_history()
    if save_to_history == "y":
        format_conversion_option = get_conversion_type_name(option)
        history_manager.save_to_history(
            format_conversion_option, source_unit, target_unit, value, result
        )

        # View history
        view_history = input_handler.ask_view_history()
        if view_history == "y":
            history_manager.display_history()


def main():
    initialize()


if __name__ == "__main__":
    main()
