conversion_types = {
    "length": "Convert between units of length (e.g., meters, kilometers).",
    "weight": "Convert between units of weight (e.g., kilograms, grams).",
    "temperature": "Convert between temperature scales (e.g., Celsius, Fahrenheit).",
    "liquid": "Convert between liquid volumes (e.g., liters, milliliters).",
}


def render_conversion_options():
    print("Conversion Options:")
    for idx, (type, description) in enumerate(conversion_types.items(), 1):
        print(f"{idx}. {type.capitalize()}: {description}")
    print("5. Exit")
    print()
