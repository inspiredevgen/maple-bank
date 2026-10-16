"""A single bank account."""
from maplebank import config


class InsufficientFunds(Exception):
    """Raised when a withdrawal would go below the allowed limit."""


class Account:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive not null")
        self.balance += amount
        self._record("deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        self._record("withdrawal", amount)

    def _record(self, kind, amount):
        self.transactions.append((kind, amount, self.balance))
