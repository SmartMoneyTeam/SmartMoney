from FinancialAccount import FinancialAccount
from Transaction import Transaction, RepeatedTransaction, Transfer, datetime

def print_evolution(account):
    print("{}:".format(account))
    evolution = account.amount_evolution(datetime(2016, 1, 1), datetime(2016, 12, 31))
    for el in evolution:
	    print("{}/{}/{}\t{}".format(el[0].day, el[0].month, el[0].year, el[1]))

# init
wallet = FinancialAccount('Wallet')
bank = FinancialAccount("Bank", initial = 1000)
RepeatedTransaction('Salary', bank, 695, datetime(2016, 1, 10), end_date=datetime(2016, 12, 31))
Transaction('Salary', bank, amount = 695, date=datetime(2016, 1, 10))
Transfer(bank, wallet, 100)

# display result
print_evolution(bank)
print_evolution(wallet)