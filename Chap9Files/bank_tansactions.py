# this can be built using dictionaries or by using composition
from datetime import datetime
from functools import cmp_to_key
class Transaction:
    def __init__(self, transaction_id, transaction_type, transaction_date, amount, status, receiver = None ):
        self._transaction_id = transaction_id
        self._transaction_type = transaction_type
        self._amount = amount
        self._receiver = receiver
        self._transaction_date = transaction_date
        self._status = status

    def get_id (self):
        return self._transaction_id

    def get_amount(self):
        return self._amount

    def get_status(self):
        return self._status

    def get_type(self):
        return self._transaction_type

    def __str__(self):
        return (f'Transaction id: {self._transaction_id} , Type: {self._transaction_type},Amount: {self._amount}, '
                f'Status: {self._status}, date: {self._transaction_date} Receiver: {self._receiver} ')

class BankAccount:
    def __init__(self, acc_id, name, age):
        self._acc_id = acc_id
        self._name = name
        self._age = age
        self._transactions = []

    def add_transaction(self, transaction_id, transaction_type, transaction_date, amount , receiver = None):
        if transaction_type == 'deposit':
            self._transactions.append(Transaction(transaction_id, transaction_type, transaction_date, amount, 'success', None))
        else:
            bal = self.get_balance()
            if bal > amount:
                self._transactions.append(Transaction(transaction_id, transaction_type, transaction_date, amount, 'success', receiver))
            else:
                self._transactions.append(Transaction(transaction_id, transaction_type,  transaction_date, amount, 'failure', receiver))

    def get_name(self):
        return self._name

    def get_balance(self):
        total_balance = 0
        for transaction in self._transactions:
            if transaction.get_status() == 'success':
                if transaction.get_type() == 'deposit':
                    total_balance += transaction.get_amount()
                else:
                    total_balance -= transaction.get_amount()
        return total_balance

    def sort_transactions(self):
        def sort_helper(transaction1, transaction2):
            if transaction1.get_status() == 'failure' and transaction2.get_status() == 'failure':
                return 0
            elif transaction1.get_status() == 'failure':
                return -1
            elif transaction2.get_status() == 'failure':
                return 1
            elif transaction1.get_amount() > transaction2.get_amount():
                return 1
            elif transaction2.get_amount() > transaction1.get_amount():
                return -1
            else:
                return 0

        # sorted_transactions = sorted(self._transactions, key=lambda transaction: transaction.get_amount(), reverse=True)
        sorted_transactions = sorted(self._transactions, key=cmp_to_key(sort_helper), reverse = True)
        return sorted_transactions

    def __str__(self):
        result = f'Account id: {self._acc_id} Account Holder: {self._name} Age: {self._age}'
        for transaction in self._transactions:
            result += "\n\t" + str(transaction)
        return result + '\n'


d1 = datetime(2023, 1, 1)
d2 = datetime(2023, 2, 1)
d3 = datetime(2023, 3, 1)
d4 = datetime(2023, 4, 1)

account = BankAccount("AB1234", "Max Winchester", 35)
account.add_transaction(1, "deposit",d1, 500)
account.add_transaction(2, "deposit",d2, 500)
account.add_transaction(3, "deposit", d3, 2500)
account.add_transaction(4, "withdrawl",d4, 200, "self")
account.add_transaction(5, "transfer",d4, 200, "AB2234")
account.add_transaction(6, "transfer",d4, 5000, "AB2234")
print(account)

print("\n Sorted Transactions")
sorted_transactions = account.sort_transactions()
for transaction in sorted_transactions:
    print(transaction)
