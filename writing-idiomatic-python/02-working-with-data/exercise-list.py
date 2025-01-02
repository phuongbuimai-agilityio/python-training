# Example 1: Use list comprehension to create a new list from an existing list
original_list = [1, 2, 3, 4, 5]
new_list = [x * 2 for x in original_list]

print(new_list)


# Example 2: Use negative indexing to access the last element of a list
def get_suffix(word: str) -> str:
    """Extract the last two characters from a string.

    Args:
        word (str): The input string to extract from

    Returns:
        str: The last two characters of the input string.
             If the string is shorter than 2 characters,
             returns the entire string.

    Example:
        >>> get_suffix("hello")
        'lo'
        >>> get_suffix("a")
        'a'
    """
    return word[-2:]


print(get_suffix("hello"))
# Output: "lo"

# Example 3: Prefer list comprehensions over map and filter
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers_times_two = [n * 2 for n in the_list if n % 2 == 1]

print(odd_numbers_times_two)

# Example 4: Use sum to calculate the sum of a list
the_list = [1, 2, 3, 4, 5]
result = sum(the_list)

print(result)


# Example 5: Use all to check if all elements in a list are True
def contains_zero(iterable: list) -> bool:
    """Check if the given iterable contains any zero values.

    Args:
        iterable (list): A list of numeric values to check

    Returns:
        bool: True if the iterable contains at least one zero value,
              False otherwise

    Example:
        >>> contains_zero([1, 0, 2, 3])
        True
        >>> contains_zero([1, 2, 3])
        False

    Note:
        This function uses Python's truthiness where 0 is considered False,
        and the built-in all() function which returns False if any element
        is falsy.
    """

    return not all(iterable)


print(contains_zero([1, 2, 3]))
# Output: False

print(contains_zero([0, 2, 3]))
# Output: True

# Example 6: Use the * operator to represent the rest of a list
some_list = ["a", "b", "c", "d", "e"]
(first, second, *rest) = some_list
print(rest)
(first, *middle, last) = some_list
print(middle)
(*head, penultimate, last) = some_list
print(head)
