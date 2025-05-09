# 🕵 Blind Auction Program
<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/05/09_Blind_Auction.jpg" alt="Landing Page" />
</p>

This Python project simulates a secret auction where multiple participants can place their bids anonymously. The highest bidder is revealed at the end. It’s a fun way to practice dictionaries, loops, and basic logic.

## 🎯 Project Goal

- Practice using dictionaries to store key-value data.
- Collect and process user input in a loop.
- Use conditionals and functions to determine the highest bidder.

## 🧭 Flowchart

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/05/blind_auction-map.jpg" alt="Secret Auction Flowchart" />
</p>


## 🧠 Python Concepts Practiced

- `input()` for user interaction
- `int()` for type conversion
- `while` loops for repeated entry
- `dict` for storing bids (`name: amount`)
- Function definition for bid evaluation
- `if-else` logic
- String formatting with `f-strings`

## 📋 Features

- Repeatedly prompts for names and bids.
- Stores bids in a dictionary.
- Clears screen between entries (via `print("\n" * 100)`).
- Ends when user types "no", then:
  - Finds the highest bidder.
  - Displays winner's name and bid amount.

## 🛠 How to Run

Make sure the `art.py` file includes the `logo` variable for the ASCII banner.

Then run:

```bash
python blind_auction.py
