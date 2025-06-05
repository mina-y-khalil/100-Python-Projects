from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# How the screen should behave
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by: Mina Y, Khalil")
screen.tracer(0) # Stop auto-refresh

snake = Snake( )
food = Food()
scoreboard = Scoreboard()

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

#TODO 04: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#TODO 06: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


#TODO 07: Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()