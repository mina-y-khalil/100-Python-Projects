# 🐍 Classic Snake Game

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/snake-game.jpg" alt="Artwork Grid Example" />
</p>

A recreation of the classic Snake Game using Python's `turtle` module. The player controls the snake with arrow keys, eats food to grow longer, and avoids crashing into walls or its own tail.

## 🎯 Project Goal

- Build a modular game using object-oriented programming
- Apply concepts like collision detection, movement logic, and event listeners
- Understand real-time screen refresh and game loop logic

## 🧠 Python Concepts Practiced

- **Object-Oriented Programming (OOP)**: Custom classes for `Snake`, `Food`, and `Scoreboard`
- **Class inheritance**: Using `super().__init__()` from the `Turtle` class
- **Encapsulation**: Methods like `move()`, `extend()`, `up()`, `down()` handle state changes internally
- **Event-driven programming**: Using `onkey()` and `listen()` to control the snake
- **Collision detection**: Using `distance()` to check food and self-collisions
- **Game loops and timing**: Using `while` loops with `time.sleep()` and `screen.update()`
- **Constants**: Defined with UPPERCASE (e.g. `STARTING_POSITIONS`, `MOVE_DISTANCE`)
- **Graphics with turtle module**: Using shapes, coordinates, pen control, and screen properties
- **Scorekeeping and text rendering**: Drawing the scoreboard using `write()`

## 📋 Game Mechanics

- Snake moves continuously and responds to arrow key inputs.
- Eats randomly placed blue food to grow longer and increase score.
- Game ends when:
  - The snake hits the wall boundary
  - The snake hits its own tail
- Score is displayed at the top and updates in real time.

## 🎮 Controls

- `Up Arrow` – Move Up  
- `Down Arrow` – Move Down  
- `Left Arrow` – Move Left  
- `Right Arrow` – Move Right

## 🛠 How to Run

Make sure the following files are in the same directory:
- `main.py`  
- `snake.py`  
- `food.py`  
- `scoreboard.py`

Then run:

```bash
python main.py
```

Use the arrow keys to control the snake. Eat food to grow. Avoid the walls and your own tail. Click anywhere on the game window to exit.

---

Enjoy the nostalgia, now powered by Python! 🎮🐍
