# petshelter food calculator- Animal , Dog , Cat, Ginnie pig . feed() – poly morphism python
# Here per shelter also needs to have a few items like food, medicines, cages
# so we modify the pet_shelter so we can create a item object and add it to the pet_shelter object
# but we will see what happens if we add item as a pet.

class PetFoodQuantityException(Exception):
    def __init__(self):
        super.__init__("Insufficient pet food")

class ItemQuantityException(Exception):
    def __init__(self):
        super.__init__("Insufficient Item to sell")

class InvalidArgumentException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ItemNotFoundException(Exception):
    def __init__(self):
        super().__init__("Item was not found")

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
        if isinstance(pet, Animal):
            self.__pets.append(pet)
        else:
            raise InvalidArgumentException("Invalid pet provided")
    def add_item(self, item_name, quantity):
        if type(item_name) == str and type(quantity) == int:
            self.__inventory[item_name] = self.__inventory.get(item_name, 0) +quantity
        else:
            raise InvalidArgumentException("item name and quantity are invalid ")

    def remove_pet(self, id):
        if type(id) == int:
            index = -1
            for i, pet in enumerate(self.__pets):
                if pet.get_id() == id:
                    index = i
                    break

            if index != -1:
                self.__pets.pop(index)
        else:
            raise InvalidArgumentException('invalid id to remove a pet')

    def feed_pets(self):
        food_needed = 0
        for pet in self.__pets:
            # using polymorphism
            food_needed += pet.calculate_food()
        if food_needed > self.__inventory.get('pet_food', 0):
            raise PetFoodQuantityException()
        else:
            self.__inventory['pet_food'] -= food_needed
            return food_needed

    def add_item(self, item, quantity, price):
        if type(item) == str and type(quantity) == int and (type(price) == float or type(price) == int):
            self.__inventory[item] = quantity
            self.__expenditure += price
        else:
            raise InvalidArgumentException('item or quantity or price is invalid.')

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


class Item:
    def __init__(self, name, category, price, quantity):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity

    def increase_quantity(self, quantity):
        self.__quantity += quantity

    def sell_item(self, quanity):
        if quanity > self.__quantity:
            raise ItemQuantityException()
        else:
            self.__quantity -= quanity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_name(self):
        return self.__name


    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f'Name: {self.__name}, Category:{self.__category}, Price: ${self.__price}, Quantity: {self.__quantity}')

    def __repr__(self):
        return (f'Name: {self.__name}, Category:{self.__category}, Price: ${self.__price}, Quantity: {self.__quantity}')

class PetShop:
    def __init__(self):
        self.__items = {}

    def add_item(self, item):
        # isinstance works on object types.
        if isinstance(item, Item):
            name = item.get_name()
            found_item = self.__items.get(name)
            if found_item == None:
                self.__items[name] = item
            else:
                found_item.increase_quanity(item.get_quantity())
        else:
            raise InvalidArgumentException("item for the item shop is invalid")

    def sell_item(self, name, quantity):
        if type(name) == str and type(quantity) == int:
            item = self.__items.get(name)
            if item == None:
                raise ItemNotFoundException()
            else:
                try:
                    item.sell_item(quantity)
                except ItemQuantityException as e:
                    print(e)
                else:
                    return item.get_price() * quantity
        else:
            raise InvalidArgumentException("name and quantity might be invalid values")
    def __str__(self):
        output = ''
        for name, item in self.__items.items():
            output += f'name : {name}, Price: {item.get_price}, quantity: {item.get_quanity()} '
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

pet_shelter.add_pet("cat")


