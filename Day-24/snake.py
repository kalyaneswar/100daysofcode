from turtle import Turtle  # Importing Turtle graphics module

# Initial positions for the 3 segments of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Constant values for movement
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []  # List to hold all segments of the snake
        self.create_snake()  # Initialize the snake with segments
        self.head = self.segments[0]  # The first segment is considered the snake's head

    def create_snake(self):
        # Create the initial snake with 3 segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")  # Create a new turtle segment
        new_segment.color("white")  # Set the color of the segment
        new_segment.penup()  # Prevent drawing when moving
        new_segment.goto(position)  # Move to the starting position
        self.segments.append(new_segment)  # Add the segment to the snake list

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        # Move each segment to the position of the segment ahead of it
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment
            new_x = self.segments[seg_num - 1].xcor()  # Get x of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Get y of the segment in front
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment to that position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward in its current direction

    def up(self):
        # Change direction to up unless the snake is going down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change direction to down unless the snake is going up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change direction to left unless the snake is going right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change direction to right unless the snake is going left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
