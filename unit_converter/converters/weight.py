from .base import BaseConverter


class WeightConverter(BaseConverter):
    """Converter for weight units (kilograms and grams)."""

    def __init__(self) -> None:
        """Initialize the weight converter."""
        super().__init__("weight")
