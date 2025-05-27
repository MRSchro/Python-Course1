import math
import random
print(math)

# ──────────────────────────────────────────────────────────────────────────────
# Ecercise 1: Run the program on your system and see what numbers you get. Run
# the program more than once and see what numbers you get.
# The random function is only one of man functions that handle rrandom numbers.
# The function randint take s the parameters low and high, and returns an integer
# between low and high (including both).
# ──────────────────────────────────────────────────────────────────────────────
"""
print(">>> random.randint(5, 10) = ", random.randint(5, 10))
print(">>> random.randint(5, 10) = ", random.randint(5, 10))
"""
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 2: Move the last line of this program to the top, so the funciton call
# appears before the definitions. Run the program and see what error message you
# get.
# ──────────────────────────────────────────────────────────────────────────────

"""
repeat_lyrics() # moved this line from the bottom

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
"""
# error message received was: name 'repeat_lyrics' is not defined

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 3: Move the function call back to the bottom and move the definition
# of print_lyrics after the definition of repeat_lyrics. What happens when you
# run this program?
# ──────────────────────────────────────────────────────────────────────────────
"""
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
  
repeat_lyrics()

# the output is:
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
"""
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 4: What is the purpose of the "def" keyword in Python?
# b.) It indicates the start of a function.
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 5: What will the following Python program print out?
"""
def fred():
    print("Zap")

def jane():
    print("ABC")

jane()
fred()
jane()
"""
# d.) ABC Zap ABC
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters (hours and rate)
# ──────────────────────────────────────────────────────────────────────────────
"""
hrs_prompt = input("Enter Hours: ")
hrs = float(hrs_prompt)
rate_prompt = input("Enter Rate: ")
rate = float(rate_prompt)

def computepay(a,b):
    if a > 40:
        pay_amnt = ((a - 40) * (b * 1.5)) + (40 * b)
    elif a <= 40:
        pay_amnt = (a * b)
    return pay_amnt # type: ignore

x = computepay(hrs, rate)
print("Pay: " + str(x))
"""

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as
# a string.
# ──────────────────────────────────────────────────────────────────────────────

score_prompt = input('Enter score: ')

def computegrade(grade):
    try:
        enteredscore = float(grade)
        if float(enteredscore) > 0.0 and float(enteredscore) < 1.0:
            if enteredscore >= 0.9:
                gradedscore = print('A')
            elif enteredscore >= 0.8:
                gradedscore = print('B')
            elif enteredscore >= 0.7:
                gradedscore = print('C')
            elif enteredscore >= 0.6:
                gradedscore = print('D')
            else:
                gradedscore = print('F')
    except ValueError:
                print('Bad score')

computegrade(score_prompt)
