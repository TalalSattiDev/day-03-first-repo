bill = float(input("What's the bill total? "))
tip_percent = float(input("What tip % do you want to leave? "))
people = int(input("How many people are splitting? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print("")
print(f"Bill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each person pays: ${per_person:.2f}")