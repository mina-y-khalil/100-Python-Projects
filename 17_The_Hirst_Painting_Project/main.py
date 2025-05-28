from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("teal")
def square ():
    for _ in range (4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

# square()
# timmy_the_turtle.forward(200)
# square()

def star ():
    for _ in range (5):
        timmy_the_turtle.right(72)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(72)


star()


screen = Screen()
screen.exitonclick()

