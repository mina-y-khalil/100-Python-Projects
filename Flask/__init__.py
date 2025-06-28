from flask import Flask

app = Flask(__name__)
# print(__name__)

#when we add this below we will be able to start and end out code with the regular way without adding the environmental variables first

@app.route('/')
def hello_world():
    return '<h1>Hello Flask</h1>'

@app.route('/bye')
def say_bye():
    return '<h2>This is the bye bye page</h2>'

if __name__ == "__main__":
    app.run()