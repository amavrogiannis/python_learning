"""
Bank Account - TDD Exercise
"""
from dataclasses import dataclass

transaction_history = []

class BankAccount: 
    balance: float = 0.0
    deposit: float = 0.0
    withdraw: float = 0.0
    transfer: float = 0.0

    def deposit(self) -> float:
        self.deposit = deposit
        self.balance += self.deposit
    
    def withdraw(self) -> float:
        self.withdraw = withdraw
        if self.withdraw > self.balance:
            self.balance -= self.withdraw
        else:
            print('Insufficient ammount')
    
    def transfer(self) -> float:
        self.transfer = transfer
        if self.transfer > self.balance:
            self.balance -= self.transfer
        else:
            print('Insufficient ammount')

