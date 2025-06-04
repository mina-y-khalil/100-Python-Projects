from turtle import Screen
from snake import Snake
import time
from food import Food

# How the screen should behave
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by: Mina Y, Khalil")
screen.tracer(0) # Stop auto-refresh

snake = Snake( )
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# How the snake should behave
game_is_on = True
while game_is_on:
    screen.update()  # Refresh screen once
    time.sleep(0.05)

    snake.move()


#TODO 03: Create snake food
#TODO 04: Detect collision with food
#TODO 05: Create a scoreboard
#TODO 06: Detect collision with wall
#TODO 07: Detect collision with tail





screen.exitonclick()