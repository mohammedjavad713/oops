import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter the radius of the circle: "))

c = Circle(radius)

print("Area of the circle =", c.calculate_area())
print("Circumference of the circle =", c.calculate_circumference())

