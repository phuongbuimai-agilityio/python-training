from collections import Counter

# Example 1: Use collections.namedtuple to make tuple-heavy code more clear
from collections import namedtuple

# Define namedtuple
Employee = namedtuple("Employee", ["name", "position", "salary"])

# Create a list of employees
employees = [
    Employee("Alice", "Developer", 90000),
    Employee("Bob", "Designer", 80000),
    Employee("Charlie", "Manager", 120000),
]


def get_employees(employees: list) -> None:
    """
    Print information about each employee in the given list.

    Args:
        employees (list): A list of employee objects, where each object has
                         name, position, and salary attributes

    Returns:
        None: This function prints to stdout and doesn't return anything
    """
    # Access information
    for emp in employees:
        print(f"{emp.name} is a {emp.position} earning ${emp.salary}")


get_employees(employees)


# Example 2: Use _ as a placeholder for data in a tuple that should be ignored
def get_user_info():
    return "Alice", 30, "Engineer"


# Unpack only the name and profession
name, _, profession = get_user_info()
print(name)  # Output: Alice
print(profession)  # Output: Engineer

# Example 3: Use tuples to unpack data
list_from_comma_separated_value_file = ["dog", "Fido", 10]
(animal, name, age) = list_from_comma_separated_value_file
output = "{name} the {animal} is {age} years old".format(
    animal=animal, name=name, age=age
)

print(output)
# Example 4: Use a tuple to return multiple values from a function
STATS_FORMAT = """Statistics:
Mean: {mean}
Median: {median}
Mode: {mode}"""


def calculate_staistics(value_list: list) -> tuple:
    """
    Calculate basic statistical measures (mean, median, mode) for a list of numbers.

    Args:
        value_list (list): A list of numeric values to analyze

    Returns:
        tuple: A tuple containing three elements:
            - mean (float): The arithmetic mean of the values
            - median (float): The middle value when sorted
            - mode (Any): The most frequently occurring value
    """
    mean = float(sum(value_list) / len(value_list))
    median = value_list[int(len(value_list) / 2)]
    mode = Counter(value_list).most_common(1)[0][0]
    return (mean, median, mode)


(mean, median, mode) = calculate_staistics([10, 20, 20, 30])
print(STATS_FORMAT.format(mean=mean, median=median, mode=mode))
