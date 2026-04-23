class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius   
object1 = Circle(5)
print("Area of the circle:", object1.area())
print("Perimeter of the circle:", object1.perimeter())
