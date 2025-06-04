from turtle import Turtle, Screen
#Constants (written in ALL_CAPS)
STARTING_POSITIONS  = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        """#TODO 01: Create a snake body"""
        # snake body
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """#TODO 02: Move the snake"""
        for seg_num in range(len(self.segments) - 1, 0,-1):  # the first number here is the (start) the second number is the (stop) and the third number is (step)
            """Moves each segment to the position of the segment in front of it, starting from the tail"""
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)  # Moves the head (first segment) forward to keep the snake moving
