student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for marks in student_scores:
    if student_scores[marks] >90 and student_scores[marks] <=100:
        student_grades[marks] = "Outstanding" 
    elif student_scores[marks] >80 and student_scores[marks] <=90:
        student_grades[marks] ="Exceeds Expectations"
    elif student_scores[marks] >70 and student_scores[marks] <=80:
        student_grades[marks] ="Acceptable"
    elif student_scores[marks] <=70:
        student_grades[marks] ="Fail"

print(student_grades)


