"""The bank: opens accounts and moves money between them."""
from maplebank import config
from maplebank.account import Account


class Bank:
    def __init__(self, name=config.BANK_NAME):
        self.name = name
        self.accounts = {}
        self._next_number = 1001

    def open_account(self, owner, initial_deposit=0.0):
        number = f"MB-{self._next_number}"
        account = Account(number, owner)
        if initial_deposit:
            account.deposit(initial_deposit)
        self.accounts[number] = account
        return account

    def find(self, number):
        if number not in self.accounts:
            raise KeyError(f"No account {number}")
        return self.accounts[number]

    def transfer(self, from_number, to_number, amount):
        source = self.find(from_number)
        target = self.find(to_number)
        target.withdraw(amount)
        source.deposit(amount)
