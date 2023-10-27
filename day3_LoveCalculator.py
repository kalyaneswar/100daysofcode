print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name2 + name1
upper_name = combined_names.upper()

T = upper_name.count('T')
R = upper_name.count('R')
U = upper_name.count('U')
E = upper_name.count('E')

true_score = T + R + U + E


L = upper_name.count('L')
O = upper_name.count('O')
V = upper_name.count('V')
E = upper_name.count('E')

love_score = L+O+V+E


total_score_string = str(true_score) + str(love_score)
total_score = int(total_score_string)

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")

