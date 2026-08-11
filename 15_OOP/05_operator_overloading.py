class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2
p = p1 + p2 # We overloaded the + Operator by writing __add__ function
p.print_point()