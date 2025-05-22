"""
Chapter 2 ─ Exercises
=====================
"""
# ──────────────────────────────────────────────────────────────────────────────
# Exercise 2: Write a program that uses input to prompt a user for their name
# and then welcomes them.
# ──────────────────────────────────────────────────────────────────────────────

prompt = ('What is your name? ')
yourname = input(prompt)
print('Hello ' + yourname)

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 3: Write a program to prompt the user for hours and rater per hour
# to compute gross pay.
# ──────────────────────────────────────────────────────────────────────────────

hours_prompt = ('How many hours did you work? ')
hoursworked = input(hours_prompt)
rate_prompt = ('What is your hourly rate? ')
hourlyrate = input(rate_prompt)
grosspay = int(hoursworked) * int(hourlyrate)
print('Your gross pay is: ' + str(grosspay))

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 4: Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and
# the type (of the value of the expression).
# ──────────────────────────────────────────────────────────────────────────────

width = 17
height = 12.0

print('1. width // 2 = ' + str(width // 2))
print('2. width / 2.0 = ' + str(width/2.0))
print('3. height / 3 = ' + str(height/3))
print('4. 1 + 2 * 5 = ' + str(1 + 2 * 5))

# ──────────────────────────────────────────────────────────────────────────────
# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert it to Fahrenheit, and print out the converted temperature.
# ──────────────────────────────────────────────────────────────────────────────

temp_prompt = ('What is the temperature in Celsius? ')
Celsius = input(temp_prompt)
Fahrenheit = (float(Celsius) * 9/5) + 32
print('The temperature in Fahrenheit is: ' + str(Fahrenheit))
