
# Revisiting the __eq__ method
class Student:
    def __init__(self, id, name, age, marks):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def __hash__(self):
        # has method should return a hash of unique property
        return hash(self.__id)

    def __eq__(self, other):
        # we dont know if the other object is an object of current class.
        # we need to check of the oter is the object current class. On when this satisfies, we compare them
        if not isinstance(other, Student):
            return False
        return self.__marks == other.get_marks()


s1 = Student(1, "Max", 20, 99.9)
s2 = Student(2, "James", 20, 99.9)

print(s1 == s2)

class Item:
    def __init__(self, id, name, description, price):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price

    def get_price(self):
        return self.__price

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.__price == other.get_price()

item1 = Item(1, "PS5", "A gaming console", 400)
item2 = Item(2, "Acer Nitro G15", "A gaming laptop", 1300)

print(item1 == item2)


print(s1 == item1)

