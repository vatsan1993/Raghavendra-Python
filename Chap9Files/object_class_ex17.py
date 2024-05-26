class Student(object):
    def __init__(self, id, name, age, marks):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        if isinstance(other , Student):
            return self.__marks == other.get_marks()
        else:
            return False
    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}, Marks: {self.__marks}'

print(dir(Student)) # describes all properties and methods of a class or an object or a simple value.

s1 = Student(1, "Max", 20, 99.9)
s2 = Student(2, "James", 20, 99.9)
print(s1 == s2)

print(s1.__dict__)
print(s2.__dict__)

print(s1.__class__.__name__)
print(s2.__class__.__name__)


class SalesData :
    def __init__(self , sales = []):
        self.__sales = sales

    def get_sales(self):
        return self.__sales


    def add_sale(self, sale):
        self.__sales.append(sale)

    def __add__(self, other):
        if isinstance(other, SalesData):
            return SalesData(self.__sales + other.get_sales())
        return SalesData(self.__sales)
    def __str__(self):
        return str(self.__sales)



sales1 = SalesData([25,4,6,45])
sales1.add_sale(5)
sales1.add_sale(7)

sales2 = SalesData([25,6,3,4,6,4])
sales2.add_sale(4)
sales2.add_sale(7)

merged_sales = sales1 + sales2
print(merged_sales)


print(s1 == sales1)


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.__width + other.get_width(), self.__height + other.get_height())
        return Rectangle(self.__width , self.__height )
    def __sub__(self, other):
        if isinstance(other, Rectangle):
            width = abs(self.__width - other.get_width())
            height = abs(self.__height + other.get_height())
            return Rectangle(width, height)
        return Rectangle(self.__width, self.__height)

    def get_area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'Width : {self.__width}, height: {self.__height} , area: {self.get_area()}'



r1 = Rectangle(10, 4)
r2 = Rectangle(5, 3)
print(r1)
print(r2)
r3 = r1 + r2
print(r3)
r4 = r1 - r2
print(r4)



class Book:
    def __init__(self, id,  name, author, price):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__price = price

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_autor(self):
        return self.__author

    def get_price(self):
        return self.__price

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, keyword):
        if isinstance(keyword, str):
            return self.__name == keyword
        if isinstance(keyword, int):
            return self.__id == keyword
        return False

    def __str__(self):
        return f'id: {self.__id} name: {self.__name} Author: {self.__author} Price: {self.__price}'


class Inventory:
    def __init__(self, inventory = {}):
        self.__inventory = inventory

    def add_book(self, book, quantity):
        for existing_book, existing_quantity in self.__inventory.items():
            if existing_book == book.get_name():
                self.__inventory[book] += quantity
        self.__inventory[book] = quantity

    def __contains__(self, keyword):
        for existing_book, existing_quantity in self.__inventory.items():
            if existing_book == keyword:
                return True
        return False


