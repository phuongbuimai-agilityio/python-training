from .base import BaseConverter


class LengthConverter(BaseConverter):
    """Converter for length units (meters and kilometers)."""

    def __init__(self) -> None:
        """Initialize the length converter."""
        super().__init__("length")
