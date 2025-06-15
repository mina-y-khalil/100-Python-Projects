from turtle import Turtle, Screen
import pandas


turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

user_input = screen.textinput(title="Guess the State", prompt="What is your guess?")

if user_input in all_states:
    t = Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == user_input] #getting the row that matches the user input
    t.goto(state_data.x.item() , state_data.y.item() )
    t.write(user_input)








screen.exitonclick()