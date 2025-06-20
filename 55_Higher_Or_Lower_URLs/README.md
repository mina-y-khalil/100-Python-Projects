# 🔢 Flask Number Guessing Game

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/Higher_Or_Lower_URLs.jpg" alt="Artwork Grid Example" />
</p>

A dynamic Flask web app that challenges users to guess a random number between 0 and 9 by typing it directly in the URL. The app responds with immediate visual feedback using text and GIFs, simulating an interactive "higher or lower" experience.

## 🎯 Project Goal

- Build a lightweight interactive game using Flask and Python.
- Learn to handle dynamic routes and return custom HTML responses.
- Apply decorators and simple backend logic in a creative way.

## 🧠 Python Concepts Practiced

- `@app.route()` decorators for defining routes
- Capturing dynamic path parameters (e.g., `/3`)
- Conditional logic and flow control
- Custom function decorators (`make_bold`)
- Using external media (GIFs) with HTML responses
- Flask debug mode for rapid development

## 🌐 How It Works

1. The homepage (`/`) displays:
   - A centered welcome message
   - A prompt to guess a number
   - A fun GIF from Giphy

2. The app generates a secret number between 0–9 at runtime.

3. When the user visits a path like `/4`, the app:
   - Compares the guess to the secret number
   - Returns an `<h1>` with a result message
   - Shows a corresponding reaction GIF:
     - ✅ Correct: celebratory GIF
     - 🔺 Too High: warning GIF
     - 🔻 Too Low: encouraging GIF

4. Colors change dynamically based on the result.

## 🖼️ Example Feedback

| Guess | Result         | Visual |
|-------|----------------|--------|
| `/3`  | Too low        | <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="150"/> |
| `/7`  | Too high       | <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="150"/> |
| `/5`  | Just right 🎯  | <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="150"/> |

## 🛠 How to Run

Install Flask if needed:

```bash
pip install flask
```

Run the app:

```bash
python main.py
```

Open your browser at:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)  
Then enter `/0`, `/1`, ..., `/9` to play!
