"""
Grade calculator 

This program will calculate a user's grade. 

Author Owen Read
"""

grade = int(input("What is your grade? "))
letter_grade = ''
grade_sign = ''

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60: 
    letter_grade = 'D'
else:
    letter_grade = 'F'


remander = grade % 10

if remander >= 7:
    grade_sign = "+"
elif remander < 3:
    grade_sign = "-"
else:
    grade_sign = ""

if grade >= 97:
    grade_sign = ""
elif letter_grade == "F":
    grade_sign = ""
else:
    grade_sign = grade_sign


print(f'You have a grade of {letter_grade}{grade_sign}.')
# 97 / 10 = 9 with remander of 7.

if grade >= 70:
    print("You have passed the course!")
else:
    print("You have not passed the course, please try again.")