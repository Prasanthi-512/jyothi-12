
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self._balance = 0  # Protected attribute (encapsulation)

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount} to {self.owner}'s account")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount} from {self.owner}'s account")
        else:
            print("Insufficient funds")


class CurrentAccount(Account):
    def __init__(self, account_number, owner, overdraft_limit=1000):
        super().__init__(account_number, owner)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited ${amount} to {self.owner}'s account")

    def withdraw(self, amount):
        if self._balance + self.overdraft_limit >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount} from {self.owner}'s account")
        else:
            print("Overdraft limit exceeded")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, account_number, owner):
        if account_type == 'savings':
            account = SavingsAccount(account_number, owner)
        elif account_type == 'current':
            account = CurrentAccount(account_number, owner)
        else:
            print("Invalid account type")
            return
        self.accounts[account_number] = account
        print(f"Created {account_type} account for {owner}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


# Main driver
bank = Bank()
bank.create_account('savings', '1001', 'Alice')
bank.create_account('current', '1002', 'Bob')

acc1 = bank.get_account('1001')
acc2 = bank.get_account('1002')

acc1.deposit(500)
acc1.withdraw(100)
print("Balance:", acc1.get_balance())

acc2.deposit(300)
acc2.withdraw(800)
print("Balance:", acc2.get_balance())
