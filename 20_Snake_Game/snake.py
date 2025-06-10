from turtle import Turtle, Screen
#Constants (written in ALL_CAPS)
STARTING_POSITIONS  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.speed("slow")

    def create_snake(self):
        """#TODO 01: Create a snake body"""
        # snake body
        for position in STARTING_POSITIONS:
            self.add_Segment(position)


    def add_Segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """add a new segment to the snake"""
        position = self.segments[-1].position()
        self.add_Segment(position)

    def move(self):
        """#TODO 02: Move the snake"""
        for seg_num in range(len(self.segments) - 1, 0,-1):  # the first number here is the (start) the second number is the (stop) and the third number is (step)
            """Moves each segment to the position of the segment in front of it, starting from the tail"""
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_DISTANCE)  # Moves the head (first segment) forward to keep the snake moving

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
