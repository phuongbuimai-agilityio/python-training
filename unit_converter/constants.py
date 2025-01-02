"""Constants used throughout the unit converter application."""

# Exit options (case-insensitive)
EXIT_OPTIONS = ("e", "exit")

# Conversion types
CONVERSION_TYPES: list[dict] = [
    {
        "option": 1,
        "name": "length",
        "description": "Convert between units of length (e.g., meters, kilometers)",
        "unit": ("meters", "kilometers"),
    },
    {
        "option": 2,
        "name": "weight",
        "description": "Convert between units of weight (e.g., kilograms, grams)",
        "unit": ("kilograms", "grams"),
    },
    {
        "option": 3,
        "name": "temperature",
        "description": "Convert between units of temperature (e.g., celsius, fahrenheit)",
        "unit": ("celsius", "fahrenheit"),
    },
    {
        "option": 4,
        "name": "liquid",
        "description": "Convert between units of liquid volume (e.g., liters, milliliters)",
        "unit": ("liters", "milliliters"),
    },
]
