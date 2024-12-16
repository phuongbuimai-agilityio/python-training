# Exercise 1: Write a function called subtract_time that takes two Time objects
# and returns the interval between them in seconds -- assuming that they are two times during the same day.
class Time:
    """Represents a time of day"""


def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second

    return time


def time_to_int(time):
    """Convert a Time object to an integer number of seconds.

    Args:
        time: A Time object with attributes hour, minute, and second.

    Returns:
        int: The total number of seconds represented by the time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second

    return seconds


def subtract_time(t1, t2):
    """Compute the difference between two Time objects in seconds.

    Args:
        t1: First Time object
        t2: Second Time object to subtract from t1

    Returns:
        int: The difference in seconds between t1 and t2 (t1 - t2)

    Examples:
        >>> subtract_time(make_time(3, 2, 1), make_time(3, 2, 0))
        1
        >>> subtract_time(make_time(3, 2, 1), make_time(3, 0, 0))
        121
        >>> subtract_time(make_time(11, 12, 0), make_time(9, 40, 0))
        5520
    """
    interval_time = time_to_int(t1) - time_to_int(t2)

    return interval_time


print(subtract_time(make_time(3, 2, 1), make_time(3, 2, 0)))
print(subtract_time(make_time(3, 2, 1), make_time(3, 0, 0)))
print(subtract_time(make_time(11, 12, 0), make_time(9, 40, 0)))


# Exercise 2: Write a function called is_after that takes two Time objects
# and returns True if the first time is later in the day than the second, and False otherwise.
def is_after(t1, t2):
    """Check if one Time object represents a later time than another.

    Args:
        t1: First Time object to compare
        t2: Second Time object to compare

    Returns:
        bool: True if t1 occurs after t2, False otherwise

    Examples:
        >>> is_after(make_time(13, 30, 0), make_time(13, 29, 0))
        True
        >>> is_after(make_time(13, 30, 0), make_time(13, 31, 0))
        False
    """
    if time_to_int(t1) > time_to_int(t2):
        return True
    else:
        return False


print(is_after(make_time(3, 2, 1), make_time(3, 2, 0)))
print(is_after(make_time(3, 2, 1), make_time(3, 2, 1)))
print(is_after(make_time(11, 12, 0), make_time(9, 40, 0)))
