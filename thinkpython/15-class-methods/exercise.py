# Exercise:
# 1. Write a definition for a Date class that represents a date -- that is, a year, month, and day of the month.
# 2. Write an __init__ method that takes year, month, and day as parameters and assigns the parameters to attributes.
# Create an object that represents June 22, 1933.
# 3. Write __str__ method that uses an f-string to format the attributes and returns the result.
# If you test it with the Date you created, the result should be 1933-06-22.
# 4. Write a method called is_after that takes two Date objects and returns True if the first comes after the second.
# Create a second object that represents September 17, 1933, and check whether it comes after the first object.


class Date:
    """A class representing a calendar date.

    This class provides functionality to create and compare dates.

    Attributes:
        year (int): The year of the date
        month (int): The month of the date (1-12)
        day (int): The day of the date (1-31)
    """

    def __init__(self, year: int, month: int, day: int):
        """Initialize a new Date object.

        Args:
            year (int): The year
            month (int): The month (1-12)
            day (int): The day of the month (1-31)
        Raises:
            ValueError: If the provided year, month, or day is invalid.
        """
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= day <= self.days_in_month(year, month)):
            raise ValueError(
                f"Day must be valid for the month and year provided: {year}-{month}."
            )
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        """Convert the date to a string in ISO format (YYYY-MM-DD).

        Returns:
            str: The date formatted as YYYY-MM-DD
        """
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        """Return the number of days in a given month, accounting for leap years.

        Notes:
            - This function is static, so it can be called without an instance of the class.
            - It takes two parameters: year and month.
            - It returns an integer representing the number of days in the month.
            - It used as an utility method

        Args:
            year (int): The year
            month (int): The month (1-12)

        Returns:
            int: The number of days in the month
        """
        if month in {1, 3, 5, 7, 8, 10, 12}:  # Months with 31 days
            return 31
        elif month in {4, 6, 9, 11}:  # Months with 30 days
            return 30
        elif month == 2:  # February
            return 29 if Date.is_leap_year(year) else 28
        raise ValueError("Invalid month.")

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Check if a year is a leap year.

        Args:
            year (int): The year to check.

        Returns:
            bool: True if the year is a leap year, False otherwise.

        Notes:
            - It used as an utility method
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __eq__(self, other) -> bool:
        """Check if two dates are equal."""
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    # In this exercise, I will use 2 methods to compare dates are:
    # 1. __lt__ method
    # 2. is_after method
    # These methods are used to compare dates, whether one date is earlier than another date
    def __lt__(self, other) -> bool:
        """Check if this date is earlier than another date."""
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def is_after(self, other):
        """Check if this date comes after another date.

        Args:
            other (Date): Another Date object to compare with

        Returns:
            bool: True if this date is later than the other date, False otherwise

        Examples:
            >>> date1 = Date(2023, 12, 1)
            >>> date2 = Date(2024, 1, 1)
            >>> date2.is_after(date1)
            True
        """
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                return self.day > other.day
        return False


# Create two Date objects
date1 = Date(1933, 6, 22)
date2 = Date(1933, 7, 10)

# Print the dates
print(date1)
print(date2)

# Check whether date 2 comes after date 1
print(date2.is_after(date1))

# Compare dates
print(date2 > date1)  # Output: True
print(date1 == date2)  # Output: False
print(date1 < date2)  # Output: True
