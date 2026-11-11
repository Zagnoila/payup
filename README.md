# PayUp — Ian Rosenthal

A small Python app that splits a shared expense. Enter the occasion, cost, tip percentage, and number of people. PayUp shows the tip, grand total, and what each person owes.

Built for **Scrimba Learn Python — Module 1: Python Fundamentals**.

## Run it

Install Python 3.9 or newer. Download this repository and open its folder in your terminal (the window where you type commands). Run:

```sh
python3 payup.py
```

On Windows, use `py payup.py` if `python3` is unavailable. No extra packages are needed. Type an answer after each question and press Enter.

Example: `Pizza night`, `120`, `20%`, `4` gives a **$24.00 tip**, **$144.00 total**, and **$36.00 per person**.

## Two versions

- **payup_fundamentals.py** follows the module's variables, strings, input, numeric conversion, arithmetic, `.strip()` and two-decimal f-strings. Run `python3 payup_fundamentals.py`. It expects valid numeric input and a positive group size, as the course version does.
- **payup.py** adds friendly retries for invalid input and exact cent allocation. These optional extensions use functions, loops, exception handling, `Decimal`, and `divmod`, which go beyond Module 1. A $10 bill split three ways becomes $3.34 + $3.33 + $3.33.
- **practice/** contains original exercise answers and the stages used to build the course version.

The app calculates in dollars, accepts a whole-number tip percentage, and stores no personal or payment data. It does not transfer money. The tip is rounded to cents using half-up rounding; any leftover cents are assigned to some group members so all shares add up exactly.

## Check the work

```sh
python3 -m unittest discover -s tests -v
python3 practice/run_practice.py
```

Course: https://scrimba.com/learn-python-c03
