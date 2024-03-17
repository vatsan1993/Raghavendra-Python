# petshelter food calculator- Animal , Dog , Cat, Ginnie pig . feed() – poly morphism python
# Here per shelter also needs to have a few items like food, medicines, cages
# so we modify the pet_shelter so we can create a item object and add it to the pet_shelter object
# but we will see what happens if we add item as a pet.

class PetFoodQuantityException(Exception):
    pass



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
        self.__inventory = {}
        self.__expenditure = 0

    def add_pet(self, pet):
        self.__pets.append(pet)

    def add_item(self, item_name, quantity):
        self.__inventory[item_name] = self.__inventory.get(item_name, 0) +quantity

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
            # using polymorphism
            food_needed += pet.calculate_food()
        if food_needed > self.__inventory.get('pet_food', 0):
            raise PetFoodQuantityException("Not Enough Food available. Restock the inventory")
        else:
            self.__inventory['pet_food'] -= food_needed
            return food_needed

    def add_item(self, item, quantity, price):
        self.__inventory[item] = quantity
        self.__expenditure += price

    def use_item(self, id):
        for item, quantity in enumerate(self.__inventory):
            if item.get_id() == id:
                if quantity >0:
                   self.__inventory[item] = quantity - 1
                break
    def get_expenditure(self):
        return self.__expenditure

    def get_food_remaining(self):
        return self.__inventory.get('pet_food', 0)

    def __str__(self):
        output = 'Pets\n'
        for pet in self.__pets:
            output += '\t' + str(pet) + '\n'
        output += 'Inventory\n'
        for item,quantity in self.__inventory.items():
            output += f'\t {item} : {quantity}\n'

        output += f'Expenditure : ${self.__expenditure} '
        return output




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



pet_shelter.add_item('Laptop', 1, 1500)
pet_shelter.add_item('pet_food', 10, 550)

print(pet_shelter)

print(pet_shelter.feed_pets())
print(pet_shelter.get_food_remaining())


# print(pet_shelter.feed_pets()) # error as there is not enough food available.

pet_shelter.remove_pet(1)
print(pet_shelter)




