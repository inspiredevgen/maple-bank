import unittest

from maplebank import config


class TestEx2Config(unittest.TestCase):
    """Exercise 2 - new fee and overdraft policy (both tickets must land)."""

    def test_ticket_A_withdrawal_fee_is_two_dollars(self):
        self.assertEqual(config.WITHDRAWAL_FEE, 2.00)

    def test_ticket_B_overdraft_limit_is_one_hundred(self):
        self.assertEqual(config.OVERDRAFT_LIMIT, 100.00)
