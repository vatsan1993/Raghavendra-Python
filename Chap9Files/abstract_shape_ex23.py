from abc import ABC
import math
class Shape(ABC):
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"Color = {self.__color}"

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def __str__(self):
        return f'Radius = {self.__radius} {super().__str__()}'

    def area(self):
        return math.pi * math.pow(self.__radius, 2)

class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def __str__(self):
        return f'Length: {self.__length}, Width: {self.__width}, {super.__str__()}'

    def area(self):
        return self.__length  * self.__width



c1 = Circle(10, "Blue")
r1 = Rectangle(15, 10, "Red")

print(c1.area())
print(r1.area())