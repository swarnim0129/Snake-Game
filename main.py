from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
segments=[]
screen.tracer(0)

food=Food()
scoreboard=ScoreBoard()
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()                  #adds new food on random location
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    for segment in snake.segments:
        if snake.head==segment:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset_score()
            snake.reset_snake()
            snake.move()











screen.exitonclick()