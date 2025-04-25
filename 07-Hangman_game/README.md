# 🐾 Hangman Game - Animal Edition
<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/04/Hangman-Game-Animal-Edition.jpg" alt="Landing Page" />
</p>

This project is a Python implementation of the classic Hangman game, themed around animal names. It challenges users to guess a hidden word one letter at a time while keeping track of incorrect guesses visually with ASCII art.

## 🎯 Project Goal

- Practice control flow with loops and conditionals.
- Improve string and list manipulation skills.
- Introduce modular coding by importing assets (word list and art) from separate files.

## 🧠 Python Concepts Practiced

- `import` statement to bring in external modules (`hangman_words`, `hangman_art`)
- `input()` and `str.lower()` for user interaction
- `random.choice()` for random word selection
- `for` loops for iteration
- `if-elif-else` logic
- String concatenation and list handling
- Managing game state with Boolean flags

## 📋 Features

- Randomly selects an animal name as the secret word.
- Displays a placeholder (underscores) for unguessed letters.
- Tracks and displays correctly guessed letters.
- Penalizes wrong guesses by decreasing a score and updating hangman stages.
- Ends the game with a win if the word is guessed or a loss if guesses run out.

## 🛠 How to Run

Make sure you also have the supporting files:
- `hangman_words.py` (animal word list)
- `hangman_art.py` (ASCII stages and logo)

Then run:

```bash
python hangman_game.py
This project has not been completed yet.