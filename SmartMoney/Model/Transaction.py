class Transaction(object):
    """A generic transaction of money to or from a portfolio"""

    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date

    def __str__(self):
        return self.name + "({})".format(self.amount)
