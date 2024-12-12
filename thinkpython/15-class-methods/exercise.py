# Exercise: 
# 1. Write a definition for a Date class that represents a date -- that is, a year, month, and day of the month.
# 2. Write an __init__ method that takes year, month, and day as parameters and assigns the parameters to attributes.
# Create an object that represents June 22, 1933.
# 3. Write __str__ method that uses an f-string to format the attributes and returns the result. 
# If you test it with the Date you created, the result should be 1933-06-22.
# 4. Write a method called is_after that takes two Date objects and returns True if the first comes after the second.
# Create a second object that represents September 17, 1933, and check whether it comes after the first object.

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    def is_after(self, other):
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