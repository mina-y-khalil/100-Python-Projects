# 🕹️ Pong Game (Classic Arcade)

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/the-pong-game.jpg" alt="Artwork Grid Example" />
</p>

A Python-based recreation of the classic Pong arcade game using the `turtle` graphics module. Two players control paddles on opposite sides of the screen to bounce the ball and score points.

## 🎯 Project Goal

- Recreate a retro arcade game using Python
- Implement object-oriented design with multiple classes
- Practice real-time graphics, user input, and collision detection

## 🧠 Python Concepts Practiced

- **Object-Oriented Programming (OOP)**:
  - `Paddle`, `Ball`, and `Scoreboard` as separate classes
- **Inheritance**:
  - Custom classes extend `Turtle` for shared drawing behavior
- **Event-driven programming**:
  - `onkey()` and `listen()` handle paddle controls
- **Collision detection**:
  - Ball collision with walls and paddles using `.distance()` and `.xcor()`/`.ycor()`
- **Game loop & timing**:
  - `while` loop with `time.sleep()` and `screen.update()` for animation
- **Encapsulation & class responsibility**:
  - Each class manages its own state (score tracking, ball movement, paddle position)
- **Custom bounce logic**:
  - Ball reflects on collision and speeds up after each paddle hit

## 🎮 Controls

- **Right Paddle**:  
  - `Up Arrow` → Move Up  
  - `Down Arrow` → Move Down  

- **Left Paddle**:  
  - `W` → Move Up  
  - `S` → Move Down

## 📋 Game Mechanics

- The ball moves diagonally and bounces off walls and paddles.
- If the ball passes a paddle, the opposite player scores a point.
- Score is updated and displayed in real-time.
- Ball resets to center after each score.

## 🛠 How to Run

Ensure the following files are in the same directory:
- `main.py`  
- `paddle.py`  
- `ball.py`  
- `scoreboard.py`

Then run:

```bash
python main.py
```

A game window will open. Use the keyboard to control the paddles and play against a friend.

---

Challenge a friend and relive the arcade days in Python! 🏓
