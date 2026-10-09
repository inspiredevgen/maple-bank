"""Printable account statements."""
from maplebank import config


def format_money(amount):
    return f"{amount} {config.CURRENCY}"


def statement(account):
    lines = [
        f"{config.BANK_NAME} - Statement for {account.owner} ({account.number})",
        "-" * 60,
    ]
    for kind, amount, balance_after in account.transactions:
        lines.append(f"{kind:<12} {format_money(amount):>20} {format_money(balance_after):>20}")
    lines.append("-" * 60)
    lines.append(f"{'Balance':<12} {format_money(account.balance):>41}")
    return "\n".join(lines)
