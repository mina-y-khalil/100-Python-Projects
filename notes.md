# Python Code Examples and Flask Setup

## 1. Dictionary Comprehensions

- Creating a dictionary from a list:
```python
new_dict = {new_key: new_value for item in list}
```

- Creating a dictionary from another dictionary's key-value pairs:
```python
new_dict = {new_key: new_value for (key, value) in dict.items()}
```

- Creating a dictionary with a condition:
```python
new_dict = {new_key: new_value for (key, value) in dict.items() if test}
```

## 2. Flask Environment Setup

To run the Flask application, we need to set up environment variables that tell Flask where the server file is located. Run the following commands in the terminal:

- **For macOS:**
```bash
export FLASK_APP=main.py
```

- **For Windows:**
```bash
set FLASK_APP=main.py
```

Then, use the following command to run Flask:
```bash
flask run
```

## 3. Flask Decorator Example

Here’s a decorator example that adds a delay before and after executing a function:

```python
import time

def decorative_function(function):
    def wrapper_function():
        # Do something before
        time.sleep(5)
        function()
        # Do something after
    return wrapper_function

@decorative_function
def say_hello():
    print("Hello")

say_hello()
```

### Explanation:
- **`decorative_function`** is a decorator that wraps the `say_hello()` function, adding a 5-second delay before and after its execution.
- **`@decorative_function`** is applied to `say_hello()` to modify its behavior.

### 🛠️ How to Edit a Website Directly from Chrome

To edit a website directly in Google Chrome:

1. Open the website in Chrome.
2. Press `Ctrl + Shift + I` (or right-click and select **Inspect**) to open Developer Tools.
3. In the Console tab, paste this command:
   ```javascript
   document.body.contentEditable = true;
   ```
4. You can now freely edit the page content like a normal document.
5. When finished, right-click on the page and select **Save As** to download it as an `.html` file.
6. Move the saved file into your project folder for further development.
