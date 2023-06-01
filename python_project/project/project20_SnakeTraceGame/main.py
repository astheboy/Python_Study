from turtle import Screen
import time
import random
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game!")
screen.tracer(0)  # Turns off the screen updates

game_is_on = True
score = 0

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")


while game_is_on:
    screen.update()  # Updates the screen
    time.sleep(0.1)  # Slows down the game
    snake.trace_move()
    
    if (
        snake.all_snakes[0].pos()[0] > 280
        or snake.all_snakes[0].pos()[1] > 280
        or snake.all_snakes[0].pos()[0] < -280
        or snake.all_snakes[0].pos()[1] < -280
    ):
        game_is_on = False
        print("Game Over")
        score.game_over()
    if (
        snake.all_snakes[0].distance(food) < 15
    ):  # 뱀의 머리와 음식의 거리를 확인하여 충돌 여부를 검사합니다.
        
        snake.grow_snake()  # 뱀의 꼬리 추가
        food.refresh()  # 음식을 새로운 위치로 이동
        score.increase_score()  # 점수 증가
        print(score)




screen.exitonclick()
