import unittest

from maplebank import config
from maplebank.account import Account
from maplebank.interest import monthly_interest


def account_with(balance):
    acc = Account("T-1", "Test")
    acc.balance = balance
    return acc


class TestEx4Interest(unittest.TestCase):
    """Exercise 4 - monthly interest: /12 (A) and rounded to cents (B)."""

    def test_A_monthly_not_annual(self):
        expected = 1200.00 * config.ANNUAL_INTEREST_RATE / 12
        self.assertAlmostEqual(monthly_interest(account_with(1200.00)), expected)

    def test_B_rounded_to_cents(self):
        value = monthly_interest(account_with(1000.55))
        self.assertEqual(value, round(value, 2))

    def test_A_and_B_together(self):
        expected = round(1000.55 * config.ANNUAL_INTEREST_RATE / 12, 2)
        self.assertEqual(monthly_interest(account_with(1000.55)), expected)
