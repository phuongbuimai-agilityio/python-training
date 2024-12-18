# Example 1: Use dict to replace switch...case statement
import operator as op


def apply_operation(left_operand, right_operand, operator):
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
