from typing import Dict, Type
from .base import BaseConverter
from .length import LengthConverter
from .weight import WeightConverter
from .temperature import TemperatureConverter
from .liquid import LiquidConverter


class ConverterFactory:
    """Factory class to create appropriate converters based on a numerical option provided."""

    _converters: Dict[int, Type[BaseConverter]] = {
        1: LengthConverter,
        2: WeightConverter,
        3: TemperatureConverter,
        4: LiquidConverter,
    }

    @classmethod
    def create_converter(cls, option: int) -> BaseConverter:
        """Create a converter instance based on the specified conversion option.

        Args:
            option (int): The conversion option (1-4)

        Returns:
            BaseConverter: An instance of the appropriate converter
        """
        converter_class = cls._converters.get(option)
        if converter_class:
            return converter_class()
