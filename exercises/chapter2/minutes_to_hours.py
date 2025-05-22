"""
minutes_to_hours.py
-------------------
Convert minutes to hours + minutes (e.g. 135 → 2 hours 15 minutes).

How to run:
    python minutes_to_hours.py
"""

total_minutes = int(input("Enter minutes: "))

hours   = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hour(s) {minutes} minute(s)")
