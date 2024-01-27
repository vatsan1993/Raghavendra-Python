# this can be built using dictionaries or by using composition
class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, receiver = None ):
        self._transaction_id = transaction_id
        self._transaction_type = transaction_type
        self._amount = amount
        self._receiver = receiver

    def get_id (self):
        return self._transaction_id

    def get_amount(self):
        return self._amount

    def __str__(self):
        return f'Transaction id: {self._transaction_id} , Type: {self._transaction_type, self._amount, self._receiver}'

class BankAccount:
    def __init__(self, acc_id, name, age):
        self._acc_id = acc_id
        self._name = name
        self._age = age
        self._transactions = []

    # def add_transaction(self, transaction_id, transaction_type, amount, receiver = None):
    #     self._transactions.append(Transaction(transaction_id, transaction_type, amount, receiver))

    def add_transaction (self, transaction):
        self._transactions.append(transaction)
        
