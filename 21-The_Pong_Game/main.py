#TODO 01: Create the screen
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("The Pong Game")
screen.tracer(0)



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#TODO 03: Create another paddle
#TODO 04: Create the ball and make it move
#TODO 05: Detect Collision with wall and bounce
#TODO 06: Detect when paddle misses
#TODO 07: Keep Score


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()