# Example 1: Annotating a Function argument as a Callable
from typing import Callable


def apply_function(func: Callable[[int, int], int], arg1: int, arg2: int) -> int:
    """Apply a function to two arguments.

    Args:
        func (Callable[[int, int], int]): The function to apply.
        arg1 (int): The first argument to pass to the function.
        arg2 (int): The second argument to pass to the function.

    Returns:
        int: The result of applying the function to the arguments.
    """
    return func(arg1, arg2)


def add(x: int, y: int) -> int:
    """Add two integers.

    Args:
        x (int): The first integer to add.
        y (int): The second integer to add.

    Returns:
        int: The sum of x and y.
    """
    return x + y


result = apply_function(add, 5, 3)
print("Annotating a Function argument as a Callable: ", result)


# Example 2: Annotating a Callable with No Arguments
def execute_task(task: Callable[[], None]) -> None:
    """Execute a task.

    Args:
        task (Callable[[], None]): The task to execute.

    Returns:
        None: The task is executed.
    """
    task()


def say_hello() -> None:
    """Say hello to the world."""
    print("Hello, world!")


execute_task(say_hello)


# Example 3: Annotating Methods with Callable return types
def multiplier(factor: int) -> Callable[[int], int]:
    """Create a multiplier function.

    Args:
        factor (int): The factor to multiply by.

    Returns:
        Callable[[int], int]: A function that multiplies a number by the factor.
    """
    return lambda x: x * factor


# Create a doubling function
double = multiplier(2)
# Use the returned function
result = double(5)
print("Annotating Methods with Callable return types: ", result)
