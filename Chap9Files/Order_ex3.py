from datetime import datetime
from functools import reduce


class Order:
    nextId = 1

    def __init__(self, table_num, menu):
        self._order_id = Order.nextId
        self._table_num = table_num
        Order.nextId += 1
        self._ordered_items = {}
        self._time_of_order = datetime.now()
        self._menu = menu
        self._tax_percentage = 5
        self._discount_rate = 2

    def get_id(self):
        return self._order_id

    def get_table_num(self):
        return self._table_num

    def get_time_of_order(self):
        return self._time_of_order

    def get_tax_percentage(self):
        return self._tax_percentage

    def get_discount_rate(self):
        return self._discount_rate

    def set_tax_percentage(self, tax_percentage):
        self._tax_percentage = tax_percentage

    def set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    def add_item(self, item_id):
        self._ordered_items[item_id] = self._ordered_items.get(item_id, 0) + 1

    def get_item(self, item_id):
        return self._menu.get_item(item_id)

    def caculate_total(self, items):
        def total(a, item):
            if item != None:
                return a + (item.getPrice() * self._ordered_items[item.getId()])
            else:
                return a + 0

        result = reduce(total, list(items), 0)

        return result

    def calculateTotals(self, starters, main_course, desserts):
        starters_total = self.caculate_total(starters)
        main_course_total = self.caculate_total(main_course)
        desserts_total = self.caculate_total(desserts)

        total = starters_total + main_course_total + desserts_total
        discounted_total = total - (total * self._discount_rate) / 100
        tax_applicable = discounted_total * self._tax_percentage / 100
        final_total = discounted_total + tax_applicable
        return [starters_total, main_course_total, desserts_total, total, discounted_total, tax_applicable, final_total]

    def filter_items(self, item_type=None):
        if item_type == None:
            return self._ordered_items
        data = [self.get_item(item_id) for item_id in self._ordered_items.keys() if
                self._menu.get_item(item_id).getCategory() == item_type]
        return data

    def format_items(self, items):
        result = ''
        for item in items:
            quantity = self._ordered_items[item.getId()]
            price = item.getPrice()
            total = quantity * price
            result += "{:20}{:2d} x {:3.2f} ={:4.2f}\n".format(item.getName(), quantity, price, total)

            # result+=f'{item.getName()} {self._ordered_items[item.getId()]} x {item.getPrice()} = {self._ordered_items[item.getId()] * item.getPrice()}\n'
        return result

    def __str__(self):
        string = f'Table No: {self._table_num}\n Time: {self._time_of_order}\n'
        # starters = [self._menu.get_item(item_id) for item_id in self._orders if self._menu.get_item(item_id).getCategory() =="starter"]
        # main_course = [self._menu.get_item(item_id) for item_id in self._orders if self._menu.get_item(item_id).getCategory() =="main_course"]
        # desserts = [self._menu.get_item(item_id) for item_id in self._orders if self._menu.get_item(item_id).getCategory() =="desserts"]
        starters = self.filter_items('Starter')
        main_course = self.filter_items('Main Course')
        desserts = self.filter_items('Desserts')
        starters_total, main_course_total, desserts_total, total, discounted_total, tax_applicable, final_total = self.calculateTotals(
            starters, main_course, desserts)
        string += '\nStarters\n'
        string += self.format_items(starters)
        string += f"\n\nStarters Total:{starters_total}"

        string += '\nMain Course\n'
        string += self.format_items(main_course)
        string += f"\n\nMain Course Total:{main_course_total}"

        string += '\nDesserts\n'
        string += self.format_items(desserts)
        string += f"\n\nDesserts Total:{desserts_total}"

        string += f'\nTotal: {total}\nDiscounted Total: {discounted_total}\nTax Applicable: {tax_applicable}\nAmount Payable:{final_total}'
        return string
