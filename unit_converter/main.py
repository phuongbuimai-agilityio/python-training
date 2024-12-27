# Built-in imports

from handler.input_handler import InputHandler
from utils import renderer


# Initialize
def initialize():
    """
    Display the main menu of the Unit Converter application.

    This function prints a welcome message and shows available conversion options:
    1. Length
    2. Weight
    3. Temperature
    4. Liquid
    5. Exit
    """
    print("Welcome to the Unit Converter")
    print("==============")
    renderer.render_conversion_options()
    input_handler = InputHandler()
    input_handler.get_conversion_type()
    input_handler.get_units()
    input_handler.get_value()
    print("==============")


def main():
    initialize()


if __name__ == "__main__":
    main()
