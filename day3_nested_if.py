print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("what's your age "))

if height >= 120:
    print("You are eligible for the ride")
    if age <= 18:
        print("you have to pay $7")
    else:
        print("you have to pay $12")
else:
    print("Sorry! You can't have ride for now")