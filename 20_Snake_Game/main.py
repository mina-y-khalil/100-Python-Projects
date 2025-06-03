#TODO 01: Create a snake body
from turtle import Turtle, Screen
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by: Mina Y, Khalil")
screen.tracer(0) # Stop auto-refresh


#snake body
starting_positions = [(0,0) , (-20,0), (-40,0)]
segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

#TODO 02: Move the snake
game_is_on = True
while game_is_on:
    screen.update()  # Refresh screen once
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


#TODO 03: Create snake food
#TODO 04: Detect collision with food
#TODO 05: Create a scoreboard
#TODO 06: Detect collision with wall
#TODO 07: Detect collision with tail





screen.exitonclick()