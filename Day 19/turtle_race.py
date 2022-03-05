from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(500, 400)
user = screen.textinput(title = "Make your Bet", prompt = "Which turtle will win the Race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = [-75, -40, -10, 20, 50, 80 ]

turtles = []
for new_object in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[new_object])
    tim.penup()
    tim.goto(-230, pos[new_object])
    turtles.append(tim)

if user:
    race = True
while race:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if user == winner:
                print("You won");
            else:
                print("You Lost")


        distance = random.randint(0,10)
        turtle.forward(distance)
        


screen.exitonclick()
