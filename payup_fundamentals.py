"""PayUp using the concepts taught in Scrimba Python Fundamentals.

Use numeric amounts, a whole-number tip, and a group size of at least one.
The main payup.py version adds friendly validation as an optional extension.
"""

print("Welcome to PayUp — split the bill, keep it simple.\n")

event = input("What are we splitting? ")
cost = float(input("How much did it cost? $"))
service_charge = int(input("Tip or service charge (%)? ").strip().strip("%"))
group_size = int(input("How many people are splitting it? "))

service_charge_total = cost * (service_charge / 100)
grand_total = cost + service_charge_total
total_per_person = grand_total / group_size

print(f"\n{event}")
print(f"Cost:            ${cost:.2f}")
print(f"Tip ({service_charge}%):       ${service_charge_total:.2f}")
print(f"People:          {group_size}")
print(f"Grand total:     ${grand_total:.2f}")
print(f"Each person:     ${total_per_person:.2f}")
print("\nAmounts are displayed to the nearest cent.")
