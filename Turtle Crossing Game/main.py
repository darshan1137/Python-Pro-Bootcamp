from turtle import Turtle, Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import Cars

screen =  Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0) 

player = Player()
obj = Cars()
scoreboard = Scoreboard()

game_is_on = True


screen.listen()
screen.onkeypress(player.move, "Up")

while game_is_on:
    screen.update() 
    time.sleep(0.1)
    

screen.exitonclick()

