# 🗺️ U.S. States Guessing Game

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/U.S.-States-Game-updated.jpg" alt="Artwork Grid Example" />
</p>

This interactive Python game challenges the user to name all 50 U.S. states. Each correct guess is labeled on a blank map of the United States using turtle graphics. The game ends when the user types "Exit," and it generates a study list of missing states.

## 🎯 Project Goal

- Practice working with graphical input/output in a fun geography quiz format.
- Reinforce skills in reading and filtering data with pandas.
- Apply turtle graphics for coordinate-based labeling.

## 🧠 Python Concepts Practiced

- **Turtle Graphics**: Displaying a static image and writing text dynamically on the map
- **CSV Data Handling**: Reading state names and coordinates using `pandas.read_csv()`
- **Data filtering**: Locating a row with `.loc[]` or boolean indexing (`data[data.state == user_input]`)
- **Lists**: Managing guessed states and calculating missing ones
- **Loops & Conditionals**: Handling game state logic
- **String formatting and title-casing**: `.title()` to normalize input
- **File Writing**: Saving unguessed states to `states_to_learn.csv`

## 📋 Game Mechanics

- Loads a blank U.S. map as a turtle shape (`.gif`)
- Prompts the user to guess a state
- Correct guesses appear on the map at their respective coordinates
- Typing `Exit` ends the game and creates `states_to_learn.csv` with remaining states

## 🛠 How to Run

Ensure the following files are in your project folder:
- `main.py`
- `50_states.csv` (with `state`, `x`, `y` columns)
- `blank_states_img.gif`

Then run:

```bash
python main.py
```

Type each U.S. state to see it labeled on the map. Exit the game to get a list of missed states in `states_to_learn.csv`.

---

Test your U.S. geography and visualize your progress in real-time! 🧠🗺️
