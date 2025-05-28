from ast import Try
import math
import random

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 1: Write a program which repeatedly reads integers until the user
# eneters "done". Once "done" is entered, print out the total, count, and average
# of the integers. If the user enters anything other than an integer, detect their
# mistake using try and except and print an error message and skip to the next
# integer.
# ──────────────────────────────────────────────────────────────────────────────
"""
total = 0
cnt_number = 0

while True:
    int_input = input("Enter a number: ")
    if int_input == "done":
        break
    try:
        int_entered = float(int_input)
    except ValueError:
        print("Invalid input")
        continue
    total = total + int(int_input)
    cnt_number = cnt_number + 1

print(str(total) + " " + str(cnt_number) + " " + str(total/cnt_number))
"""

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.
# ──────────────────────────────────────────────────────────────────────────────
"""
total = 0
cnt_number = 0
min_numb = 0
max_numb = 0

while True:
    int_input = input("Enter a number: ")
    if int_input == "done":
        break
    try:
        int_entered = float(int_input)
        if cnt_number == 0:
            min_numb = int_entered
    except ValueError:
        print("Invalid input")
        continue
    if int_entered > max_numb:
        max_numb = int_entered
    if int_entered < min_numb:
        min_numb = int_entered
    total = total + int(int_input)
    cnt_number = cnt_number + 1

print(str(total) + " " + str(cnt_number) + " " + str(min_numb) + " " + str(max_numb))
"""
