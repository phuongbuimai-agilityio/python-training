import math


# Example 1: Always use self or a @classmethod when referring to a class's attributes
class Blog:
    __tablename__ = "blog"

    def table_name(self):
        return Blog.__tablename__  # Hardcoding parent here is problematic


class DerivedBlog(Blog):
    __tablename__ = "derived_blog"


b = DerivedBlog()
print(b.table_name())
# result: 'blog' => the result should be 'derived_blog'
# but it's not because the class name used directly in the method table_name
# Solution:


class Blog:
    __tablename__ = "blog"

    def table_name(self):
        return self.__tablename__

    @classmethod
    def other_table_name(cls):
        return cls.__tablename__


class DerivedBlog(Blog):
    __tablename__ = "derived_blog"


b = DerivedBlog()
print(b.table_name())  # result: 'derived_blog'


# Example 2: Use the isinstance() function to determine the type of an object
def get_size(some_object: any) -> int:
    """
    Calculate size of an object based on its type.

    Args:
        some_object (Any): The object to measure, can be list, dict, str, tuple, bool, None, int, or float

    Returns:
        int: The size of the object where:
            - For sequences (list, dict, str, tuple): returns length
            - For bool and None: returns 1
            - For numbers (int, float): returns integer value
    """
    if isinstance(some_object, (list, dict, str, tuple)):
        return len(some_object)
    elif isinstance(some_object, (bool, type(None))):
        return 1
    elif isinstance(some_object, (int, float)):
        return int(some_object)


print(get_size("hello"))
print(get_size([1, 2, 3, 4, 5]))
print(get_size(10.0))


# Example 3: Use leading underscores in function and variable names to denote private data
class Foo:
    def __init__(self):
        """Since 'id' is of vital importance to us, we don't
        want a derived class accidentally overwriting it. We'll
        prepend with double underscores to introduce name
        mangling.
        """
        self.__id = 8
        self.value = self.__get_value()  # Our 'private copy'

    def get_value(self):
        pass

    def should_destroy_earth(self):
        return self.__id == 42

    # Here, we're storing a 'private copy' of get_value,
    # and assigning it to '__get_value'. Even if a derived
    # class overrides get_value in a way incompatible with
    # ours, we're fine
    __get_value = get_value


class Baz(Foo):
    def get_value(self, some_new_parameter):
        pass


class Qux(Foo):
    def __init__(self):
        """Now when we set 'id' to 42, it's not the same 'id'
        that 'should_destroy_earth' is concerned with. In fact,
        if you inspect a Qux object, you'll find it doesn't
        have an __id attribute. So we can't mistakenly change
        Foo's __id attribute even if we wanted to.
        """
        self.id = 42
        # No relation to Foo's id, purely coincidental
        super(Qux, self).__init__()


q = Qux()
b = Baz()  # Works fine now
print(q.should_destroy_earth())  # returns False
print(q.id == 42)  # returns True

# Example 4: Use properties to "future-proof" your class implementation


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Internal storage (private attribute)

    @property
    def radius(self):
        """The radius of the circle."""
        return self._radius

    @radius.setter  # The @radius.setter ensures that radius remains positive
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def diameter(self):
        """The diameter of the circle."""
        return self._radius * 2

    @property
    def area(self):
        """The area of the circle."""
        return math.pi * (self._radius**2)


# Usage
circle = Circle(5)
print(circle.radius)  # Output: 5
# New attributes like diameter and area are added
# as computed properties without altering the class’s interface.
print(circle.diameter)  # Output: 10
print(circle.area)  # Output: 78.53981633974483

circle.radius = 10
print(circle.area)  # Output: 314.1592653589793

# Example 5: Use the __repr__ for a machine-readable representation of a class

# Example 6: Use the __str__ in a class to show a human-readable representation
