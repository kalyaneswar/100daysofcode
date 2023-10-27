print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("what's your age "))
bill =0

if height >= 120:

    print("You are eligible for the ride")
    if age <= 18:
        bill = 7
        print("you have to pay $7")
    else:
        bill = 12
        print("you have to pay $12")
else:
    print("Sorry! You can't have ride for now")

want_photo = input("Do you want a photo taken? Y or N.")
if want_photo == 'Y':
    bill += 3
    print(bill)
else:
    bill += 0
    print(bill)