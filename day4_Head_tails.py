# 1 means Heads 0 means Tails

print('Welcome! You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".')

import  random

choose1 = random.randint(0,1)
print(choose1)
if choose1 == 1:
    print("Head")
elif choose1 ==0:
    print("Tail")
else:
    print("Something is wrong check with tech team")