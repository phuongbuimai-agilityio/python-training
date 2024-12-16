# Exercise 1: Write a function named uses_none that takes a word and a string of forbidden letters,
# and returns True if the word does not use any of the forbidden letters.
def uses_none(word: str, forbidden: str) -> bool:
    """
    Check if a word contains none of the forbidden letters.

    This function determines whether a given word uses any letters from a specified
    forbidden set. The comparison is case-insensitive.

    Args:
        word (str): The word to check for forbidden letters.
        forbidden (str): A string containing letters that are not allowed in the word.

    Returns:
        bool: True if the word does not contain any of the forbidden letters,
              False otherwise.

    Examples:
        >>> uses_none('banana', 'xyz')
        True
        >>> uses_none('apple', 'abc')
        False
        >>> uses_none('Hello', 'h')
        False
        >>> uses_none('Python', 'qrst')
        True

    Notes:
        - The function converts both the word and forbidden letters to lowercase
          to ensure case-insensitive comparison.
        - An empty forbidden string will always return True.
        - An empty word will always return True.
    """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True


print(uses_none("banana", "xyz"))
print(uses_none("apple", "abc"))

# Exercise 2: Write a function called uses_all that takes a word and a string of letters,
# and that returns True if the word contains all of the letters in the string at least once.


def uses_all(word: str, required: str) -> bool:
    """
    Check if a word contains all of the required letters.

    This function determines whether a given word includes every letter
    from a specified required set. The comparison is case-insensitive.

    Args:
        word (str): The word to check for required letters.
        required (str): A string containing letters that must be present in the word.

    Returns:
        bool: True if the word contains all of the required letters,
              False otherwise.

    Examples:
        >>> uses_all('hello', 'hel')
        True
        >>> uses_all('python', 'py')
        True
        >>> uses_all('banana', 'ban')
        True
        >>> uses_all('apple', 'xyz')
        False
        >>> uses_all('programming', 'prog')
        True

    Notes:
        - The function converts both the word and required letters to lowercase
          to ensure case-insensitive comparison.
        - An empty required string will always return True.
        - An empty word will return False if required is not empty.
        - Each required letter needs to appear at least once in the word.
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True


print(uses_all("banana", "ban"))
print(uses_all("apple", "api"))
