"""
"""
#Chapter 1:
"""
# ── Example 1: print and input ──────────────────────────────────────────────
print("Hello, World!")
name = input("What is your name? ")
print("Nice to meet you, ", name)

# ── Example 2: arithmetic ───────────────────────────────────────────────────
a, b = 5, 2
print("5 ** 2 =", a ** b)      # exponent
print("5 // 2 =", a // b)      # floor division

"""
#Chapter 2:
"""
x = 1 + 2 * 3 - 8 / 4
print(x)  # 1 + 6 - 2 = 5.0

x = int(98.6)
print(x)

"""
#Chapter 3:
"""

x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
x is y # x is the same as y
x is not y # x is not the same as y
"""

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)

try:
    if h > 40:
        pay = ((h-40) * (r * 1.5)) + (40 * r)
        print(pay)
    elif h <= 40:
        pay = h * r
        print(pay)
except ValueError:
    print("Must be a number value")
