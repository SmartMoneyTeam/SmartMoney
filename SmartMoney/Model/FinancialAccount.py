from datetime import datetime

class FinancialAccount(object):
    """A portfolio that tracks transactions and manages an evolving amount of money"""

    def __init__(self, name):
        self.name = name
        self.transactions = []

    @property
    def amount(self):
        return self.amount_at(datetime.now())

    def amount_at(self, date):
        return sum(map(lambda t: t.amount ,
						filter(lambda t: t.date <= date, 
							self.transactions)))

    def amount_evolution(self, date_start, date_end):
        if date_start >= date_end:
            raise Exception('Invalid Range')
        amount = self.amount_at(date_start)
        evolution = [(date_start, amount)]
        for t in sorted(
                        filter(
                                lambda t: t.date > date_start and t.date <= date_end,
                                self.transactions),
                        key = lambda t: t.date):
            amount = amount + t.amount
            evolution.append((t.date, amount))
        evolution.append((date_end, amount))
        return evolution

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __str__(self):
        return self.name