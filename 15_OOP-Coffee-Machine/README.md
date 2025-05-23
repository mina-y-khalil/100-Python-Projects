# ☕ OOP Coffee Machine Program
<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/05/oop-coffee-machine.jpg" alt="Landing Page" />
</p>

This project is a refactored version of the Coffee Machine simulation, using Object-Oriented Programming (OOP) principles. It separates logic into modular classes for better organization, reuse, and readability.

## 🎯 Project Goal

- Implement object-oriented principles to structure code more cleanly.
- Simulate a real coffee machine using class-based models.
- Enhance maintainability and scalability of procedural logic.

## 🧠 Python Concepts Practiced

- Object-Oriented Programming (classes, objects, methods)
- Composition and abstraction through multiple files
- Loops and conditionals
- Input handling and flow control

## 🧩 Class Architecture

### ✅ `MenuItem` Class  
Represents a drink on the menu.  

**Attributes**:
- `name` (str): The drink name (e.g., `"latte"`)
- `cost` (float): Price of the drink (e.g., `1.5`)
- `ingredients` (dict): Required ingredients  
  Example: `{"water": 100, "coffee": 16}`

---

### ✅ `Menu` Class  
Manages the list of available drinks.  

**Methods**:
- `get_items()` → Returns available drink names as a string.  
  Example: `"latte/espresso/cappuccino"`
- `find_drink(order_name)` → Returns the corresponding `MenuItem` object if found, else `None`.

---

### ✅ `CoffeeMaker` Class  
Handles resources and brewing logic.  

**Methods**:
- `report()` → Prints current resource levels  
  Example:
  ```
  Water: 300ml  
  Milk: 200ml  
  Coffee: 100g
  ```
- `is_resource_sufficient(drink)` → Checks ingredient availability for the drink. Returns `True` or `False`.
- `make_coffee(order)` → Deducts ingredients and serves the drink.

---

### ✅ `MoneyMachine` Class  
Handles payment processing and profit tracking.  

**Methods**:
- `report()` → Displays total earnings  
  Example: `Money: $2.50`
- `make_payment(cost)` → Accepts coins from user. Returns `True` if payment is successful, `False` otherwise.

---

## 📋 Program Flow

1. Display available drink options from the menu.
2. Accept user input:
   - `"report"` → Display resource and money status.
   - `"off"` → Shut down the machine.
   - Valid drink name → Proceed with:
     - Checking ingredient availability
     - Requesting and verifying payment
     - Brewing and serving the drink
3. Loop continues until `"off"` is entered.

## 🛠 How to Run

Ensure the following files exist in your project:
- `menu.py` (with `Menu` and `MenuItem` classes)
- `coffee_maker.py` (with `CoffeeMaker` class)
- `money_machine.py` (with `MoneyMachine` class)

Then run:

```bash
python main.py
```

## 🚀 Upcoming updates

- Add refill options for maintainers.
- Save sales data to a file.
- Add error handling for invalid drink names.

---

Enjoy your clean OOP coffee code! ☕💻
