from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment_coordinate in COORDINATES:
            if segment_coordinate == (0, 0):
                self.add_segment(segment_coordinate, True)
            else:
                self.add_segment(segment_coordinate)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position, is_head=False):
        fig = "square"
        if is_head:
            fig = "circle"
        new_segment = Turtle(fig)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # def create_snake(self):
    #     for segment_coordinate in COORDINATES:
    #         self.add_segment(segment_coordinate)
    #
    #     for i in range(15):
    #         self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE)

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