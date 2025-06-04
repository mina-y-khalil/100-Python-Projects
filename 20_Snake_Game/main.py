from turtle import Turtle, Screen
from snake import Snake
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by: Mina Y, Khalil")
screen.tracer(0) # Stop auto-refresh

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()  # Refresh screen once
    time.sleep(0.1)



#TODO 03: Create snake food
#TODO 04: Detect collision with food
#TODO 05: Create a scoreboard
#TODO 06: Detect collision with wall
#TODO 07: Detect collision with tail





screen.exitonclick()