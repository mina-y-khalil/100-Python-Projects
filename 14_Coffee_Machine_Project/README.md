# ☕ Coffee Machine Program
<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/05/Coffee-Machine-Project.jpg" alt="Landing Page" />
</p>

This Python project simulates the operations of a real-world coffee machine. It manages drink orders, checks resources, processes coin-based payments, and outputs drinks with real-time inventory tracking. Perfect for learning procedural programming and system simulation.

## 🎯 Project Goal

- Simulate a basic coffee vending machine interface.
- Practice control flow, function-based programming, and resource management.
- Handle user input, validate transactions, and update system state.

## 🧠 Python Concepts Practiced

- `input()` for command-line user interaction
- Dictionaries for storing drink menus and resources
- Functions with parameters and return values
- `if-else` statements and loops
- Global variable handling
- Modularity and abstraction

## 📋 Features

1. **User Prompt**  
   Continuously prompts the user with:  
   ```
   What would you like? (espresso/latte/cappuccino):
   ```

2. **Turn Off Command**  
   Typing `off` shuts down the program — used by machine maintainers.

3. **Report Function**  
   Typing `report` displays current resource levels:
   ```
   Water: 100ml  
   Milk: 50ml  
   Coffee: 76g  
   Money: $2.5
   ```

4. **Resource Check**  
   Ensures there are enough ingredients before making a drink. If not, it shows:
   ```
   Sorry there is not enough water.
   ```

5. **Coin Processing**  
   Asks for coin input:
   - Quarters = $0.25  
   - Dimes = $0.10  
   - Nickles = $0.05  
   - Pennies = $0.01  
   Calculates total money inserted and checks against drink price.

6. **Transaction Validation**  
   - If insufficient funds: refunds and displays error.  
   - If sufficient funds: adds cost to total profit and returns change.

7. **Making Coffee**  
   - Deducts ingredients from resources.  
   - Confirms drink with:  
     ```
     Here is your latte ☕
     ```

## 🛠 How to Run

Make sure you have a `data.py` file containing:

- `resources` dictionary with ingredient stock
- `MENU` dictionary with drink info
- `profit` initialized to 0

Then run:

```bash
python coffee_machine_project.py
```
