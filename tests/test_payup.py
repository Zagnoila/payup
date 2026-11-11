import subprocess
import sys
import unittest
from decimal import Decimal
from pathlib import Path
from payup import calculate_split

ROOT = Path(__file__).resolve().parents[1]

class PayUpTests(unittest.TestCase):
    def test_even_split(self):
        self.assertEqual(calculate_split(Decimal("120"), Decimal("20"), 4),
                         (Decimal("24.00"), Decimal("144.00"), Decimal("36"), 0))

    def test_remainder_preserves_total(self):
        tip, total, base, extra = calculate_split(Decimal("10"), Decimal("0"), 3)
        self.assertEqual((base, extra), (Decimal("3.33"), 1))
        self.assertEqual(base * 3 + Decimal("0.01") * extra, total)

    def test_small_cost_and_more_people_than_cents(self):
        self.assertEqual(calculate_split(Decimal("0.01"), Decimal("0"), 3),
                         (Decimal("0.00"), Decimal("0.01"), Decimal("0"), 1))

    def test_tip_half_cent_rounds_up(self):
        self.assertEqual(calculate_split(Decimal("0.05"), Decimal("10"), 1)[0], Decimal("0.01"))

    def run_cli(self, answers):
        return subprocess.run([sys.executable, str(ROOT / "payup.py")], input=answers,
                              text=True, capture_output=True, check=True).stdout

    def test_percent_and_dollar_symbols(self):
        output = self.run_cli("Pizza night\n$120.00\n20%\n4\n")
        self.assertIn("$144.00", output)
        self.assertIn("$36.00", output)

    def test_invalid_inputs_retry(self):
        output = self.run_cli("\nNaN\nInfinity\n-5\nhello\n1.234\n10\n15.5\n0\n0\n-2\n2.5\n3\n")
        self.assertIn("Shared expense", output)
        self.assertIn("Use at most two decimal places", output)
        self.assertIn("Use a whole-number percentage", output)
        self.assertIn("Enter a whole number from 1", output)
        self.assertIn("$3.34", output)
        self.assertIn("$3.33", output)

    def test_zero_bill(self):
        self.assertIn("$0.00", self.run_cli("Free lunch\n0\n0\n1\n"))

    def test_closed_input_exits_cleanly(self):
        self.assertIn("PayUp closed", self.run_cli(""))

if __name__ == "__main__":
    unittest.main()
