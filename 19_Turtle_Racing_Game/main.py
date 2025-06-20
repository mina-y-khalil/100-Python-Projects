import random
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("lightblue")

screen.setup(500, 400,  startx=None, starty=None)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Choose a color from the following list {colors}: ").lower()
all_turtles = []
y_positions = [-70 , -40 , -10 , 20, 50, 80]
counting = 1
moving = 10
is_race_on = False

for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    counting += 1
    # tim.shape("turtle")
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()