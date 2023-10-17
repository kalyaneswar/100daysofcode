#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("what's the total bill\n"))

# print(type(bill))

tip_percentage = int(input("what's percentage of bill you would like to give tip 10%, 12%, 15%: \n"))
tip = (int(tip_percentage)/100) +1

total_amount = (bill * tip)

total_persons = int(input("How many u need to split :\n"))

final_bill_for_each = round(total_amount/total_persons)


print(final_bill_for_each)

