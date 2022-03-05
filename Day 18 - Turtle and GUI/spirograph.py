from turtle import Turtle, Screen 
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

obj = Turtle()


obj.speed(0)
for _ in range(100):
    obj.color(random_color())
    obj.circle(100)
    current_heading = obj.heading()
    obj.setheading(current_heading + 10)


screen = Screen()
screen.exitonclick