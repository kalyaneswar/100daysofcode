Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

import random

asci_list = [Rock, Paper, Scissors]

computer_choice = random.randint(0,2)
# print(computer_choice)
computer = asci_list[computer_choice]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

user = asci_list[user_choice]
print(f"user choice is {user}")
print(f"computer choice is {computer}")

# Determine the winner
if computer_choice == user_choice:
    print("🤝 It's a draw!")
elif (computer_choice == 0 and user_choice == 1) or \
     (computer_choice == 1 and user_choice == 2) or \
     (computer_choice == 2 and user_choice == 0):
    print("🎉 You win!")
else:
    print("😞 You lose!")