class Item:
    nextId = 1
    def __init__(self, name, category, price):
        self._id = Item.nextId
        Item.nextId += 1
        self._name = name
        self._category = category
        self._price = price

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def getCategory(self):
        return self._category

    def getPrice(self):
        return self._price

    def __str__(self):
        return (f'Item id: {self._id}, Name: {self._name}, Category:{self._category}, Price: ${self._price}')

    def __repr__(self):
        return (f'Item id: {self._id}, Name: {self._name}, Category:{self._category}, Price: ${self._price}')
