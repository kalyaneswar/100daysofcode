
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_provided = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_people= int(input("How many people to split the bill?"))
bill_per_person = (total_bill + tip_provided)/total_people
print("each person should pay: $" + str(bill_per_person))