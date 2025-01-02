from constants import CONVERSION_TYPES


def render_conversion_options() -> None:
    """Display the available conversion options to the user."""
    print("Conversion options:")
    for idx, conversion_type in enumerate(CONVERSION_TYPES, 1):
        print(
            f"{idx}. {conversion_type['name'].capitalize()}: {conversion_type['description']}"
        )
    print("\nPress e & exit to exit")
    print("Choose the number corresponding to your selection")
    print("==============")


def render_unit_by_conversion_type(option: int) -> None:
    """Display available units for the selected conversion type.

    Args:
        option (int): The conversion type option (1-4)
    """
    conversion_type = CONVERSION_TYPES[option - 1]
    print(f"\nAvailable units for {conversion_type['name']}:")
    units = conversion_type["unit"]
    for unit in units:
        print(f"- {unit}")


def render_result(
    value: float, source_unit: str, target_unit: str, result: float
) -> None:
    """Display the result section of the application."""
    print("\n")
    print("==============")
    print(f"Result: {value} {source_unit} = {result} {target_unit}")
    print("==============")
