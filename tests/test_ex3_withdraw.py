import unittest

from maplebank import config
from maplebank.account import Account, InsufficientFunds


def account_with(balance):
    acc = Account("T-1", "Test")
    acc.balance = balance
    return acc


class TestEx3Withdraw(unittest.TestCase):
    """Exercise 3 - withdrawals: limit (A) + fee (B) must work TOGETHER."""

    def test_A_cannot_go_past_overdraft_limit(self):
        acc = account_with(100.00)
        too_much = 100.00 + config.OVERDRAFT_LIMIT + 50
        with self.assertRaises(InsufficientFunds):
            acc.withdraw(too_much)
        self.assertEqual(acc.balance, 100.00)

    def test_B_fee_is_charged_and_recorded(self):
        acc = account_with(100.00)
        acc.withdraw(10.00)
        self.assertAlmostEqual(acc.balance, 100.00 - 10.00 - config.WITHDRAWAL_FEE)
        kinds = [kind for kind, _, _ in acc.transactions]
        self.assertEqual(kinds, ["withdrawal", "fee"])

    def test_A_and_B_fee_counts_toward_available_funds(self):
        acc = account_with(100.00)
        # The amount fits, but amount + fee does not -> must be refused.
        amount = 100.00 + config.OVERDRAFT_LIMIT - config.WITHDRAWAL_FEE / 2
        with self.assertRaises(InsufficientFunds):
            acc.withdraw(amount)
        self.assertEqual(acc.balance, 100.00)
