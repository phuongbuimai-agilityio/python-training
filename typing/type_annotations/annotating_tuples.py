# Example 1: Fixed-Length Tuples
from typing import Tuple


def get_coordinates() -> Tuple[int, int]:
    """Get coordinates.

    Returns:
        Tuple[int, int]: A tuple of two integers.
    """
    return (10, 20)  # Fixed-length tuple with 10, 20


coordinates = get_coordinates()
print("Fixed-Length Tuples: ", coordinates)


# Example 2: Variable-Length Tuples
def sum_numbers(*args: Tuple[int, ...]) -> int:
    """Sum numbers.

    Args:
        *args: Variable-length tuple of integers.

    Returns:
        int: The sum of the numbers in the tuple.
    """
    return sum(args)


result = sum_numbers(1, 2, 3, 4, 5)
print("Variable-Length Tuples: ", result)


# Example 3: Nested Tuples
def get_nested_tuple() -> Tuple[int, Tuple[str, str]]:
    """Get a nested tuple.

    Returns:
        Tuple[int, Tuple[str, str]]: A tuple containing an integer and a tuple of strings.
    """
    return (1, ("a", "b"))


nested_tuple = get_nested_tuple()
print("Nested Tuples: ", nested_tuple)
