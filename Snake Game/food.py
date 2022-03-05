import random
from turtle import Turtle 

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        self.goto(x,y)
