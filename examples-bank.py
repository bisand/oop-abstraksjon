import datetime


class Transaction:
    def __init__(self, account_number, date, amount, type) -> None:
        self.account_number = account_number
        self.date = date
        self.amount = amount
        self.type = type


class BankAccount:
    def __init__(self, account_number, owner, initial_balance) -> None:
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = initial_balance
        self.__transactions = []
        self.__add_transaction(account_number, initial_balance, "DEPOSIT")

    def __add_transaction(self, account_number, initial_balance, type):
        self.__transactions.append(
            Transaction(account_number, datetime.datetime.now(), initial_balance, type)
        )

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction(self.__account_number, amount, "DEPOSIT")
            print(f"{amount} has been deposited.")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            print(
                f"You do not have coverage. The amount is {amount} but balance is {self.__balance}"
            )
            return
        self.__balance -= amount
        self.__add_transaction(self.__account_number, amount, "WITHDRAWAL")

    def get_balance(self):
        return self.__balance
    
    def get_transactions(self):
        result = "account_no;date;amount;transaction_type\n"
        for t in self.__transactions:
            result += f"{t.account_number};{t.date};{t.amount};{t.type}\n"
        return result


account = BankAccount("1234567890", "André", 1000)
print(account.get_balance())
account.deposit(520)
print(account.get_balance())
account.withdraw(302)
print(account.get_balance())
account.withdraw(1500)
print(account.get_balance())

print(account.get_transactions())
