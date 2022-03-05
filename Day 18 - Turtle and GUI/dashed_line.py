from turtle import Turtle, Screen

obj = Turtle()
screen = Screen()

for i in range(0, 50):
    obj.forward(5)
    obj.penup()
    obj.forward(5)
    obj.pendown()

screen.exitonclick