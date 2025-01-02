from .base import BaseConverter


class TemperatureConverter(BaseConverter):
    """Converter for temperature units (Celsius and Fahrenheit)."""

    def __init__(self) -> None:
        """Initialize the temperature converter."""
        super().__init__("temperature")
