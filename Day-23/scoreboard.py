from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT='left'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.level = 1
        self.color("black")
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        # self.clear()
        self.write(f"Level: {self.level}",  align=ALIGNMENT, font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",  align="center", font=FONT)


