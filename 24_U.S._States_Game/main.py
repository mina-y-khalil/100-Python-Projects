from turtle import Turtle, Screen
import pandas


turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)



user_input = screen.textinput(title="Guess the State", prompt="What is your guess?")








screen.exitonclick()