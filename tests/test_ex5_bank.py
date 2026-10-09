import unittest

from maplebank import config
from maplebank.account import Account, InsufficientFunds
from maplebank.bank import Bank


def bank_with_two_accounts():
    bank = Bank()
    for number, balance in (("X-1", 200.00), ("X-2", 50.00)):
        acc = Account(number, number)
        acc.balance = balance
        bank.accounts[number] = acc
    return bank


class TestEx5Transfer(unittest.TestCase):
    """Exercise 5 - Student A: money moves FROM source TO target."""

    def test_transfer_direction(self):
        bank = bank_with_two_accounts()
        bank.transfer("X-1", "X-2", 30.00)
        self.assertAlmostEqual(bank.find("X-1").balance, 200.00 - 30.00 - config.WITHDRAWAL_FEE)
        self.assertAlmostEqual(bank.find("X-2").balance, 50.00 + 30.00)

    def test_failed_transfer_changes_nothing(self):
        bank = bank_with_two_accounts()
        with self.assertRaises(InsufficientFunds):
            bank.transfer("X-2", "X-1", 10_000.00)
        self.assertAlmostEqual(bank.find("X-1").balance, 200.00)
        self.assertAlmostEqual(bank.find("X-2").balance, 50.00)


class TestEx5AccountNumbers(unittest.TestCase):
    """Exercise 5 - Student B (6-digit numbers) + the hotfix on main (unique numbers)."""

    def test_B_six_digit_format(self):
        self.assertEqual(Bank().open_account("A").number, "MB-001001")

    def test_hotfix_numbers_are_unique(self):
        bank = Bank()
        numbers = {bank.open_account(name).number for name in ("A", "B", "C")}
        self.assertEqual(len(numbers), 3)

    def test_B_and_hotfix_together(self):
        bank = Bank()
        bank.open_account("A")
        self.assertEqual(bank.open_account("B").number, "MB-001002")
