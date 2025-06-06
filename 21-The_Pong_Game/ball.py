from  turtle import Turtle

#TODO 04: Create the ball and make it move
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() +10
        new_y = self.ycor() +10
        self.goto(new_x,new_y)