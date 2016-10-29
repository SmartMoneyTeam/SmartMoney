from datetime import datetime
from datetime import timedelta

#a class to wrap payees or revenues info
class Transaction:

	def __init__(self, name, amount, date):
		self.name = name
		self.amount = amount
		self.date = date

#a class to manage a portfolio
class FinacialAccount:
	
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


#tests
my_wallet = FinacialAccount('Wallet', 64.5)

salary = Transaction('Salary', 700, datetime.now() - timedelta(days = 1))
my_wallet.add_transaction(salary)
print('{} status: {}'.format(my_wallet, my_wallet.amount))