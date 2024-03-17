class Animal:
    def __init__(self, name, fav_food):
        self.__name = name
        self.__fav_food = fav_food

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_fav_food(self):
        return self.__fav_food

    def set_fav_food(self, fav_food):
        self.__fav_food = fav_food

    def __str__(self):
        return f'Name: {self.__name} Fav Food: {self.__fav_food}'

    # can also write repr

class Dog(Animal):
    def __init__(self, name, fav_food, friendly):
        super().__init__(name, fav_food)
        self.__friendly = friendly

    def get_friendly(self):
        return self.__friendly

    def set_friendly(self, friendly):
        self.__friendly = friendly

    def __str__(self):
        return super().__str__() + f' Friendly: {self.__friendly}'



class Cat(Animal):
    def __init__(self, name, fav_food, sleep_time):
        super().__init__(name, fav_food)
        self.__sleep_time = sleep_time

    def get_sleep_time(self):
        return self.__sleep_time

    def set_sleep_time(self, sleep_time):
        self.__sleep_time = sleep_time

    def __str__(self):
        return super().__str__() + f' Sleep Time: {self.__sleep_time} hours'



class Pig(Animal):
    def __init__(self, name, fav_food, intelligence):
        super().__init__(name, fav_food)
        self.__intelligence = intelligence

    def get_intelligence(self):
        return self.__intelligence

    def set_intelligence(self, intelligence):
        self.__intelligence = intelligence

    def __str__(self):
        return super().__str__() + f' intelligence: {self.__intelligence}'


d1 = Dog("Max", "Chicken", True)
c1 = Cat("Snowball", "fish", 3)
p1 = Pig("John", "Apple", 2)
print(d1.get_name())
print(c1.get_name())
print(p1.get_name())