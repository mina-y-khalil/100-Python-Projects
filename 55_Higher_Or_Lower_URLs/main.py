from flask import Flask
import random


app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        content = function()
        return f'<b>{content}</b>'
    return wrapper_function

random_number = random.randint(0,9)
# print(random_number)


#Different routes using the app.route decorator
@app.route('/')
def home():
    return ('<h1 style="text-align:center">Hello</h1>'
            '<p style="text-align:center">Guess a number between 0 and 9.</p>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" ">')


# creating a variable path and converting the path to a specific data type
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"






if __name__ == '__main__':
    #Run the app in debug mode to auto-reload
    app.run(debug=True)