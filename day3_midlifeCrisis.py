print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
want_photo = input("Do you want a photo for memory: Y or N: ")
age = int(input("what's your age "))
bill = 0
if height >= 120:
    print("You are eligible for the ride")
    if age < 12:
        print("you have to pay $7")
        bill += 5
    elif age >= 12 and age < 18:
        bill += 7
    elif age >= 18:
        if age >= 45 and age <= 55:
            bill += 0
        else:
            bill += 12
else:
    print("Sorry! You can't have ride for now")

if want_photo == 'Y':
    bill += 3
else:
    bill += 0

print(f"The total bill is {bill}")
