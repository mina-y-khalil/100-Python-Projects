import random
import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("teal")
# def square ():
#     for _ in range (4):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(90)
#
# # square()
# # timmy_the_turtle.forward(200)
# # square()
#
# def star ():
#     for _ in range (5):
#         timmy_the_turtle.right(72)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(72)


# star()


# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#
# def draw_shape(num_sides):
#     for _ in range (num_sides):
#         angel = 360 / num_sides
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angel)
#
# for shape_side_n in range (3, 11):
#     turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)
#
#

#
#NWES
turtle.colormode(255)
def random_color ():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r , g, b)
    return color


# directions = [0,90,180,270]
# timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(30)

# for _ in range(200):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.setheading(random.choice(directions))
#

#making a spirograph using turtle:
def draw_spirograph (size_of_gab):
    for _ in range (int(360 / size_of_gab)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gab)

draw_spirograph(5)




screen = Screen()
screen.exitonclick()