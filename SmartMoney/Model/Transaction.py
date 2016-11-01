from datetime import datetime
from relativedelta import relativedelta

class Transaction(object):
    """
    A generic transaction of money to or from a portfolio
    
    """

    def __init__(self, name, account, amount, date=datetime.now()):
    	"""
    	Creates a new transaction object, given its name and the portfolio this must be registered in
    	
    	"""
        self.account = account.add_transaction(self)
        self.name = name
    	self.amount = amount
    	self.date = date

    def __str__(self):
    	"""
    	Gives a string representation of this transaction
    	
    	"""
    	return self.name + " ({})".format(self.amount)

class Transfer(Transaction):
    """
    A transfer of money from a portfolio to another

    """

    def __init__(self, account_from, account_to, amount_from, amount_to=None, date=datetime.now()):
        self.transaction_from = Transaction('{}->{}'.format(account_from, account_to), account_from, -amount_from, date)
        self.transaction_to = Transaction('{}->{}'.format(account_from, account_to), account_to, amount_to if amount_to is not None else amount_from, date)
        self.amount = amount_from
        self.account = account_from
        self.date = date
        self.name = '{}->{}'.format(account_from, account_to)

class RepeatedTransaction(Transaction):
    """
    A transaction that is repeated in time

    """

    def __date_increment_function(self):
        switcher = {
            'day': lambda d: d + relativedelta(days = 1),
            'week':lambda d: d + relativedelta(weeks = 1),
            'month': lambda d: d + relativedelta(months = 1),
            'year': lambda d: d + relativedelta(years = 1)
            }
        return switcher.get(self.quantum, switcher.get('month'))

    def __get_transactions(self):
        current_date = self.date_from
        increment_date = self.__date_increment_function()
        transactions = []
        while current_date <= self.date_to:
            transactions.append(Transaction(self.name, self.account, self.amount, current_date))
            current_date = increment_date(current_date)

    def __init__(self, name, account, amount, date_start=datetime.now(), quantum="month", number_of_quants=1, end_date=datetime.now() + relativedelta(months = 1)):
        self.account = account
        self.amount = amount
        self.date_from = date_start
        self.name = name
        self.date_to = end_date
        self.quantum = quantum
        self.number_of_quants = number_of_quants
        self.transactions = self.__get_transactions()