"""Importing modules to test script"""
import unittest
from account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Testing class BankAccount"""

    def setUp(self):
        """Setup fixtures"""
        self.account = BankAccount()

    def test_account_balance(self):
        """ This function will test the account balance that is given to the account """
        self.account.balance = 20.0
        self.assertEqual(self.account.balance, 20.0)

    def test_deposit(self):
        """Testing the deposit ammount to the account"""
        self.account.balance = 15
        self.account.deposit = 20

        self.account.balance += self.account.deposit

        self.assertEqual(self.account.balance, 35)

    def test_withdraw(self):
        """Testing the withdraw ammount from the account"""
        self.account.balance = 20
        self.account.withdraw = 5
        if self.account.balance > self.account.withdraw:
            self.account.balance -= self.account.withdraw
        else:
            print('Insufficient ammount')

        self.assertEqual(self.account.balance, 15)

    def test_transfer(self):
        """Transfer funds to another account"""
        self.account.balance = 50
        self.account.transfer = 20
        if self.account.balance > self.account.transfer:
            self.account.balance -= self.account.transfer
        else:
            print('Insufficient ammount')

        self.assertEqual(self.account.balance, 30)



if __name__ == '__main__':
    unittest.main()
