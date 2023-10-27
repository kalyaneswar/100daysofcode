# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
#Important You should not use the sum() or len() functions in your answer.
#You should try to replicate their functionality using what you have learnt about for loops.
total_count = 0
total_height = 0
for heights in student_heights:
    total_count += 1
    total_height += heights


avg_height = round(total_height/total_count)
print(f"total height = {total_height}")
print(f"number of students = {total_count}")
print(f"average height = {avg_height}")

