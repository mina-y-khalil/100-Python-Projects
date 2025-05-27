# 🧠 Python Quiz Game
<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/05/quiz-game.jpg" alt="Landing Page" />
</p>

This is a terminal-based Python quiz game that asks users a series of computer science trivia questions and keeps track of their score. The game uses object-oriented programming to manage questions, answers, and game logic.

## 🎯 Project Goal

- Practice object-oriented programming (OOP) in Python.
- Work with structured data (question sets) and user input.
- Build a modular quiz system with reusable components.

## 🧠 Python Concepts Practiced

- Class creation and object instantiation
- Encapsulation using methods
- Looping and conditional logic
- User input and score tracking
- Data parsing from list of dictionaries

## 📦 Files and Components

### `question_model.py`
Defines the `Question` class:
```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

### `quiz_brain.py`
Contains the game engine logic in the `QuizBrain` class:
- Loops through each question
- Handles input, scoring, and answer validation

### `data.py`
Stores the list of questions in a dictionary format.

### `main.py`
Main script that:
- Parses the question data
- Creates question objects
- Starts the game loop

---

## 🎮 How It Works

1. Loads a list of question dictionaries from `data.py`
2. Each question is turned into a `Question` object
3. The `QuizBrain` class handles the quiz logic:
   - Displays the current question
   - Accepts user input (True/False)
   - Checks if the answer is correct
   - Updates the score
4. Ends with a final score display after all questions are answered

---

## 🛠 How to Run

```bash
python main.py
```

Ensure the following files are in the same directory:
- `main.py`
- `data.py`
- `question_model.py`
- `quiz_brain.py`

---

Enjoy the quiz and test your tech knowledge! 🧑‍💻📚
