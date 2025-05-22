"""
temperature_convert.py
----------------------
Convert Fahrenheit to Celsius.

How to run:
    python temperature_convert.py
"""

fahrenheit = float(input("Enter temperature in °F: "))
celsius    = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
