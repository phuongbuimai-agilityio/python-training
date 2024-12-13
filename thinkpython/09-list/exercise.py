# Exercise 1: Two words are anagrams if you can rearrange the letters from one to spell the other.
# For example, tops is an anagram of stop.

# One way to check whether two words are anagrams is to sort the letters in both words.
# If the lists of sorted letters are the same, the words are anagrams.

# Write a function called is_anagram that takes two strings and returns True if they are anagrams.


# Remove whitespace, and convert to lowercase
def remove_whitespace(word):
    """
    Remove all whitespace from a given string and convert it to lowercase.

    This function strips out all spaces from the input string and transforms
    the remaining characters to lowercase, which can be useful for
    text normalization and comparison.

    Args:
        word (str): The input string to process.

    Returns:
        str: A new string with all whitespace removed and converted to lowercase.

    Examples:
        >>> remove_whitespace("Hello World")
        'helloworld'
        >>> remove_whitespace("  Python  Programming  ")
        'pythonprogramming'
        >>> remove_whitespace("No Spaces")
        'nospaces'
        >>> remove_whitespace("")
    """
    word = word.replace(" ", "").lower()
    return word


def is_anagram(word1, word2):
    """
    Check if two words are anagrams, ignoring spaces and case.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        bool: True if the words are anagrams, False otherwise.

    Examples:
        >>> is_anagram('listen', 'silent')
        True
        >>> is_anagram('hello', 'world')
        False
        >>> is_anagram('Debit Card', 'Bad Credit')
        True
        >>> is_anagram('Python', 'Typhon')
        True
        >>> is_anagram('', '')
        True
    """
    word1 = remove_whitespace(word1)
    word2 = remove_whitespace(word2)

    return sorted(word1) == sorted(word2)


# Test cases
print(is_anagram("tops", "stop"))  # True
print(is_anagram("apple", "banana"))  # False

# Exercise 2: Write a function called reverse_sentence
# that takes as an argument a string that contains any number of words separated by spaces.


def reverse_sentence(input_string):
    """
    Reverse the order of words in a sentence.

    Args:
        input_string (str): The input sentence.

    Returns:
        str: The sentence with word order reversed and the first letter capitalized.

    Examples:
        >>> reverse_sentence('hello world')
        'World hello'
        >>> reverse_sentence('Python is awesome')
        'Awesome is python'
        >>> reverse_sentence('I love programming')
        'Programming love i'
    """
    # Split the sentence into words, reverse the list, and join them back
    sentence = " ".join(input_string.split()[::-1]).lower()

    return sentence.capitalize()


# Test cases
print(reverse_sentence("Python list"))  # "List python"
print(reverse_sentence("Hello world"))  # "World hello"
print(reverse_sentence("  Multiple   spaces  "))  # "Spaces multiple"
