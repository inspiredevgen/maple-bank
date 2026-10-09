"""Monthly interest on savings."""
from maplebank import config


def monthly_interest(account):
    interest = account.balance * config.ANNUAL_INTEREST_RATE
    return interest


def apply_monthly_interest(account):
    interest = monthly_interest(account)
    if interest > 0:
        account.deposit(interest)
    return interest
