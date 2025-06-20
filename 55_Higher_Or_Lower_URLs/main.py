from flask import Flask


app = Flask(__name__)

#Different routes using the app.route decorator
@app.route('/')
def hello_world():
    return 'Hello, World'

# creating a variable path and converting the path to a specific data type
@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'hello there {name}, you are {number} years old!'


if __name__ == '__main__':
    #Run the app in debug mode to auto-reload
    app.run(debug=True)