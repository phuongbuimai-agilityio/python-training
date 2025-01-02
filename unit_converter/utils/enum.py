from enum import Enum


class ConversionType(Enum):
    """Enumeration of supported unit conversion types.

    This enum defines the available types of unit conversions in the application.
    Each type corresponds to a specific category of measurements that can be
    converted between different units.

    Attributes:
        LENGTH (1): Length conversions (e.g., meters to kilometers)
        WEIGHT (2): Weight conversions (e.g., kilograms to grams)
        TEMPERATURE (3): Temperature conversions (e.g., celsius to fahrenheit)
        LIQUID (4): Liquid volume conversions (e.g., liters to milliliters)

    Usage:
        >>> conversion_type = ConversionType.LENGTH
        >>> conversion_type.value
        1
        >>> ConversionType(1)
        ConversionType.LENGTH
    """

    LENGTH = 1
    WEIGHT = 2
    TEMPERATURE = 3
    LIQUID = 4


def get_conversion_type_name(conversion_type: int) -> str:
    """Get the name of a conversion type based on its value.

    Args:
        conversion_type (int): The value of the conversion type

    Returns:
        str: The name of the conversion type
    """
    return ConversionType(conversion_type).name
