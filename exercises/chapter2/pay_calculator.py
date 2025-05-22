"""
pay_calculator.py
-----------------
Prompt the user for hours worked and hourly rate,
then print the gross pay.

How to run:
    python pay_calculator.py
"""

hours = float(input("Hours worked: "))
rate  = float(input("Hourly rate: "))
pay   = hours * rate

print(f"Gross pay: {pay}")
