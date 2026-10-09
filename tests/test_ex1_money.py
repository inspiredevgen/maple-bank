import unittest

from maplebank.report import format_money


class TestEx1Money(unittest.TestCase):
    """Exercise 1 - Student B: money is shown as $1,234.50 CAD."""

    def test_two_decimals_and_thousands_separator(self):
        self.assertEqual(format_money(1234.5), "$1,234.50 CAD")

    def test_negative_amount(self):
        self.assertEqual(format_money(-20), "-$20.00 CAD")

    def test_float_noise_is_hidden(self):
        self.assertEqual(format_money(0.1 + 0.2), "$0.30 CAD")
