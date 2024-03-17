# petshelter food calculator- Animal , Dog , Cat, Ginnie pig . feed() – poly morphism python

class Animal:
    def __init__(self, id, name, height, weight):
        self.__id = id
        self.__name = name
        self.__height = height
        self.__weight = weight

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f'id: {self.__id}, Name: {self.__name}, Height: {self.__height}, weight: {self.__weight}'

    def __repr__(self):
        return f'{self.__id}, {self.__name}, {self.__height}, {self.__weight}'

class Dog(Animal):
    def __init__(self, id, name, height, weight, food_percent):
        super().__init__(id, name, height, weight)
        self.__food_percent = food_percent

    def calculate_food(self):
        return self.get_height() * self.get_weight() * self.__food_percent/100


class Cat(Animal):
    def __init__(self,id, name, height, weight, feeding_count):
        super().__init__(id, name, height, weight)
        self.__feeding_count = feeding_count

    def calculate_food(self):
        return (self.get_height() * self.get_weight() * 1 / 100) * self.__feeding_count

class GinniePig(Animal):
    def __init__(self,id, name, height, weight):
        super().__init__(id, name, height, weight)

    def calculate_food(self):
        return self.get_height() * self.get_weight() * 1 / 100

class PetShelter:
    def __init__(self):
        self.__pets = []

    def add_pet(self, pet):
        self.__pets.append(pet)

    def remove_pet(self, id):
        index = -1
        for i, pet in enumerate(self.__pets):
            if pet.get_id() == id:
                index = i
                break

        if index != -1:
            self.__pets.pop(index)

    def feed_pets(self):
        food_needed = 0
        for pet in self.__pets:
            food_needed += pet.calculate_food()
        return food_needed


d1 = Dog(1,"Max", 10, 20,3)
d2 = Dog(2, "Fluffy", 5, 15, 2)
c1 = Cat(3, "Snowball", 2, 10, 5)
c2 = Cat(4, "Alice", 1.5, 8, 3)
g1 = GinniePig(5, "Max", 0.2, 3)
g2 = GinniePig(6, "Flash", 0.1, 1.5)

pet_shelter = PetShelter()

pet_shelter.add_pet(d1)
pet_shelter.add_pet(d2)
pet_shelter.add_pet(c1)
pet_shelter.add_pet(c2)
pet_shelter.add_pet(g1)
pet_shelter.add_pet(g2)



print(pet_shelter.feed_pets())

pet_shelter.remove_pet(1)
print(pet_shelter.feed_pets())


