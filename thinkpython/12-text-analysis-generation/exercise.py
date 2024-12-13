# Exercise: Write a function that counts the number of times each trigram (sequence of three words) appears
from collections import Counter


def count_trigrams(text, case_insensitive=True):
    """
    Count and analyze trigrams (sequences of three consecutive words) in a given text.

    A trigram is a sequence of three consecutive words that appear together in the text.
    This function splits the text, generates trigrams, and counts their frequencies.

    Args:
        text (str): The input text to analyze.
        case_insensitive (bool): If True, normalize text to lowercase.

    Returns:
        Counter: A dictionary-like object mapping trigrams to their occurrence counts.

    Process:
        1. Split the text into words
        2. Generate trigrams using sliding window approach
        3. Count frequency of each trigram
        4. Print trigram frequencies
        5. Return trigram counts

    Examples:
        >>> text = "the quick brown fox jumps over the lazy dog"
        >>> count_trigrams(text)
        the quick brown: 1
        quick brown fox: 1
        brown fox jumps: 1
        fox jumps over: 1
        jumps over the: 1
        over the lazy: 1
        the lazy dog: 1

    Notes:
        - Trigrams include overlapping sequences.
        - If `case_insensitive` is True, text will be converted to lowercase.
        - If the text has fewer than three words, an empty Counter is returned.

    See Also:
        - collections.Counter: Used for efficient frequency counting
        - List comprehensions: Used to generate trigrams
    """
    # Normalize case if required
    if case_insensitive:
        text = text.lower()

    # Split the text into words, ignoring extra spaces
    words = text.split()

    # Check if there are enough words for trigrams
    if len(words) < 3:
        return Counter()

    # Generate trigrams (sequences of three consecutive words)
    trigrams = [" ".join(words[i : i + 3]) for i in range(len(words) - 2)]

    # Count the frequency of each trigram
    return Counter(trigrams)


# Helper function to print sorted trigrams
def print_trigrams(counter):
    """
    Print trigrams and their counts sorted by frequency (descending) and alphabetically for ties.

    Args:
        counter (Counter): A Counter object mapping trigrams to their counts.
    """
    for trigram, count in counter.most_common():
        print(f"{trigram}: {count}")


# Test cases
text = "the quick brown fox jumps over the lazy dog the quick brown fox"
trigram_counts = count_trigrams(text)
print_trigrams(trigram_counts)
