"""
Create a variable (grade) holding an integer 0-100
code if if-else, statements to print the letter grade of the nuber grade variable

grades:
 a=90-100
 b=80-89
 c=70-79
 d=60-69
 f=0-59
"""

grade = 85

if 90 <= grade < 100:
    print('A')
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 79:
    print("C")
elif 60 <= grade < 69:
    print("D")
elif 0 < grade < 59:
    print("F")
else:
    print("USE LESS")