# Exercise 1: 
# Write a Line method called midpoint that computes the midpoint of a line segment and returns the result as a Point object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
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