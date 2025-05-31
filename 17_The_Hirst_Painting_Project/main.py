import random
import turtle as turtle_module
from turtle import Turtle, Screen
import colorgram


# Using colorgram to extract RGB color tuples from an image.
# This section can be commented out after generating the color list once,
# to avoid reprocessing the image on every run.
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(120, 163, 215), (204, 161, 91), (212, 225, 83), (162, 168, 36), (118, 234, 154), (209, 125, 192), (204, 65, 177), (114, 200, 125), (181, 238, 203), (108, 92, 218), (233, 224, 184), (146, 93, 39), (192, 217, 239), (162, 55, 134), (176, 169, 237), (71, 177, 74), (229, 159, 216), (232, 196, 221), (77, 92, 160), (196, 227, 13), (220, 85, 59), (66, 127, 74), (112, 223, 237), (150, 17, 117), (65, 42, 154), (60, 164, 181), (78, 89, 21), (145, 35, 21), (247, 166, 151), (79, 27, 76)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









#draft and practicing only
# timmy_the_turtle = Turtle()
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
# turtle.colormode(255)
# def random_color ():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r , g, b)
#     return color
#
#
# # directions = [0,90,180,270]
# # timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed(30)

# for _ in range(200):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.setheading(random.choice(directions))
#

#making a spirograph using turtle:
# def draw_spirograph (size_of_gab):
#     for _ in range (int(360 / size_of_gab)):
#         timmy_the_turtle.color(random_color())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gab)
#
# draw_spirograph(5)
#
#
#
#
screen = Screen()
screen.exitonclick()