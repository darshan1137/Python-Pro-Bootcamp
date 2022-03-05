from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_Forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def cleanup():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_Forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_right)
screen.onkey(key = "d", fun = move_left)
screen.onkey(key = "c", fun = cleanup)

screen.exitonclick()