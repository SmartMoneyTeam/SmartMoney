import unittest
from FinancialAccount import FinancialAccount
from Transaction import Transaction

class Test_Transactions(unittest.TestCase):
    def test_addition(self):
        wallet = FinancialAccount('Wallet')
        self.assertEqual(wallet.amount, 700)

if __name__ == '__main__':
    unittest.main()