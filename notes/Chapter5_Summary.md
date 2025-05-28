# 📖 Python for Everybody — Chapter 5: Iteration

| Key idea | One-sentence takeaway |
|----------|-----------------------|
| **`while` loop** | Repeats a block as long as the Boolean condition stays `True`. |
| **`for … in` loop** | Iterates over each element of a sequence (string, list, tuple, range, file, etc.). |
| **`break`** | Exits the nearest enclosing loop immediately. |
| **`continue`** | Skips the rest of the current iteration and jumps to the next one. |
| **Infinite loops** | A `while` with an always-true condition (`while True:`) must include a `break` or `return` inside or it runs forever. |
| **Loop variables & scope** | The loop index (e.g., `for x in …`) is overwritten on every iteration and remains defined *after* the loop ends. |
| **Iteration patterns** | Common patterns include running totals, searching for a maximum/minimum, counting, and validating input. |

---

## 🔑 Syntax Cheatsheet

```python
# while loop
count = 0
while count < 5:
    print("count =", count)
    count += 1

# for … in loop
for char in "hello":
    print(char)

# range() helper: range(stop) or range(start, stop[, step])
for i in range(1, 10, 2):      # 1, 3, 5, 7, 9
    print(i)

# break & continue
for num in range(10):
    if num == 5:
        break          # exits loop entirely
    if num % 2 == 0:
        continue       # skip even numbers
    print(num)         # prints 1, 3
