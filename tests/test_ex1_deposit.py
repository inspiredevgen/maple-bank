import unittest

from maplebank.account import Account


class TestEx1Deposit(unittest.TestCase):
    """Exercise 1 - Student A: deposits must be positive."""

    def test_positive_deposit_increases_balance(self):
        acc = Account("T-1", "Test")
        acc.deposit(25.00)
        self.assertEqual(acc.balance, 25.00)

    def test_negative_deposit_is_refused(self):
        acc = Account("T-1", "Test")
        with self.assertRaises(ValueError):
            acc.deposit(-50.00)
        self.assertEqual(acc.balance, 0.0)

    def test_zero_deposit_is_refused(self):
        acc = Account("T-1", "Test")
        with self.assertRaises(ValueError):
            acc.deposit(0)
