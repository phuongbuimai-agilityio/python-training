# Exercise 1: Write a function named has_duplicates that takes a sequence -- like a list or string -- as a parameter
# and returns True if there is any element that appears in the sequence more than once.


def value_counts(sequence):
    """
    Count the occurrences of each element in a sequence.

    This function creates a dictionary that maps each unique element
    in the input sequence to its number of occurrences.

    Args:
        sequence (iterable): The input sequence to count elements from.
                           Can be a string, list, or any other iterable.

    Returns:
        dict: A dictionary where keys are unique elements from the input,
              and values are the number of times each element appears.

    Examples:
        >>> value_counts('banana')
        {'b': 1, 'a': 3, 'n': 2}
        >>> value_counts([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}

    Notes:
        Another solution is to use the Counter class from the collections module.
        >>> return Counter(sequence)
    """
    counter = {}
    for letter in sequence:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


def has_duplicates(sequence):
    """Check whether any element in a sequence appears more than once.

    Args:
        sequence (iterable): The input sequence to check for duplicates.

    Returns:
        bool: True if there are duplicates, False otherwise.

    Examples:
    >>> has_duplicates('banana')
    True
    >>> has_duplicates('ambidextrously')
    False
    >>> has_duplicates([1, 2, 2])
    True
    >>> has_duplicates([1, 2, 3])
    False
    """
    counter = value_counts(sequence)
    for count_item in counter.values():
        if count_item > 1:
            return True
    return False


print(has_duplicates([1, 2, 2]))
print(has_duplicates([1, 2, 3]))

# Exercise 2: Write function called find_repeats that takes a dictionary that maps from each key to a counter,
# like the result from value_counts. It should loop through the dictionary and return a list of keys that have counts greater than 1


def find_repeats(input_dict):
    """Find keys with values greater than 1 in a dictionary.

    Args:
        input_dict (dict): A dictionary mapping keys to their counts.

    Returns:
        list: A list of keys with values greater than 1.

    Examples:
        >>> find_repeats({'a': 2, 'b': 1, 'c': 3})
        ['a', 'c']
        >>> find_repeats({'apple': 1, 'banana': 2, 'cherry': 1})
        ['banana']
    """
    return [key for key, count in input_dict.items() if count > 1]


string_counts = value_counts("banana")  # First, convert string to a counts dictionary
print(find_repeats(string_counts))  # ['a', 'n']
