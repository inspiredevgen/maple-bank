"""Demo: run `python main.py` and read the output carefully - some numbers are wrong!"""
from maplebank.bank import Bank
from maplebank.interest import apply_monthly_interest
from maplebank.report import statement


def attempt(description, action):
    """Run one banking action and say whether the bank accepted or refused it."""
    try:
        action()
        print(f"  accepted: {description}")
    except Exception as exc:          # the bank refused - that's fine for the demo
        print(f"  refused:  {description}  ({type(exc).__name__}: {exc})")


bank = Bank()
alice = bank.open_account("Alice Martin", 500.00)
bob = bank.open_account("Bob Nguyen", 100.00)

print("Activity")
attempt("Alice deposits 0.10", lambda: alice.deposit(0.10))
attempt("Alice deposits 0.20", lambda: alice.deposit(0.20))
attempt("Alice deposits -50.00 (should be refused)", lambda: alice.deposit(-50.00))
attempt("Alice transfers 75.00 to Bob", lambda: bank.transfer(alice.number, bob.number, 75.00))
attempt("Bob withdraws 1000.00 (should be refused)", lambda: bob.withdraw(1000.00))
attempt("Monthly interest for Alice", lambda: apply_monthly_interest(alice))

print()
print(f"Accounts opened: {', '.join(bank.accounts)}")
print()
print(statement(alice))
print()
print(statement(bob))
