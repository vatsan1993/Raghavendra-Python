# IsSellableItem,PaymentMethod, shopping cart
from abc import ABC
class IsSellableItem:
    def __init__(self, id, name, description, price):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def calculate_discount(self, discount_rate):
        return self.__price - (self.__price * discount_rate / 100)

    def __str__(self):
        return f'Name = {self.__name}, Price: {self.__price} , discounted price: {self.calculate_discount(4)}'


class Electornics(IsSellableItem):
    def __init__(self,id, name, description, price, ram, storage, processor):
        super().__init__(id, name, description, price)
        self.__ram = ram
        self.__storage = storage
        self.__processor = processor

    def get_ram(self):
        return self.__ram

    def get_storage(self):
        return self.__storage

    def get_processor(self):
        return self.__processor

    def __str__(self):
        return super().__str__() + f'RAM: {self.__ram}, Storage: {self.__storage}, Processor: {self.__processor}'

class Document(IsSellableItem):
    def __init__(self,id, name, description, price, author, num_of_pages):
        super().__init__(id, name, description, price)
        self.__author = author
        self.__num_of_pages = num_of_pages

    def get_author(self):
        return self.__author
    def  get_num_of_pages(self):
        return self.__num_of_pages

    def __str__(self):
        return super().__str__() + f'Author: {self.__author}, Number of Pages: {self.__num_of_pages}'


class PaymentMethod(ABC):
    def pay(self):
        pass

class CardPayment(PaymentMethod):
    def __init__(self,owner_name, card_number, exp_date, cvv):
        self.__owner_name = owner_name
        self.__card_number= card_number
        self.__exp_date = exp_date
        self.__cvv = cvv

    def get_owner_name(self):
        return self.__owner_name

    def get_card_number(self):
        return self.__card_number

    def get_exp_date(self):
        return self.__exp_date

    def get_cvv(self):
        return self.__cvv

    def pay(self):
        print('Verifying card details.')
        print('Requesting a transfer from the associated bank')
        print('Money received')
        print('Transaction ended')


class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.__upi_id = upi_id

    def get_upi_id(self):
        return self.__upi_id

    def pay(self):
        print('Verifying UPI id')
        print('Connecting to UPI Server')
        print('Requesting money')
        print('UPI transfer complete')
        print('transaction ended')

class ShoppingCart:
    def __init__(self):
        self.__items = []
        self.__payment_method = None

    def add_item(self, item):
        if isinstance(item, IsSellableItem):
            self.__items.append(item)
        else:
            print("Please provide as sellable item")

    def add_payment_method(self, payment_method):
        if isinstance(payment_method, PaymentMethod):
            self.__payment_method = payment_method
        else:
            print("Only provide a payment method object to this.")

    def pay(self):
        if self.__payment_method:
            self.__payment_method.pay()
        else:
            print("No payment method exists. please add a payment method")


shopping_cart = ShoppingCart()
item1 = Electornics(1, "Lenovo Legion Pro", "A gaming laptop", 1200, "16GB", "1TB", "Intell i9")
item2 = Document(2, "Harry Potter 1", "Volume 1", 20, "J.K. Rowling", 700)

pay1 = CardPayment("max", 123435, "10/26", 123)
pay2 = UPI("max@abc")

shopping_cart.add_item(item1)
shopping_cart.add_item(item2)

shopping_cart.add_payment_method(pay1)
shopping_cart.pay()

shopping_cart2 = ShoppingCart()

shopping_cart2.add_item(item1)
shopping_cart2.add_item(item2)

shopping_cart2.add_payment_method(pay2)
print()

shopping_cart2.pay()