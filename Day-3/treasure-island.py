print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("Your mission is to find the treasure.")
user_dir = input('Type "left" or "right"\n').lower()
if user_dir == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.\n")
    wait_r_swim = input('Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if wait_r_swim == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors_choice = input("One red, one yellow and one blue. Which colour do you choose?").lower()
        if doors_choice == 'red':
            print("It's a room full of fire. Game Over.")
        elif doors_choice == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif doors_choice == 'yellow':
            print("You found the treasure! You Win!")
        else:
            print("Please enter correct input")
    elif wait_r_swim == 'swim':
        print('You get attacked by an angry trout. Game Over.')
    else:
        print("Please enter correct input")

elif user_dir == 'right':
    print("You fell into a hole. Game Over.")
else:
    print("Please enter correct input")

