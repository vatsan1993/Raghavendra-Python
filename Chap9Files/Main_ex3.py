from Item_ex3 import Item
from Hotel_ex3 import  Hotel
from Menu_ex3 import Menu

class Main:
    def __init__(self):
        self._menu = Menu()
        self._hotel = Hotel("Hotel Taj", "New York",4.9, self._menu)
        self._ids = []

    def read_menu(self):
        with open('menu_ex3.csv') as menu_file:
            for line in menu_file:
                line=  line.strip()
                line = line.split(', ')
                item = Item(line[0], line[1],int(line[2]) )
                self._menu.add_item(item)

    def read_orders(self):
        with open('orders_ex3.csv') as menu_file:
            order_id = 0
            for line in menu_file:
                line = line.strip()
                line = line.split(',')

                self._hotel.new_order()

                order_id+=1
                self._ids.append(order_id)
                for item_id in line:
                    item_id = int(item_id)
                    self._hotel.add_item(order_id, item_id )


    def display_menu(self):
        for item in self._menu.get_items():
            print(item)

    def display_order_ids(self):
        for order in self._hotel.get_order_ids():
            print(order)

    def display_order (self, order_id):
        order = self._hotel.get_order(order_id)
        print(order)

    def generate_bill(self, order_id):
        bill = self._hotel.generate_bill(order_id)
        print(bill)

    def generate_all_bills(self):
        for id in self._ids:
            self.generate_bill(id)
            print()

app = Main()
app.read_menu()
app.read_orders()


app.generate_all_bills()