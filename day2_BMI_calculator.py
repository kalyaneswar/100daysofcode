 # BMI = Wt(kg)/(ht*ht)(meter sqr)
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight)/(float(height)* float(height))
print(round(BMI))