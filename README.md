# Python for Everybody — Course 1  
*University of Michigan / Coursera*

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.13](https://img.shields.io/badge/Python-3.13+-blue)

> **Why this repo?**  
> I’m documenting my journey through Dr. Charles Severance’s **“Python for Everybody”** specialization.  
> This repository covers **Course 1: Programming for Everybody (Getting Started with Python)**.  
> You’ll find my annotated notes, practice exercises, mini-projects, and links to quizzes / assignments.

---

## 📚 Table of Contents

| Folder | What’s inside |
|--------|---------------|
| [`notes/`](notes/) | Markdown summaries of each week’s lectures (syntax, tips, gotchas). |
| [`exercises/`](exercises/) | My solutions to the practice problems (with docstrings & comments). |
| [`mini_projects/`](mini_projects/) | Small scripts that tie concepts together—number guessing game, text file analysis, etc. |

*(Folder names are suggestions—adjust to match your actual structure.)*

---

## 🧩 Mini-Projects Roadmap (Course 1)

- [ ] **Tip Calculator** – asks bill + percentage, prints total and per-person split  
- [ ] **Number Guessing Game** – random 1-100, counts guesses, gives high/low hints  
- [ ] **Unit Converter** – miles ↔ km, lbs ↔ kg, °F ↔ °C via menu loop  

---

## 🛠 Setup

```bash
# Clone the repo
git clone https://github.com/MRSchro/python-for-everybody-course1.git
cd python-for-everybody-course1

# Create & activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS / Linux

# No third-party packages required for Course 1.
# Just run scripts directly:
python exercises/week2_variables.py
