from turtle import Turtle   
import random 

COLOURS = ['blue', 'red', 'green', 'yellow', 'magenta', 'cyan', '']

class Cars(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.goto(random.randint(-280,280 ), random.randint(-280,280 ) )
        self.color(random.choice(COLOURS))
        self.speed(1)
        self.forward(10)


