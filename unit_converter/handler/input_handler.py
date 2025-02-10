from constants import EXIT_OPTIONS
from utils import validate_options_input, validate_single_unit, validate_value


class InputHandler:
    def __init__(self) -> None:
        self.options = None
        self.source_unit = None
        self.target_unit = None
        self.value = None

    def get_options_input(self) -> int:
        """Get and validate user input for conversion type options.

        Prompts the user to enter a conversion type option. Handles two types of inputs:
        1. Exit commands ('e' or 'exit') which terminate the program
        2. Numeric options that correspond to conversion types

        The method will recursively prompt for input if validation fails.

        Returns:
            int: A validated conversion type option representing the user's selection.
        """
        options_input: str = input("Enter the conversion type: ").strip()

        if options_input in EXIT_OPTIONS:
            print("Thank you for using the Unit Converter. Goodbye!")
            return None

        corresponding_options: int = int(options_input)
        if validate_options_input(corresponding_options):
            self.options = corresponding_options
        else:
            self.get_options_input()

        return self.options

    def get_unit(self, unit_type: str, conversion_option: int) -> str:
        """Get and validate a single unit input.

        Args:
            unit_type (str): Type of unit to get ('source' or 'target')
            conversion_option (int): The conversion type option

        Returns:
            str: The validated unit input
        """
        unit = input(f"Enter the {unit_type} unit: ").strip().lower()
        if not validate_single_unit(conversion_option, unit):
            return self.get_unit(unit_type, conversion_option)
        return unit

    def get_value(self) -> float:
        """Get and validate the numeric value to convert.

        Returns:
            float: The validated numeric value
        """
        while True:
            value = input("Enter the value to convert: ").strip()
            if validate_value(value):
                try:
                    self.value = float(value)  # Set self.value if required
                    return self.value
                except ValueError:
                    print("Error: Please enter a valid numeric value.")
            else:
                print("Invalid input. Please try again.")

    def ask_save_to_history(self) -> str:
        """Asks the user if they want to save the conversion to history.

        Returns:
            str: The user's choice, either 'y' (yes) or 'n' (no).
                Will continue to prompt until a valid input is received.
        """
        option = (
            input("Do you want to save this conversion to history? (y/n): ")
            .strip()
            .lower()
        )
        if option not in ["y", "n"]:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.ask_save_to_history()
        return option

    def ask_view_history(self) -> str:
        """Asks the user if they want to view their conversion history.

        Returns:
            str: The user's choice, either 'y' (yes) or 'n' (no).
                Will continue to prompt until a valid input is received.
        """
        option = (
            input("Do you want to view your conversion history? (y/n): ")
            .strip()
            .lower()
        )
        if option not in ["y", "n"]:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.ask_view_history()
        return option
