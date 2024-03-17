
class BalanceException(Exception):
    def __init__(self):
        super().__init__('Not enough balance in the Account')

class AmountException(Exception):
    def __init__(self):
        super().__init__('The amount cannot be 0 or negative')



class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.__account_number = account_number
        self.__customer_name = customer_name
        if balance <= 0:
            raise AmountException()
        self.__balance = balance

    def deposit(self , amount):
        if amount <= 0:
            raise AmountException()
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            self.__balance -= amount
        else:
            raise BalanceException()
    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def __repr__(self):
        return f'{self.__account_number} {self.__customer_name} {self.__balance}'

    def __str__(self):
        return f'Acc_no: {self.__account_number} Name: {self.__customer_name} Balance: {self.__balance}'

class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance):
        super().__init__(account_number, customer_name, balance)
        self.__interest_rate = 7.6

    def add_interest(self):
        self.deposit(self.get_balance() * self.__interest_rate / 100)


class CheckingAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance):
        super().__init__(account_number, customer_name, balance)
        self.__min_balance = 200
        self.__fee = 10

    def withdraw(self, amount):
        self.set_balance(self.get_balance() - amount)
        if self.get_balance() < self.__min_balance:
            self.set_balance(self.get_balance() - self.__fee)