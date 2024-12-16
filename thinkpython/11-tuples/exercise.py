# Exercise 1: Write a line of code that appends the value 6 to the end of the second list in t.
# If you display t, the result should be ([1, 2, 3], [4, 5, 6]).
list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)

convert_list = list(t)
convert_list[1].append(6)
convert_tuple = tuple(convert_list)

print(convert_tuple)

# Exercise 2: Try to create a dictionary that maps from t to a string, and confirm that you get a TypeError.
dict = {(list0, list1): "dictionary"}

print(dict)


# Exercise 3: Write a function called most_frequent_letters that takes a string and prints the letters in decreasing order of frequency.
def most_frequent_letters(string: str) -> list:
    """
    Analyze and print letter frequencies in a given string.

    This function processes a string to count and display the frequency
    of alphabetic characters in descending order of occurrence.

    Args:
        string (str): The input string to analyze.

    Returns:
        list[tuple[str, int]]: A list of tuples where each tuple contains:
            - str: A single character from the input string
            - int: The number of times that character appears
            The list is sorted by frequency in descending order.
    Process:
        1. Convert string to lowercase
        2. Filter out non-alphabetic characters
        3. Count letter occurrences
        4. Sort and print letters by frequency

    Examples:
        >>> most_frequent_letters('hello world')
        [('l', 3), ('o', 2), ('h', 1), ('e', 1), ('w', 1), ('r', 1), ('d', 1)]
    """

    # Lower all letters, check alpha
    lower_letter = string.lower()
    char = []
    for letter in lower_letter:
        if letter.isalpha():
            char.append(letter)

    # Count the number of each letter
    counter = {}
    for item in char:
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1
    print(counter)

    # Sort by frequency
    sorted_letters = sorted(counter.items(), reverse=True)

    for ch, count in sorted_letters:
        print(f"{ch}: {count}")

    return sorted_letters


# Test cases
print(most_frequent_letters("hello world"))
