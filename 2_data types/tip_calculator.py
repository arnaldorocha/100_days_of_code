print("Welcome to the Tip Calculator.\n")

bill = float(input("What was the total bill? "))
print("\n")

tip = float(input("What percentage of tip would you like to give? "))
print("\n")

person = float(input("How many people to split the bill? "))
print("\n")

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / person
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: {final_amount} \n"  )
