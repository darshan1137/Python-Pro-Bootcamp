from turtle import Turtle, Screen

obj = Turtle()
new_screen = Screen()



def draw_shape(num_of_sides):
    angle = 360/ num_of_sides
    for _ in range(num_of_sides): 
        obj.forward(100)
        obj.right(angle)

for shape in range(3, 11):
    draw_shape(shape)

new_screen.exitonclick