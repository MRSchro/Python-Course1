# 📖 Python for Everybody — Chapter 4: Functions

| Key idea | One-sentence takeaway |
|----------|-----------------------|
| **What is a function?** | A reusable block of code that performs a specific task and can be “called” from anywhere. |
| **Built-ins vs. user-defined** | Python ships with many built-ins (`len`, `max`, `type`), but you can define your own with `def`. |
| **Parameters & arguments** | Parameters are placeholders in the `def` line; arguments are the actual values passed in at call time. |
| **`return` value** | A function can hand a value back to the caller with `return` (or return `None` implicitly). |
| **Why use functions?** | They let you avoid repetition, make code easier to test, and break big problems into bite-sized pieces. |
| **Scope** | Variables created inside a function are *local* and disappear when the function ends (unless returned). |
| **Docstrings** | Triple-quoted strings right after `def` describe what the function does—accessible via `help()`. |

---

## 🔑 Syntax Cheatsheet

```python
def function_name(param1, param2="default"):
    """
    Short description of what the function does.

    param1 (int): first value
    param2 (str): optional greeting
    return (str): formatted message
    """
    result = f"{param2}, you passed {param1}"
    return result

msg = function_name(42)              # positional + default
msg = function_name(param1=99,
                    param2="Hello")  # keyword args
print(msg)
