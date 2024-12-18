# Example 1: Use ''.join() to join a list of strings into a single string
result_list = ["True", "False", "File not found"]
result_string = "".join(result_list)

print(result_string)


# Example 2: Use ord to get the ASCII code of a character and
# chr to get the character from its ASCII code
def hash(some_string: str) -> int:
    hash_value = 0

    for e in some_string:
        hash_value += ord(e)
    return hash_value


print(hash("hello"))


# Example 3: Use str.format() to format a string
def get_formatted_user_info(user: object) -> str:
    output = "Name: {user.name}, Age: {user.age}, Sex: {user.sex}".format(**user)
    return output


print(get_formatted_user_info({"name": "John", "age": 30, "sex": "M"}))
# Result: Name: John, Age: 30, Sex: M
