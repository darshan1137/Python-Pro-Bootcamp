import random
from turtle import Turtle, Screen

import turtle as t
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

move = [0, 90, 180, 270]

obj = Turtle()
obj.speed(0)
obj.pensize(10)
for _ in range(100):
    new_move = random.choice(move)
    obj.forward(30)
    obj.setheading(new_move)
    

    obj.color(random_color())


screen = Screen()
screen.exitonclick


