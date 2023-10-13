"""
Bank Account - TDD Exercise
"""

class BankAccount:
    """ BankAccount class """

    def __init__(self, balance: float) -> None:
        self.balance = balance
        print(f"Balance: {balance:.2f}")
        self.transaction = []

    def deposit(self, ammount: float) -> None:
        """ BankAccount Deposit object """
        self.balance += ammount
        data = f"DP: {ammount}"
        self.transaction.append(data)

    def withdraw(self, cash: float) -> None:
        """ BankAccount Withdraw object """
        if self.balance >= cash:
            self.balance -= cash
            data = f"WD: {cash}"
            self.transaction.append(data)
        else:
            raise ValueError('Withdraw declined. Insufficient funds.')

    def transfer(self, other_account, funds: float) -> None:
        """ BankAccount Transfer object """
        if self.balance >= funds:
            # """ TO - Transfer Out """
            self.balance -= funds
            data = f"TO: {funds}"
            self.transaction.append(data)

            # """ TI - Transfer In """
            other_account.balance += funds
            data = f"TI: {funds}"
            other_account.transaction.append(data)
        else:
            raise ValueError('Transfer declined. Insufficient funds.')

if __name__ == "__main__":
    alex = BankAccount(1000.00) # Current account balance for Alex is £1000
    john = BankAccount(350.00) # Current account balance for John is £350
    alex.deposit(400.00) # Alex deposits £400
    alex.withdraw(100.00) # Alex withdraws £100
    alex.transfer(john, 250.00) # Alex sends to John £250
    print("Transaction:", alex.transaction)
    print("Closing balance - Alex:",alex.balance)

    print("Transaction:", john.transaction)
    print("Closing balance - John:",john.balance)

# End-of-file (EOF)
