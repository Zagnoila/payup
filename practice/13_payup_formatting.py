event = input("Occasion? ")
cost = float(input("Cost? "))
service_charge = int(input("Tip percentage? "))
group_size = int(input("People? "))
service_charge_total = cost * (service_charge / 100)
grand_total = cost + service_charge_total
total_per_person = grand_total / group_size
print(f"{event}: cost ${cost:.2f}; tip ${service_charge_total:.2f}; people {group_size}")
print(f"Total ${grand_total:.2f}; each ${total_per_person:.2f}")
