import datetime
from models.Transaction import Transaction


class BankDatabase:

    def __init__(self) -> None:
        self.__table_transaction = []

    def __add_transaction(self, transaction):
        self.__table_transaction.append(transaction)

    def get_transactions(self):
        return self.__table_transaction

    def deposit_money(self, amount, comment=None):
        self.__add_transaction(
            Transaction(datetime.datetime.now(), amount, "DEPOSIT", comment)
        )

    def withdraw_money(self, amount, comment=None):
        self.__add_transaction(
            Transaction(datetime.datetime.now(), amount, "WITHDRAWAL", comment)
        )
