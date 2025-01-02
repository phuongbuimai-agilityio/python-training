from .base import BaseConverter


class LiquidConverter(BaseConverter):
    """Converter for liquid units (liters and milliliters)."""

    def __init__(self) -> None:
        """Initialize the liquid converter."""
        super().__init__("liquid")
