import unittest as Test
import FinancialAccount
import Transaction

class TestTransactions(unittest.TestCase):
    def test_addition(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    Test.main()


#to be integrated above
my_wallet = FinancialAccount('Wallet', 64.5)

salary = Transaction('Salary', 700, datetime.now())
my_wallet.add_transaction(salary)
print('{} status: {}'.format(my_wallet, my_wallet.amount))