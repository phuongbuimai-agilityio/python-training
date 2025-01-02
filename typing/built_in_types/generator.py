# Example for generator function
def count_up_to(n: int) -> int:
    """
    Generate a sequence of integers from 1 up to and including n.

    This generator function yields consecutive integers starting from 1
    and continuing until the specified maximum value is reached.

    Args:
        n (int): The maximum value to count up to.

    Yields:
        int: Consecutive integers from 1 to n.

    Example:
        >>> list(count_up_to(5))
        [1, 2, 3, 4, 5]
    """
    count = 1
    while count <= n:
        yield count  # Pause and return the current value
        count += 1


gen = count_up_to(3)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# Raises StopIteration if called again

# Example for generator expression
squares = (x**2 for x in range(10))

for square in squares:
    print(square)
