# Example 1: Use some set operations to create a new set
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Using the union() method
result_union_method = set1.union(set2)
print(result_union_method)  # Output: {1, 2, 3, 4, 5}

# Using the | operator
result_union = set1 | set2
print(result_union)  # Output: {1, 2, 3, 4, 5}

# Using the difference() method
result_difference_method = set1.difference(set2)
print(result_difference_method)  # Output: {1, 2}

# Using the - operator
result_difference = set1 - set2
print(result_difference)  # Output: {1, 2}

# Using the intersection() method
result_intersection_method = set1.intersection(set2)
print(result_intersection_method)  # Output: {3, 4, 5}

# Using the & operator
result_intersection = set1 & set2
print(result_intersection)  # Output: {3, 4, 5}

# Using the symmetric_difference() method
result_symmetric_difference_method = set1.symmetric_difference(set2)
print(result_symmetric_difference_method)  # Output: {1, 2, 6, 7}

# Using the ^ operator
result_symmetric_difference = set1 ^ set2
print(result_symmetric_difference)  # Output: {1, 2, 6, 7}


# Example 2: Use a set comprehension to create a new set from an existing set
def extract_unique_characters(string: str) -> set:
    """
    Extract all unique alphabetic characters from the input string.

    Args:
        string (str): The input string to process

    Returns:
        set: A set containing all unique alphabetic characters found in the input string
    """
    unique_chars = {char for char in string if char.isalpha()}
    return unique_chars


string = "Hello, World!"
unique_chars = extract_unique_characters(string)
print(unique_chars)  # Output: {'H', 'e', 'l', 'o', 'W', 'r', 'd', ','}

# Example 3: Use sets to determine if two lists share any common elements
list_one = ["Manny", "Moe", "Jack"]
list_two = ["Larry", "Moe", "Curly"]


def has_duplicate(list_one: list, list_two: list) -> set:
    """
    Find common elements between two lists using set intersection.

    Args:
        list_one (list): First list to compare
        list_two (list): Second list to compare

    Returns:
        set: A set containing all elements that appear in both input lists
    """
    return set(list_one) & set(list_two)


print(has_duplicate(list_one, list_two))  # Output: {'Moe'}


# Example 4: Use sets to eliminate duplicate entries from iterable containers
def remove_duplicates(iterable: list) -> set:
    """
    Remove duplicate sublists from a nested list by converting them to tuples in a set.

    Args:
        iterable (list): A nested list containing sublists that may have duplicates

    Returns:
        set: A set of tuples where each tuple represents a unique sublist from the input
             Duplicates are automatically eliminated due to set properties
    """
    nested = iterable
    unique_nested = set(tuple(sublist) for sublist in nested)

    return unique_nested


nested_list = [[1, 2], [3, 4], [1, 2], [5, 6]]
unique_nested_list = remove_duplicates(nested_list)
print(unique_nested_list)  # Output: {(1, 2), (3, 4), (5, 6)}
