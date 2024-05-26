# Geometric Shape, Rectangle, ellipse, Square , circle
import math
class GeometricShape:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"Shape: {self.__name}"


class Rectangle(GeometricShape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
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


    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 *(self.__width + self.__length)

    def __str__(self):
        return super().__str__() + f' Length: {self.__length}, width: {self.__width}'


class Ellipse(GeometricShape):
    def __init__(self, semi_major_axis, semi_minor_axis):
        super().__init__("Ellipse")
        self.__semi_major_axis = semi_major_axis
        self.__semi_minor_axis = semi_minor_axis

    def get_semi_major_axis(self):
        return self.__semi_major_axis

    def set_semi_major_axis(self, semi_major_axis):
        self.__semi_major_axis= semi_major_axis

    def get_semi_minor_axis(self):
        return self.__semi_minor_axis

    def set_semi_minor_axis(self, semi_minor_axis):
        self.__semi_minor_axis = semi_minor_axis


    def get_area(self):
        return math.pi * self.__semi_minor_axis * self.__semi_minor_axis

    def get_perimeter(self):
        major_axis_squared = self.__semi_major_axis ** 2
        minor_axis_squared = self.__semi_minor_axis ** 2
        return 2 * math.pi * math.sqrt((major_axis_squared + minor_axis_squared)/2)

    def __str__(self):
        return super().__str__() + f' Semi Major Axis = {self.__semi_minor_axis}, Semi Minor Axis = {self.__semi_minor_axis}'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.set_name("Square")


class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.set_name("Circle")


class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.__height = height
        self.set_name("Cuboid")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        # we are overriding the get_area method to have different formula
        return (2 * self.get_length() * self.get_width() +
                2 * self.get_width() * self.get_height() +
                2 * self.get_height() * self.get_length())

    def get_perimeter(self):
        # we are overriding the get_perimeter method to have different formula
        return 4 * (self.get_length() + self.get_width() + self.get_height())

    def get_volume(self):
        return self.get_length() * self.get_width() * self.get_height()

    def __str__(self):
        return super().__str__() + f' height: {self.__height}'

class Cube(Cuboid):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.set_name("Cube")


rectangle = Rectangle(10, 5)
print(rectangle)
print(f'Area: {rectangle.get_area()}')
print(f'Perimeter: {rectangle.get_perimeter()}')


print()
ellipse = Ellipse(10, 3)
print(ellipse)
print(f'Area: {ellipse.get_area()}')
print(f'Perimeter: {ellipse.get_perimeter()}')

print()
square = Square(10)
print(square)
print(f'Area: {square.get_area()}')
print(f'Perimeter: {square.get_perimeter()}')

print()
circle = Circle(10)
print(circle)
print(f'Area: {circle.get_area()}')
print(f'Perimeter: {circle.get_perimeter()}')

print()
cuboid = Cuboid(10, 7 ,3)
print(cuboid)
print(f'Area: {cuboid.get_area()}')
print(f'Perimeter: {cuboid.get_perimeter()}')
print(f'Volume: {cuboid.get_volume()}')

print()
cube = Cube(10)
print(cube)
print(f'Area: {cube.get_area()}')
print(f'Perimeter: {cube.get_perimeter()}')
print(f'Volume: {cube.get_volume()}')
