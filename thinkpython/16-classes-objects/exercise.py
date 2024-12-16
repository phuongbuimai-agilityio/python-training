# Exercise 1:
# Write a Line method called midpoint that computes the midpoint of a line segment and returns the result as a Point object
class Point:
    """A class representing a point in 2D space.

    Attributes:
        x (float): The x-coordinate
        y (float): The y-coordinate
    """

    def __init__(self, x, y):
        """Initialize a Point with x and y coordinates.

        Args:
            x (float): The x-coordinate
            y (float): The y-coordinate
        """
        self.x = x
        self.y = y


class Line:
    """A class representing a line segment defined by two points.

    Attributes:
        p1 (Point): The first endpoint of the line
        p2 (Point): The second endpoint of the line
    """

    def __init__(self, p1, p2):
        """Initialize a Line with two endpoints.

        Args:
            p1 (Point): The first endpoint
            p2 (Point): The second endpoint
        """
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        """Calculate the midpoint of the line segment.

        Returns:
            Point: A new Point object representing the midpoint of the line

        Examples:
            >>> p1 = Point(0, 0)
            >>> p2 = Point(4, 4)
            >>> line = Line(p1, p2)
            >>> mid = line.midpoint()
            >>> mid.x, mid.y
            (2.0, 2.0)
        """
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return Point(mid_x, mid_y)


start = Point(0, 0)
end1 = Point(300, 0)
end2 = Point(0, 150)
line1 = Line(start, end1)
line2 = Line(start, end2)

mid1 = line1.midpoint()
print(mid1)

mid2 = line2.midpoint()
print(mid2)

line3 = Line(mid1, mid2)
print(line3)
