"""Run all tests and print a progress table per exercise.

Usage:  python tools/test_report.py
In GitHub Actions the table is also written to the run's Summary page.
Exit code: 0 when everything passes, 1 otherwise.
"""
import os
import sys
import unittest
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

LABELS = {
    "TestEx1Deposit": "Ex 1 · A · Deposits must be positive",
    "TestEx1Money": "Ex 1 · B · Money formatting",
    "TestEx2Config": "Ex 2 · Fee and overdraft policy",
    "TestEx3Withdraw": "Ex 3 · Withdraw limit + fee",
    "TestEx4Interest": "Ex 4 · Monthly interest",
    "TestEx5Transfer": "Ex 5 · A · Transfer direction",
    "TestEx5AccountNumbers": "Ex 5 · B + hotfix · Account numbers",
}


class Collector(unittest.TestResult):
    def __init__(self):
        super().__init__()
        self.by_class = defaultdict(lambda: [0, 0])          # [passed, total]

    def addSuccess(self, test):
        super().addSuccess(test)
        self.by_class[type(test).__name__][0] += 1

    def startTest(self, test):
        super().startTest(test)
        self.by_class[type(test).__name__][1] += 1


def main():
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"), top_level_dir=str(ROOT))
    result = Collector()
    suite.run(result)

    rows = ["| Exercise | Tests | Status |", "|---|---|---|"]
    passed_all = total_all = 0
    for cls, label in LABELS.items():
        passed, total = result.by_class.get(cls, [0, 0])
        passed_all += passed
        total_all += total
        icon = "✅" if total and passed == total else "❌"
        rows.append(f"| {label} | {passed}/{total} | {icon} |")
    branch = os.getenv("GITHUB_REF_NAME", "local")
    report = f"## Maple Bank · test progress on `{branch}`\n\n" + "\n".join(rows) + \
             f"\n\n**{passed_all}/{total_all} tests passing**\n"

    print(report)
    for test, trace in result.failures + result.errors:
        print(f"--- {test.id()}\n{trace.strip().splitlines()[-1]}\n")
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(report)
    return 0 if passed_all == total_all else 1


if __name__ == "__main__":
    sys.exit(main())
