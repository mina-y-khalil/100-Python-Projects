from turtle import Turtle, Screen
import _random

screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
counting = 1
turtle_name = "tim" + str(counting)
moving = 10

for turtle in colors:
    turtle_name = Turtle(shape="turtle")
    turtle_name.penup()
    turtle_name.color(turtle)
    counting += 1
    # tim.shape("turtle")
    turtle_name.left(10)
    turtle_name.setheading(0)
    turtle_name.goto(x=-230, y=(-100 +int(moving)))



screen.exitonclick()