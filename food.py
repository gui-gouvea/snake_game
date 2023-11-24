# Everytime the snake hits the food, it will generate a new one in a new location.

from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    def refresh(self): # creating a piece of food in a new location
        random_x = randint(-14, 14)
        random_y = randint(-14, 14)
        self.goto(random_x*20, random_y*20)
