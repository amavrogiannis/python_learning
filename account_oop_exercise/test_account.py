"""
Bank Account - TDD Exercise - Test Script
"""
import pytest
from account import BankAccount

def test_account_balance():
    """ Testing BankAccount balance object """
    account_this = BankAccount(100.00)

    assert account_this.balance == 100.00

def test_deposit():
    """ Testing BankAccount deposit object """
    account_this = BankAccount(100.00)
    account_this.deposit(50.00)

    assert account_this.balance == 150.00

def test_withdraw():
    """ Testing BankAccount withdraw object """
    account_this = BankAccount(100.00)
    account_this.withdraw(20.00)

    assert account_this.balance == 80.00

def test_withdraw_fail():
    """ Testing BankAccount withdraw FAIL object """
    account_this = BankAccount(100.00)
    account_this.withdraw(200.00)

    assert pytest.raises(ValueError, match='Withdraw declined. Insufficient funds.')

def test_transfer():
    """ Testing BankAccount transfer object """
    account_one = BankAccount(100.00)
    account_two = BankAccount(10.00)
    account_one.transfer(account_two, 40.00)

    assert account_one.balance == 60.00
    assert account_two.balance == 50.00

def test_transfer_fail():
    """ Testing BankAccount transfer FAIL object """
    account_this = BankAccount(100.00)
    account_this.withdraw(200.00)

    assert pytest.raises(ValueError, match='Transfer declined. Insufficient funds.')

def test_transaction():
    """ Testing BankAccount transaction """
    account_this = BankAccount(100.00)
    account_this.withdraw(20.00)
    account_this.deposit(50.00)

    assert account_this.transaction == ['WD: 20.0', 'DP: 50.0']
