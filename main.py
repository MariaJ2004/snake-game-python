from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True

pantalla_score=Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#Detectar cuando obtiene la comida
    if snake.segmentos[0].distance(food)<15:
        food.refresh()
        snake.extend()
        pantalla_score.increase_score()

#Detectar coliciones con la pared
    if snake.segmentos[0].xcor()>280 or snake.segmentos[0].xcor()<-280 or snake.segmentos[0].ycor()>280 or snake.segmentos[0].ycor()<-280:
        pantalla_score.reset()
        snake.reset()

    for segment in snake.segmentos[1:]:
        if snake.segmentos[0].distance(segment)<10:
            pantalla_score.reset()
            snake.reset()

screen.exitonclick()