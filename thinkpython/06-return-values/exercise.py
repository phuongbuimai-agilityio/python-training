# Exercise 1: Write a boolean function, is_between(x, y, z), that returns True if  x<y<z  or if  z<y<x , and False otherwise.


def is_between(x: int, y: int, z: int) -> bool:
    """
    Check if a value is between two other values, considering both ascending and descending orders.

    This function determines whether the middle value `y` is between `x` and `z`,
    regardless of whether the comparison is in ascending or descending order.

    Args:
        x (comparable): The first value to compare.
        y (comparable): The middle value to check.
        z (comparable): The last value to compare.

    Returns:
        bool: True if `y` is between `x` and `z`, False otherwise.

    Examples:
        >>> is_between(1, 2, 3)
        True
        >>> is_between(3, 2, 1)
        True
        >>> is_between(1, 4, 3)
        False
        >>> is_between(1, 1, 3)
        False

    Notes:
        Another solution is to use ordering of comparison operators.
        >>> return x < y < z or z < y < x
    """
    if x < y < z:
        return True
    elif z < y < x:
        return True
    else:
        return False


# Test cases
print(is_between(1, 2, 3))  # True
print(is_between(3, 2, 1))  # True
print(is_between(1, 3, 2))  # False
print(is_between(2, 2, 2))  # False (equality is not considered "between")

# Exercise 2: The Ackermann function,  A(m,n) , is defined:
# A(m,n) = n+1 if m = 0
# A(m,n) = A(m-1,1) if m > 0 and n = 0
# A(m,n) = A(m-1,A(m,n-1)) if m > 0 and n > 0
# Write a function named ackermann that evaluates the Ackermann function. What happens if you call ackermann(5, 5)?


def ackermann(m: int, n: int) -> int:
    """
    Compute the Ackermann function, a classic example of a recursive function that grows very quickly.

    The Ackermann function is a fundamental example in computability theory and recursive function theory.
    It is known for its extreme growth rate and is not primitive recursive.

    Args:
        m (int): First non-negative integer parameter.
        n (int): Second non-negative integer parameter.

    Returns:
        int: Result of the Ackermann function computation.

    Formula:
        A(m,n) =
        - n + 1                           if m = 0
        - A(m-1, 1)                       if m > 0 and n = 0
        - A(m-1, A(m, n-1))               if m > 0 and n > 0

    Examples:
        >>> ackermann(0, 0)
        1
        >>> ackermann(1, 1)
        3
        >>> ackermann(2, 2)
        7

    Warnings:
        - This function grows extremely quickly and can cause stack overflow for large inputs.
        - Recommended to use small values of m and n (typically m < 4).

    Notes:
        - The function is not tail-recursive and can be very computationally expensive.
        - It demonstrates the power and potential pitfalls of recursive programming.
    """
    if m < 0 or n < 0:
        raise ValueError("Both m and n must be non-negative integers.")
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:  # m > 0 and n > 0
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 2))
print(
    ackermann(6, 5)
)  # Throw RecursionError because the depth of recursion already exceeds Python's default limit
