from utils.errors import ConversionTypeError, UnitError, ConversionValueError


def handle_error(error: Exception) -> None:
    """Handle various exceptions by displaying appropriate error messages.

    This function provides user-friendly error messages for known exception types
    in the unit converter application. For unknown exceptions, it displays a
    generic error message.

    Args:
        error (Exception): The exception to handle. Can be one of:
            - ConversionTypeError: For invalid conversion type selections
            - UnitError: For invalid unit inputs
            - ConversionValueError: For invalid numeric values
            - Any other Exception: Handled as an unexpected error

    Examples:
        >>> handle_error(ConversionTypeError(5))
        Conversion Type Error: Unsupported conversion type: '5'
        Please select a valid conversion type.

        >>> handle_error(ConversionValueError("abc"))
        Conversion Value Error: Invalid value provided: 'abc'
        Please enter a valid value.
    """
    if isinstance(error, ConversionTypeError):
        print(f"Conversion Type Error: {error}")
        print("Please select a valid conversion type.")
    elif isinstance(error, UnitError):
        print(f"Unit Error: {error}")
        print("Please enter valid unit.")
    elif isinstance(error, ConversionValueError):
        print(f"Conversion Value Error: {error}")
        print("Please enter a valid value.")
    else:
        print(f"An unexpected error occurred: {error}")


def handle_io_error(error: Exception, operation: str) -> None:
    """Handles IOError exceptions and prints an informative message.

    Args:
        error (Exception): The IOError to handle
        operation (str): The operation that caused the error
    """
    print(f"Error during {operation} conversion history: {error}")
