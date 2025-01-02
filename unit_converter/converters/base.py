import yaml
from pathlib import Path


class BaseConverter:
    """Base class for all unit converters."""

    def __init__(self, converter_type: str) -> None:
        """Initialize a converter with conversion rates from configuration.

        Loads conversion rates from the YAML configuration file based on the
        specified converter type. The rates are stored in self.rates for use
        in conversion calculations.

        Args:
            converter_type (str): Type of unit conversion (e.g., 'length', 'weight',
                                'temperature', 'liquid')

        Side Effects:
            - Sets self.rates with conversion rates from YAML configuration
        """
        config_path = Path(__file__).parent.parent / "config" / "conversion_rates.yaml"
        with open(config_path, "r") as f:
            self.rates = yaml.safe_load(f)[converter_type]

    def get_conversion_rate(self, source: str, target: str) -> float:
        """Get the conversion rate between source and target units.

        Args:
            source (str): The source unit
            target (str): The target unit

        Returns:
            float: The conversion rate from source to target unit
        """
        if source == target:
            return 1.0
        return self.rates[source][target]

    def convert(self, source_unit: str, target_unit: str, value: float) -> float:
        """Convert a value between units using conversion rates or formulas.

        Performs unit conversion based on the rates defined in the configuration.
        If source and target units are the same, returns the original value.
        For simple conversions, multiplies the value by the conversion rate.
        For complex conversions (like temperature), uses the formula from config.

        Args:
            source_unit (str): The unit to convert from (e.g., 'meters', 'celsius')
            target_unit (str): The unit to convert to (e.g., 'kilometers', 'fahrenheit')
            value (float): The numeric value to convert

        Returns:
            float: The converted value in the target unit

        Examples:
            >>> converter = LengthConverter()
            >>> converter.convert('meters', 'kilometers', 1000)
            1.0
            >>> converter.convert('celsius', 'fahrenheit', 0)  # Using formula
            32.0
        """
        if source_unit == target_unit:
            return value

        rate = self.get_conversion_rate(source_unit, target_unit)
        if isinstance(rate, dict) and "formula" in rate:
            # Handle special cases like temperature conversion
            return eval(rate["formula"], {"value": value})
        return value * rate
