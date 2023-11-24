from turtle import Turtle
from typing import Tuple

FONT = ('Calibri', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(arg= f'Score: {self.score}', align=ALIGNMENT, font= FONT)
    def adding_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Score: {self.score}', align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg= "GAME OVER", align='center', font=('Arial', 36, 'normal'))
