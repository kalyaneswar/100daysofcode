names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆


import random
random_name_number = random.randint(0,len(names)-1)
random_name = names[random_name_number]
print(f"{random_name} is going to buy the meal today!")