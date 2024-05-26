from abc import ABC

class Item(ABC):
    def add_more(self, quantity):
        pass

    def use(self):
        pass

    def is_edible(self):
        pass

    def is_poisonous(self):
        pass

    def use_for_cooking(self):
        pass
    def use_for_crafting(self):
        pass
    def selling_price(self):
        pass

class Edible(Item):
    def __init__(self ):
        self.__quantity = 1
    def add_more(self):
        self.__quantity += 1

    def use(self):
        if self.__quantity  != 0:
            self.__quantity -= 1
            return 50
        else: return False
    def is_edible(self):
        return True

    def is_poisonous(self):
        return False

    def use_for_cooking(self):
        self.__quantity -= 1
    def use_for_crafting(self):
        return False

    def selling_price(self):
        return 10

    def get_quantity(self):
        return self.__quantity


class PoisonousItem(Item):
    def __init__(self):
        self.__quantity = 1

    def add_more(self):
        self.__quantity += 1

    def use(self):
        if self.__quantity != 0:
            self.__quantity -= 1
            return -20
        else:
            return False


    def is_edible(self):
        return True

    def is_poisonous(self):
        return False

    def use_for_cooking(self):
        return False

    def use_for_crafting(self):
        if self.__quantity != 0:
            self.__quantity -= 1
            return True
        else:
            return False

    def selling_price(self):
        return 5

    def get_quantity(self):
        return self.__quantity


class BuildingMaterial(Item):
    def __init__(self):
        self.__quantity = 1

    def add_more(self):
        self.__quantity += 1

    def use(self):
        return 0

    def is_edible(self):
        return False

    def is_poisonous(self):
        return False

    def use_for_cooking(self):
        return False

    def use_for_crafting(self):
        if self.__quantity != 0:
            self.__quantity -= 1
            return True
        else:
            return False
    def selling_price(self):
        return 20

    def get_quantity(self):
        return self.__quantity



class Apple(Edible):
    def selling_price(self):
        return super().selling_price() + 10

class Burger(Edible):
    def selling_price(self):
        return super().selling_price() + 20

class PoisonousMushroom(PoisonousItem):
    def selling_price(self):
        return super().selling_price() + 2

class Sap(PoisonousItem):
    def selling_price(self):
        return super().selling_price() + 10

class Wood(BuildingMaterial):
    def selling_price(self):
        return super().selling_price() + 10


class Rock(BuildingMaterial):
    def selling_price(self):
        return super().selling_price() + 20

class Iron(BuildingMaterial):
    def selling_price(self):
        return super().selling_price() + 30


class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item_name):
        item = self.search_item(item_name)
        if item:
            item.add_more()
        else:
            pass


    def use_item(self, item, quantity):
        if item.get_quantity() >= quantity:
            for count in range(quantity):
                item.use()
            return True
        else:
            return False

    def search_item(self, item_name):
        for item in self.__items:
            if item.__class__.__name__.lower() == item_name.lower():
                return item
        return None

inventory = Inventory()


item_classes = {
    "Apple": Apple,
    "Burger":Burger,
    "PoisonousMushroom":PoisonousMushroom,
    "Sap":Sap,
    "Wood":Wood,
    "Iron":Iron,
    "Rock":Rock
}

ItemClass = item_classes.get("Apple")

item = ItemClass()
print(item.__class__.__name__)


