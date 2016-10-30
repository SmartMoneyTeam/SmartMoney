import unittest
import FinancialAccount
import Transaction

class Test_Transactions(unittest.TestCase):
    def test_addition(self):
        wallet = FinancialAccount('Wallet')
        wallet.add_transaction(Transaction('Salary', 700))
        self.assertEqual(wallet.amount, 700)

if __name__ == '__main__':
    unittest.main()