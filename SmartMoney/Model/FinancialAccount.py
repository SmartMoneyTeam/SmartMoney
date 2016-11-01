from datetime import datetime

class FinancialAccount(object):
    """
    A portfolio that tracks transactions and manages an evolving amount of money
    
    """

    def __init__(self, name, initial = 0):
    	"""
    	Creates a new portfolio, given a name and an optional initial amount
    	
    	"""
    	self.name = name
    	self.transactions = []
    	self.initial = initial

    @property
    def amount(self):
        return self.amount_at(datetime.now())

    def amount_at(self, date):
        return self.initial + sum(map(lambda t: t.amount ,
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
        return evolution

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return self;

    def __str__(self):
        return self.name
