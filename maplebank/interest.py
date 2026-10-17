"""Monthly interest on savings."""
from maplebank import config


def monthly_interest(account):
    return round(account.balance * config.ANNUAL_INTEREST_RATE / 12, 2)


def apply_monthly_interest(account):
    interest = monthly_interest(account)
    if interest > 0:
        account.deposit(interest)
    return interest
