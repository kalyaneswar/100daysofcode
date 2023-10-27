# # Rocks wins again scissors
# # scissors wins again papers
# # papers wins again Rocks
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# #Write your code below this line 👇
# import  random
# list1 = [rock,scissors,paper]
# value = 0
#
#
# user_choice = input('Choose one "rock","scissors","paper" :\n').lower()
# print(user_choice)
# if user_choice == 'rock':
#     value = 0
# elif user_choice == 'paper':
#     value = 1
# elif user_choice == 'scissors':
#     value = 2
#
# print(list1[value])
#
#
#
#
# computer_choice_number = random.randint(0,2)
# print(computer_choice_number)
# computer_choice = list1[computer_choice_number]
# print(computer_choice)
# if computer_choice == 'rock':
#     value = 0
# elif computer_choice == 'paper':
#     value = 1
# elif computer_choice == 'scissors':
#     value = 2
#
#
#
# print(computer_choice)
#
# if user_choice == computer_choice:
#     print("It's a tie try again!")
# elif user_choice == 'rock' and computer_choice == 'scissors':
#     print("You Win!")
# elif user_choice == 'scissors' and computer_choice == 'paper':
#     print("You Win!")
# elif user_choice == 'paper' and computer_choice == 'rock':
#     print("you Win!")
# else:
#     print("computer wins, You loose!")








import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end