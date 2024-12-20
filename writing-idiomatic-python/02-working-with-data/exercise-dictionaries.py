# Example 1: Use dict to replace switch...case statement
import operator as op


def apply_operation(left_operand, right_operand, operator):
    """Apply basic arithmetic operation between two operands.

    Args:
        left_operand (number): The left operand of the operation
        right_operand (number): The right operand of the operation
        operator (str): The arithmetic operator to apply. Must be one of:
            '+': addition
            '-': subtraction
            '*': multiplication
            '/': division

    Returns:
        number: Result of applying the operator to the operands

    Raises:
        KeyError: If operator is not one of '+', '-', '*', '/'
        ZeroDivisionError: If right_operand is 0 and operator is '/'

    Example:
        >>> apply_operation(10, 5, '+')
        15
        >>> apply_operation(10, 2, '*')
        20
    """

    operator_mapper = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}

    return operator_mapper[operator](left_operand, right_operand)


print(apply_operation(2, 3, "+"))
# Output: 5

# Example 2: Use the default parameter of dict.get() to provide default values
data = {"name": "Alice", "age": 30}

# Accessing an existing key
print(data.get("name", "Unknown"))  # Output: Alice

# Accessing a non-existing key
print(data.get("gender", "Unknown"))  # Output: Unknown

# Example 3: Use a dict comprehension to create a new dictionary from an existing dictionary
original_dict = {"a": 1, "b": 2, "c": 3}
new_dict = {k: v * 2 for k, v in original_dict.items()}

print(new_dict)
# Output: {'a': 2, 'b': 4, 'c': 6}
