# Example 1: Generator with send method
from typing import Generator, AsyncGenerator
import asyncio


def accumulator() -> Generator[int, int, None]:
    """Create a generator that accumulates values sent to it.

    This generator demonstrates the advanced generator protocol by allowing
    values to be sent to it using .send() method. It maintains a running total
    of values sent to it and yields the current total after each addition.

    The generator works as follows:
    - It starts with an initial total of 0
    - Each time a value is sent, it adds the value to the total
    - It yields the current total after each addition
    - If None is sent, it breaks the generator and returns the final total

    Yields:
        int: The current running total after each value addition.

    Returns:
        int: The final accumulated total when the generator is closed.

    Example:
        >>> acc = accumulator()
        >>> next(acc)  # Initialize the generator
        0
        >>> acc.send(10)  # Send first value
        10
        >>> acc.send(5)   # Send another value
        15
        >>> acc.send(None)  # Close the generator
        15
    """
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

    return total


# Example usage
acc = accumulator()
print(next(acc))  # Output: 0
print(acc.send(10))  # Output: 10
print(acc.send(5))  # Output: 15
# print(acc.send(None))  # Output: 15


# Example 2: Async Generator
async def async_countdown(n: int) -> AsyncGenerator[int, None]:
    """Create an asynchronous generator that counts down from a given number.

    This async generator yields decreasing integers from the input number
    to 1, with a 1-second delay between each yield. It demonstrates the
    usage of async generators and asynchronous iteration.

    The generator works as follows:
    - It starts from the input number `n`
    - Yields each number from `n` down to 1
    - Introduces a 1-second delay between each yield using `asyncio.sleep()`
    - Stops when the counter reaches 0

    Args:
        n (int): The starting number to count down from.

    Yields:
        int: Decreasing integers from `n` down to 1.

    Example:
        >>> async def main():
        ...     async for num in async_countdown(5):
        ...         print(num)
        >>> # This would print: 5, 4, 3, 2, 1 with 1-second intervals
    """
    while n > 0:
        yield n
        n -= 1
        await asyncio.sleep(1)


async def main():
    async for num in async_countdown(5):
        print(num)


asyncio.run(main())
