# ──────────────────────────────────────────────────────────────────────────────
# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
# ──────────────────────────────────────────────────────────────────────────────
"""
hours = input('How many hours did you work? ')
rate = 10

if int(hours) > 40:
    pay = (40 * rate) + ((int(hours) - 40) * rate * 1.5)
    print('Hours worked: ' + str(hours) + '\n' + 'Pay: ' + str(pay))
else:
    pay = int(hours) * rate
    print('Hours worked: ' + str(hours) + '\n' + 'Pay: ' + str(pay))
"""
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by using a try and except block.
# The following is an example of what your program should look like when it is done:
# 
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
#
# Enter Hours: forty
# Error, please enter numeric input
# ──────────────────────────────────────────────────────────────────────────────
"""
hrs_prompt = input('Enter Hours: ')
rate_prompt = input('Enter Rate: ')

try:
    hours = float(hrs_prompt)
    rate = float(rate_prompt)
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * rate * 1.5)
        print('Pay: ' + str(pay))
    else:
        pay = hours * rate
        print('Pay: ' + str(pay))
except ValueError:
    print('Error, please enter numeric input')
"""
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error. If the score is between 0.0 and
# 1.0, print a grade using the following table:
#
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#
# Enter score: 0.95
# A
#
# Enter score: perfect
# Bad score
#
# Enter score: 10.0
# Bad score
#
# Enter score: 0.75
# C
#
# Enter score: 0.5
# F
# ──────────────────────────────────────────────────────────────────────────────

score_prompt = input('Enter score: ')

try:
    if float(score_prompt) > 0.0 and float(score_prompt) < 1.0:
        score = float(score_prompt)
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
except ValueError:
                print('Bad score')