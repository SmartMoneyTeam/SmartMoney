class FinancialAccount(object):
    """A portfolio that tracks transactions and manages an evolving amount of money"""

    def __init__(self, name, amount):
        self.name = name
        self.initial_amount = amount
        self.transactions = []

    @property
    def amount(self):
        return sum(map(lambda t: t.amount ,
						filter(lambda t: t.date <= datetime.now(), 
							self.transactions))
					, self.initial_amount)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __str__(self):
        return self.name

