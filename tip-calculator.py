print("Welcome to the Chipmunk's tip calculator")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip_as_percentage = tip_percentage / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount

bill_per_person = total_bill / number_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
