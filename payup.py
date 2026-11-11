"""PayUp: an expense splitter with optional input-validation extensions.

Run with Python 3. No third-party packages or account required.
"""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")


def read_amount(prompt, *, percent=False):
    """Keep asking until the user gives a finite, nonnegative number."""
    while True:
        raw = input(prompt).strip()
        if percent:
            raw = raw.removesuffix("%").strip()
        else:
            raw = raw.removeprefix("$").strip()
        try:
            value = Decimal(raw)
            if not value.is_finite() or value < 0 or value > 1_000_000:
                raise ValueError
            if not percent and value != value.quantize(CENT):
                print("Use at most two decimal places for the cost.")
                continue
            if percent and value != value.to_integral_value():
                print("Use a whole-number percentage, like 15 or 15%.")
                continue
            return value
        except (InvalidOperation, ValueError):
            print("Enter a number from 0 to 1000000, like 25 or 25.50.")


def read_group_size():
    while True:
        try:
            people = int(input("How many people are splitting it? "))
            if 1 <= people <= 10000:
                return people
        except ValueError:
            pass
        print("Enter a whole number from 1 to 10000.")


def calculate_split(cost, tip_percent, people):
    """Round the tip once, then distribute cents so shares equal the total."""
    tip = (cost * tip_percent / 100).quantize(CENT, rounding=ROUND_HALF_UP)
    total = cost + tip
    cents = int(total * 100)
    base_cents, extra_people = divmod(cents, people)
    low_share = Decimal(base_cents) / 100
    return tip, total, low_share, extra_people


def main():
    print("\n" + "=" * 48)
    print("  PAYUP  /  Ian Rosenthal")
    print("  Split the bill, keep it simple.")
    print("=" * 48 + "\n")

    event = input("What are we splitting? ").strip() or "Shared expense"
    cost = read_amount("How much did it cost? $")
    tip_percent = read_amount("Tip or service charge (%)? ", percent=True)
    people = read_group_size()
    tip, total, low_share, extra_people = calculate_split(cost, tip_percent, people)

    print("\n" + "-" * 48)
    print(f"  {event}")
    print("-" * 48)
    print(f"  Cost                  ${cost:,.2f}")
    print(f"  Tip ({tip_percent:.0f}%)             ${tip:,.2f}")
    print(f"  People                 {people}")
    print(f"  GRAND TOTAL           ${total:,.2f}")
    print("-" * 48)
    if extra_people:
        print(f"  {extra_people} person(s) pay        ${low_share + CENT:,.2f}")
        print(f"  {people - extra_people} person(s) pay        ${low_share:,.2f}")
        print("  The extra cent(s) keep the split exact.")
    else:
        print(f"  EACH PERSON           ${low_share:,.2f}")
    print("=" * 48 + "\n")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nPayUp closed. No expense was saved.")
