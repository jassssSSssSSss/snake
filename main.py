from turtle import Screen 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game YAY")
screen.tracer(0)

snakey = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakey.up,"Up")
screen.onkey(snakey.down,"Down")
screen.onkey(snakey.left,"Left")
screen.onkey(snakey.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snakey.move()

    #detect collision w food 
    if snakey.head.distance(food) < 15:
        food.refresh()
        snakey.extend()
        scoreboard.increase_score()
    
    #detect collision w wall
    if snakey.head.xcor() > 290 or snakey.head.xcor() < -290 or snakey.head.ycor() > 290 or snakey.head.ycor() < -290:
        game_is_on = False 
        scoreboard.game_over()

    #detect collision w tail. if head collides w any segment in tail, trigger game over 
    for segment in snakey.segments[1:]:
    #use slicing to remove first segment which is snakey head!
        if snakey.head.distance(segment) < 15:
            game_is_on = False 
            scoreboard.game_over()

        


    


 
screen.exitonclick()