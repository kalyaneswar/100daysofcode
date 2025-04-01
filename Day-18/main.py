from turtle import Turtle, Screen

timmy = Turtle()

def triangle():
    timmy.color("red")
    for _ in range(3):
        timmy.forward(100)
        timmy.left(120)

def square():
    timmy.color("blue")
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)


def pentagon():
    timmy.color("green")
    for _ in range(5):
        timmy.forward(100)
        timmy.left(72)

def hexagon():
    timmy.color("yellow")
    for _ in range(6):
        timmy.forward(100)
        timmy.left(60)

def heptagon():
    timmy.color("black")
    for _ in range(7):
        timmy.forward(100)
        timmy.left(360 / 7)  # 51.43°

def octagon():
    timmy.color("pink")
    for _ in range(8):
        timmy.forward(100)
        timmy.left(45)

def nonagon():
    timmy.color("green")
    for _ in range(9):
        timmy.forward(100)
        timmy.left(40)

def decagon():
    timmy.color("grey")
    for _ in range(10):
        timmy.forward(100)
        timmy.left(36)

def straight_line():
    for _ in range(10):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

# Call the functions to draw shapes

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

# Screen setup
screen = Screen()
screen.exitonclick()
