# Hotel, menu. TableOrder List.
# 1. Hotel will have name, location, rating,
# 2. Hotel will have a menu.
# 3. Hotel Will have a list of Orders.
#
# Menu
# 1. It will have list of items
#
# Item:
# name, category, Cost
#
# Order:
# Table number
# time
# dictionaries of menu items with quantity

# calculate Price and display Invoice
# Menu will be in the file along with the hotel details.
# recommend an item in a category
from Order_ex3 import Order
from random import randint
class Hotel:
    def __init__(self,name,location, rating, menu):
        self._name = name
        self._location= location
        self._rating = rating
        self._menu = menu
        self._orders = {}

    def new_order(self):
        table_num = randint(1, 11)
        order = Order(table_num, self._menu)
        self._orders[order.get_id()] = order

    def add_item(self, order_id, item_id):
        order = self._orders[order_id]
        order.add_item(item_id)

    def generate_bill(self, order_id):
        order = self._orders[order_id]
        starters = order.filter_items('Starter')
        main_course = order.filter_items('Main Course')
        desserts = order.filter_items('Desserts')


        data = 'Bill Details\n\n Items Ordered \n\n'
        data += order.format_items(starters+main_course+ desserts)
        starters_total, main_course_total, desserts_total, total, discounted_total, tax_applicable, final_total = order.calculateTotals(
            starters, main_course, desserts)
        data += "\n\nTotal Bill Amount: "+ str(total)
        data += "\nDiscounted Total: "+ str(discounted_total)
        data += "\nTax: " + str(tax_applicable)
        data += "\nFinal Total: "+ str(final_total)
        return data


    def get_order_ids(self):
        return list(self._orders.keys())

    def get_order(self, order_id):

        return self._orders.get(order_id, None)

    def get_orders(self):
        return self._orders