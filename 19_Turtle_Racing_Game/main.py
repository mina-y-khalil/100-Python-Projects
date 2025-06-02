from turtle import Turtle, Screen
import _random

screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70 , -40 , -10 , 20, 50, 80]
counting = 1
moving = 10

for turtle_index in range(0,5):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    counting += 1
    # tim.shape("turtle")
    tim.goto(x=-230, y=y_positions[turtle_index])



screen.exitonclick()