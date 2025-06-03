#TODO 01: Create a snake body
from turtle import Turtle, Screen

#snake body
tim = Turtle(shape="square")
tim.penup()
tim.color("white")

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by: Mina Y, Khalil")



#TODO 02: Move the snake
def forward ():
    tim.forward(10)
screen.listen()
screen.onkey(key="w", fun=forward)


#TODO 03: Create snake food
#TODO 04: Detect collision with food
#TODO 05: Create a scoreboard
#TODO 06: Detect collision with wall
#TODO 07: Detect collision with tail





screen.exitonclick()