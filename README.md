# Maple Bank 🍁

A tiny banking library used to practise Git: **clone, branch, add, commit, push, fetch, pull, merge, rebase and conflict resolution**.

The code works... mostly. It has **bugs on purpose**. Your exercises fix them, in pairs, and Git conflicts *will* happen. That's the point.

## Run it
Only Python 3.10+ is needed. Nothing to install.
```bash
python main.py                      # demo - look closely, some numbers are wrong
python -m unittest -v               # all tests (many fail at the start)
python tools/test_report.py         # progress table per exercise
```

## Layout
```
maplebank/
  config.py     bank name, currency, fees, limits, interest rate
  account.py    Account: deposit, withdraw
  bank.py       Bank: open accounts, find, transfer
  interest.py   monthly interest
  report.py     money formatting and statements
tests/          one test file per exercise
tools/          test_report.py (also used by GitHub Actions)
.github/workflows/ci.yml   build + tests on every push and pull request
main.py         demo script
```

## Continuous integration
Every `git push` (any branch) and every pull request triggers the **CI** workflow (GitHub → *Actions* tab):
1. **Build:** compile check (it also catches leftover `<<<<<<<` conflict markers), run the demo, upload the build as an artifact.
2. **Tests:** run the tests and post a ✅/❌ table per exercise on the run's **Summary** page.

## Rules of the game
- Never commit directly to `main`.
- Your pair works on **your team branch** (`team-01`, `team-02`, ...). Your instructor gives you its number.
- Personal branches are named `teamNN-<yourname>-exN`, e.g. `team07-alice-ex1`.
