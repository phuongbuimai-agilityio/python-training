from typing import TypeVar, List


T = TypeVar("T")  # T is a placeholder for any type


def get_first_element(elements: List[T]) -> T:
    return elements[0]


def get_last_element(elements: List[T]) -> T:
    return elements[-1]


print(get_first_element([1, 2, 3]))
print(get_last_element([1, 2, 3]))
