from constants import CONVERSION_TYPES
from utils.error_handler import handle_error
from utils.errors import ConversionTypeError, UnitError, ConversionValueError
from utils.enum import ConversionType


def validate_options_input(options_input: int) -> bool:
    """Validate if the input option corresponds to a valid conversion type.

    Args:
        options_input (int): The numeric option selected by the user (1-4)

    Returns:
        bool: True if the option is valid, False otherwise

    Raises:
        ConversionTypeError: If the option doesn't match any valid conversion type.
        The error will be handled by the error handler.
    """
    try:
        ConversionType(options_input)
        return True
    except ValueError:
        handle_error(ConversionTypeError(options_input))
        return False


def validate_single_unit(option: int, unit: str) -> bool:
    """Validate if the input unit belongs to the specified conversion type option.

    Args:
        option (int): The conversion type option (1-4)
        unit (str): The unit to validate

    Returns:
        bool: True if the unit is valid for the given option, False otherwise

    Raises:
        UnitError: If the unit is not valid for the given conversion type.
        The error will be handled by the error handler.
    """
    try:
        conversion_type = CONVERSION_TYPES[option - 1]
        if unit in conversion_type["unit"]:
            return True
        handle_error(
            UnitError(unit, f"Invalid unit for {conversion_type['name']} conversion")
        )
        return False
    except IndexError:
        handle_error(ConversionTypeError(option))
        return False


def validate_value(value: int | float) -> bool:
    """Validate if the input value is a valid numeric value.

    Args:
        value (int|float): The value to validate

    Returns:
        bool: True if the value is valid, False otherwise

    Raises:
        ConversionValueError: If the value is not a valid numeric value.
        The error will be handled by the error handler.
    """
    try:
        value = float(value)
        return True
    except ValueError:
        handle_error(ConversionValueError(value))
        return False
