class Transaction:
    def __init__(self, date, amount, transaction_type, comment=None) -> None:
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.comment = comment