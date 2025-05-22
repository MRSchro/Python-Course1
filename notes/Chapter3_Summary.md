# 📖 Python for Everybody — Chapter 3: Conditional Execution

| Key idea | One-sentence takeaway |
|----------|-----------------------|
| **`if / elif / else`** | Control flow chooses which block of code executes based on Boolean tests. |
| **Boolean expressions** | Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`) evaluate to `True` or `False`. |
| **Indentation matters** | A colon (`:`) starts a suite; everything indented under it is part of that branch. |
| **Nested conditionals** | `if` inside `if` lets you build multi-level decisions. |
| **Logical operators** | `and`, `or`, `not` combine or negate Boolean expressions. |
| **`try / except`** | Gracefully handle runtime errors (e.g., invalid input) without crashing the program. |
| **Short-circuit evaluation** | In `A and B`, Python skips evaluating `B` if `A` is already false (and vice-versa for `or`). |

---

## 🔑 Syntax Cheatsheet

```python
# Basic pattern
if x > 10:
    print("bigger")
elif x == 10:
    print("equal")
else:
    print("smaller")

# Multiple conditions with logical operators
if age >= 18 and country == "US":
    print("You can vote!")

# Error handling
try:
    hours = float(input("Hours: "))
    rate  = float(input("Rate : "))
    pay   = hours * rate
    print("Pay:", pay)
except ValueError:
    print("Please enter numeric input.")
