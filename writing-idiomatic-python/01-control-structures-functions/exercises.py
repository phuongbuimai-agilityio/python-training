# Example 1: Use *args and **kwargs to accept arbitrary arguments
def print_list(list_value: list, sep: str) -> None:
    """Print elements of a list joined by a separator.

    Args:
        list_value (list): The list of elements to be printed.
        sep (str): The separator to use between list elements.
    """
    print("{}".format(sep).join(list_value))


the_list = ["a", "b", "c"]
the_other_list = ["Jeff", "hates", "Java"]

print_list(the_list, " ")  # Result: a b c
print_list(the_other_list, " ")  # Result: Jeff hates Java
print_list(
    the_other_list, ", "
)  # Result: Jeff, hates, Java (add the character between values)


def for_console_output(func: callable) -> callable:
    """Decorator that wraps function output with separator lines.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A wrapped function that prints its return value between separator lines.

    Example:
        @for_console_output
        def my_func():
            return "Hello World"

        # Output:
        # --------------------------------
        # Hello World
        # --------------------------------
    """

    def wrapper(*args, **kwargs):
        print("--------------------------------")
        print(str(func(*args, **kwargs)))
        print("--------------------------------")

    return wrapper


@for_console_output
def add(x: any, y: any) -> any:
    """Add two values together.

    Args:
        x (any): First value to add.
        y (any): Second value to add.

    Returns:
        any: The sum of x and y.

    Example:
        >>> add(3, 2)
        --------------------------------
        5
        --------------------------------
    """
    return x + y


add(3, 2)
