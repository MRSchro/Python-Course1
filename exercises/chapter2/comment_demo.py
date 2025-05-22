"""
comment_demo.py
---------------
Demonstrate inline comments, block comments, and docstrings.
(No console I/O.)
"""

# This is an inline comment explaining the next line:
answer = 42

def greet(name: str) -> None:
    """Return a friendly greeting."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("World")
