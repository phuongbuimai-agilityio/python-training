class ConversionTypeError(Exception):
    """Exception raised when an invalid conversion type is provided.

    This exception is raised when attempting to use a conversion type that
    is not supported by the unit converter application.

    Examples:
        >>> raise ConversionTypeError(5)
        ConversionTypeError: Unsupported conversion type: '5'
        >>> raise ConversionTypeError("volume", "Unknown conversion type")
        ConversionTypeError: Unknown conversion type: 'volume'
    """

    def __init__(
        self, conversion_type: int, message="Unsupported conversion type"
    ) -> None:
        """Initialize the ConversionTypeError.

        Args:
            conversion_type (int): The invalid conversion type that caused the error
            message (str, optional): Custom error message. Defaults to "Unsupported conversion type"
        """
        self.conversion_type = conversion_type
        self.message = f"{message}: '{conversion_type}'"
        super().__init__(self.message)


class UnitError(Exception):
    """Exception raised when an invalid unit is provided.

    This exception is raised when attempting to use a unit that is not
    supported for the selected conversion type.

    Examples:
        >>> raise UnitError("yard")
        UnitError: Invalid unit provided: 'yard'
        >>> raise UnitError("feet", "Unsupported length unit")
        UnitError: Unsupported length unit: 'feet'
    """

    def __init__(self, unit: str, message="Invalid unit provided") -> None:
        """Initialize the UnitError.

        Args:
            unit (str): The invalid unit that caused the error
            message (str, optional): Custom error message. Defaults to "Invalid unit provided"
        """
        self.unit = unit
        self.message = f"{message}: '{unit}'"
        super().__init__(self.message)


class ConversionValueError(Exception):
    """Exception raised when an invalid value is provided for conversion.

    This exception is raised when the provided value cannot be converted
    to a float or is otherwise invalid for the conversion.

    Examples:
        >>> raise ConversionValueError("abc")
        ConversionValueError: Invalid value provided: 'abc'
        >>> raise ConversionValueError("-", "Not a numeric value")
        ConversionValueError: Not a numeric value: '-'
    """

    def __init__(self, value: float, message="Invalid value provided") -> None:
        """Initialize the ConversionValueError.

        Args:
            value (float): The invalid value that caused the error
            message (str, optional): Custom error message. Defaults to "Invalid value provided"
        """
        self.value = value
        self.message = f"{message}: '{value}'"
        super().__init__(self.message)
