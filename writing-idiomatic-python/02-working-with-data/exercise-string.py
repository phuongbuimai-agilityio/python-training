# Example 1: Use ''.join() to join a list of strings into a single string
result_list = ["True", "False", "File not found"]
result_string = "".join(result_list)

print(result_string)


# Example 2: Use ord to get the ASCII code of a character and
# chr to get the character from its ASCII code
def hash(some_string: str) -> int:
    """Calculate a simple hash value for a given string.

    Args:
        some_string (str): The input string to hash

    Returns:
        int: The hash value calculated as the sum of ASCII values of all characters
    """
    hash_value = 0

    for e in some_string:
        hash_value += ord(e)
    return hash_value


print(hash("hello"))


# Example 3: Use str.format() to format a string
def get_formatted_user_info(user: object) -> str:
    """Format user information into a readable string.

    Args:
        user (object): A dictionary-like object containing user data with keys:
            - name: user's name
            - age: user's age
            - sex: user's sex/gender

    Returns:
        str: A formatted string containing the user's information in the format:
            "Name: {name}, Age: {age}, Sex: {sex}"

    Example:
        >>> user = {"name": "John", "age": 30, "sex": "M"}
        >>> get_formatted_user_info(user)
        'Name: John, Age: 30, Sex: M'
    """


print(get_formatted_user_info({"name": "John", "age": 30, "sex": "M"}))
# Result: Name: John, Age: 30, Sex: M
