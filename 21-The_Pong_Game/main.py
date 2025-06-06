#TODO 01: Create the screen
from ctypes.macholib.dyld import dyld_default_search
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("The Pong Game")

#TODO 02: Create and move a paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() +20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() -20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")



#TODO 03: Create another paddle
#TODO 04: Create the ball and make it move
#TODO 05: Detect Collision with wall and bounce
#TODO 06: Detect when paddle misses
#TODO 07: Keep Score




screen.exitonclick()