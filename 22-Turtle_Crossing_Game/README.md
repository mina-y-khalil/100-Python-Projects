# 🐢 Turtle Crossing Game

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/turtle-crossing.jpg" alt="Artwork Grid Example" />
</p>

Inspired by the classic game "Frogger," this Turtle Crossing Game challenges players to cross a road full of moving cars without getting hit. Each successful crossing increases the speed of traffic and the game level.

## 🎯 Project Goal

- Implement a multi-class arcade game using Python and Turtle graphics
- Apply event-driven movement and object interaction
- Practice OOP structure with inheritance and modular logic

## 🧠 Python Concepts Practiced

- **Object-Oriented Programming (OOP)**: Classes for `Player`, `CarManager`, and `Scoreboard`
- **Inheritance**: Extending `Turtle` to build reusable objects
- **Encapsulation**: Grouping logic into class methods (e.g., `move_cars()`, `is_at_finish_line()`)
- **Event listeners**: `screen.onkey()` for movement controls
- **Game loop**: Using `while` and `time.sleep()` to manage updates
- **Collision detection**: Measuring `distance()` between turtles
- **Screen updates**: Managing with `tracer()` and `update()` for smooth animation
- **Dynamic difficulty**: Cars move faster with each level (`level_up()`)

## 📋 Game Mechanics

- Player controls a turtle starting at the bottom of the screen.
- Cars randomly appear from the right and move left.
- Each time the player crosses successfully:
  - The level increases
  - Car speed increases
- Game ends on collision with a car.

## 🎮 Controls

- `Up Arrow` – Move the turtle forward

## 🛠 How to Run

Make sure the following files are in the same directory:
- `main.py`  
- `player.py`  
- `car_manager.py`  
- `scoreboard.py`

Then run:

```bash
python main.py
```

Use the Up arrow key to move the turtle. Avoid the cars and try to survive as long as you can. Click the screen to exit after the game ends.

---

Cross the road, dodge traffic, and level up! 🚗🐢
