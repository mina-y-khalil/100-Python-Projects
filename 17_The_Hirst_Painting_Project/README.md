# 🖼️ Hirst Spot Painting Generator

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/05/github.jpg" alt="Artwork Grid Example" />
</p>

## 🎨 About Hirst's Spot Paintings

Damien Hirst, a British contemporary artist, is known for his **Spot Paintings** — large-scale works filled with rows of evenly spaced, brightly colored dots. Each spot is a different color, placed with machine-like precision. These paintings explore ideas of uniformity, randomness, repetition, and human perception.

---

## 🎯 Project Goal

- Recreate the visual concept of Hirst’s Spot Paintings using Python.
- Practice drawing with the Turtle graphics module.
- Work with RGB color extraction using the `colorgram` library.
- Build a grid-based layout algorithm using loops and positioning.

## 🧠 Python Concepts Practiced

- `turtle` graphics (`Turtle`, `Screen`, `colormode`)
- Randomization with `random.choice()`
- Image processing with `colorgram.py`
- For loops and grid generation
- Coordinate-based movement and heading management

## 📦 How It Works

- `colorgram.py` is used to extract dominant RGB colors from an image.
- A `Turtle` object draws 100 evenly spaced colored dots in a 10x10 grid.
- Each dot is selected randomly from the extracted color palette.
- The turtle moves across and down the screen, maintaining alignment using headings.

## 🛠 How to Run

1. Install dependencies:

```bash
pip install colorgram.py
```

2. Place an image named `image.jpg` in the project directory.
3. Run the script:

```bash
python main.py
```

The output will appear in a Turtle window. Click the window to exit.

---

Enjoy creating generative art with Python! 🎨🐍
