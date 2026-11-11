"""Run every exercise with example answers and check its expected result."""
from pathlib import Path
import subprocess
import sys

cases = [
    ("01_first_look.py", "", "Ian, you are invited"),
    ("02_variables.py", "", "4\n6"),
    ("03_variables_in_action.py", "", "65\n60"),
    ("04_strings.py", "", "1. Water the plants. 2. Work on Python. 3. Draw a city."),
    ("05_f_strings.py", "", "20 buildings to draw"),
    ("06_payup_summary.py", "", "Total $330; each person $110"),
    ("07_input.py", "Alex\nmovie night\n12\nplants\nwater\n", "12 plants to water"),
    ("08_payup_input.py", "Pizza\n300\n10\n3\n", "cost 300, tip 10%, people 3"),
    ("09_arithmetic.py", "", "153\n36\n8.0"),
    ("10_type_conversion.py", "25\n88\n", "Pay: $2200.00"),
    ("11_payup_conversion.py", "Pizza\n300\n10\n3\n", "<class 'str'> <class 'float'> <class 'int'> <class 'int'>"),
    ("12_payup_calculation.py", "Karaoke\n200\n15\n3\n", "tip 30.0; total 230.0; each 76.666"),
    ("13_payup_formatting.py", "Karaoke\n200\n15\n3\n", "Total $230.00; each $76.67"),
    ("../payup_fundamentals.py", "Pizza night\n120\n20%\n4\n", "$36.00"),
]
for filename, answers, expected in cases:
    result = subprocess.run([sys.executable, str(Path(__file__).parent / filename)], input=answers, text=True, capture_output=True, check=True)
    assert expected in result.stdout, (filename, result.stdout)
    print(f"PASS {filename}")
print(f"\nAll {len(cases)} practice checks passed.")
