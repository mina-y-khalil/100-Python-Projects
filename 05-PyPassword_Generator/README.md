# 🔐 PyPassword Generator

This Python project generates a secure password based on user preferences. It allows users to specify the number of letters, symbols, and numbers in the password and provides both an easy and a hard version for password generation.

## 🎯 Project Goal

- Practice list handling and randomization.
- Build both structured and randomized password generators.
- Reinforce input handling and loop control.

## 🧠 Python Concepts Practiced

- `input()` and `int()` for interactive user input
- `random.choice()` and `random.shuffle()` from the `random` module
- `for` loops for iterative logic
- Lists and string manipulation

## 📋 Features

- Asks the user for:
  - Number of letters
  - Number of symbols
  - Number of numbers
- **Easy Mode** (commented out):
  - Password has characters in fixed order: letters → symbols → numbers.
- **Hard Mode**:
  - Characters are randomized for added security.
- Outputs the final password after shuffling.

## 🛠 How to Run

```bash
python py_password_generator.py
