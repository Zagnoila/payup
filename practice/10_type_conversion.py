hourly_rate = float(input("Hourly rate? "))
hours_worked = int(input("Whole hours worked? "))
print(type(hourly_rate))
print(type(hours_worked))
total_pay = hourly_rate * hours_worked
print(f"Pay: ${total_pay:.2f}")
