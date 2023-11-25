from Item_ex3 import  Item
from random import  choice

class Menu:
    def __init__(self):
        self._menu_items = []

    def add_item(self, item):
        self._menu_items.append(item)

    def get_item_recommendation(self, category):
        category_items = [item for item in self._menu_items if item.getCategory() == category]
        random_item = choice(category_items)
        return random_item
    # @staticmethod
    #

    def get_item(self, item_id):

        # def filter_item(item ):
        #     print(item)
        #     print(item.getId() == item_id)
        #     return  item.getId() == item_id
        matched_items = filter(lambda x : x.getId() == item_id, self._menu_items)
        # matched_items =  filter(filter_item, self._menu_items)
        data = list(matched_items)
        if(len(data)> 0):
            return data[0]
        else:
            return None

    def get_items(self):
        return self._menu_items

    def __str__(self):
        string = 'Menu\n'
        for item in self._menu_items:
            string += str(item)+'\n'
        return string

