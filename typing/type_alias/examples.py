from typing import List, Tuple, Dict, Set, Union

# Example 1: Aliases for Primitive Types
# Alias for primitive types
Age = int
Price = float
URL = str


def display_age(age: Age) -> None:
    print(f"The user's age is {age}")


display_age(30)  # Output: The user's age is 30

# Example 2: Aliases for Data Structures
# Collections
NameList = List[str]
Coordinates = Tuple[float, float]  # Latitude and Longitude
Inventory = Dict[str, int]  # Item name and quantity
UniqueIDs = Set[int]


def process_inventory(items: Inventory) -> None:
    """Process and display the inventory items.

    This function iterates through an inventory dictionary, printing
    each item's name and its corresponding quantity. It is designed
    to work with the `Inventory` type alias, which represents a
    dictionary mapping item names to their quantities.

    Args:
        items (Inventory): A dictionary containing inventory items
                           where keys are item names and values are
                           their quantities.

    Returns:
        None: The function prints inventory information but does not
              return any value.

    Example:
        >>> inventory = {"apple": 5, "banana": 3, "orange": 7}
        >>> process_inventory(inventory)
        Item: apple, Quantity: 5
        Item: banana, Quantity: 3
        Item: orange, Quantity: 7
    """
    for item, qty in items.items():
        print(f"Item: {item}, Quantity: {qty}")


inventory: Inventory = {
    "Apples": 10,
    "Oranges": 5,
}
process_inventory(inventory)

# Example 3: Union Types
# Union for multiple types
UserID = Union[int, str]  # User ID can be an integer or string
Response = Union[str, None]  # Response can be a string or None


def fetch_user(id: UserID) -> Response:
    """Fetch user information based on a flexible user identifier.

    This function demonstrates the use of Union types by accepting
    a user identifier that can be either an integer or a string.
    It returns a formatted user information string or None.

    The function handles two types of user identifiers:
    - Integer IDs: Returns a message with the numeric ID
    - String usernames: Returns a message with the username

    Args:
        id (UserID): A user identifier that can be either an integer
                     or a string. Represents either a numeric user ID
                     or a username.

    Returns:
        Response: A string describing the user if found, or None if
                  the identifier is not an int or str.

    Example:
        >>> fetch_user(123)
        'User found with ID: 123'
        >>> fetch_user('johndoe')
        'User found with username: johndoe'
        >>> fetch_user(None)
        None
    """
    if isinstance(id, int):
        return f"User found with ID: {id}"
    elif isinstance(id, str):
        return f"User found with username: {id}"
    return None


user_id = 123
response = fetch_user(user_id)
print(response)
