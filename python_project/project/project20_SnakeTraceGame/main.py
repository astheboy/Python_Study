from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game!")
screen.tracer(0)  # Turns off the screen updates

game_is_on = True
food_eaten = False
food_position = []
snake_num = 3
all_snakes = []
snake_positions = []
score = 0



def random_food_show():
    if food_eaten:
        for foods in food_position:
            foods.goto(x=1000, y=1000)
    food_position.clear()
    foods = Turtle(shape="circle")
    foods.color("red")
    foods.penup()
    foods.pensize(10)
    foods.goto(x=random.randrange(-260, 260, 20), y=random.randrange(-260, 260, 20))
    food_position.append(foods)

    return food_position


def start_snake():
    for i in range(snake_num):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.pensize(20)
        snake.goto(x=0 + (i * 20), y=0)
        all_snakes.append(snake)
        snake_positions.append(snake.pos())


def grow_snake():
    snake_tail = Turtle(shape="square")
    snake_tail.color("white")
    snake_tail.penup()
    snake_tail.pensize(20)
    snake_tail.goto(all_snakes[len(all_snakes) - 1].pos())
    all_snakes.append(snake_tail)


def head_move_up():
    for i, snake in enumerate(all_snakes):
        if i == 0 and snake.heading() != 270:
            snake.setheading(90)


def head_move_down():
    for i, snake in enumerate(all_snakes):
        if i == 0 and snake.heading() != 90:
            snake.setheading(270)


def head_move_right():
    for i, snake in enumerate(all_snakes):
        if i == 0 and snake.heading() != 180:
            snake.setheading(0)


def head_move_left():
    for i, snake in enumerate(all_snakes):
        if i == 0 and snake.heading() != 0:
            snake.setheading(180)


def trace_move():
    global snake_positions
    for i, snake in enumerate(all_snakes):
        if i < len(snake_positions):
            if i == 0:
                snake.forward(20)
            else:
                snake.goto(snake_positions[i - 1])

    snake_positions = [snake.pos() for snake in all_snakes]


def move():
    trace_move()
    screen.update()
    screen.listen()


def start_game():
    start_snake()
    random_food_show()
    screen.listen()
    screen.onkeypress(key="w", fun=head_move_up)
    screen.onkeypress(key="s", fun=head_move_down)
    screen.onkeypress(key="d", fun=head_move_right)
    screen.onkeypress(key="a", fun=head_move_left)


start_game()

while game_is_on:
    screen.update()  # Updates the screen
    time.sleep(0.1)  # Slows down the game

    if (
        all_snakes[0].pos()[0] > 270
        or all_snakes[0].pos()[1] > 270
        or all_snakes[0].pos()[0] < -270
        or all_snakes[0].pos()[1] < -270
    ):
        game_is_on = False
        print("Game Over")
    if (
        all_snakes[0].distance(food_position[0]) < 20
    ):  # 뱀의 머리와 음식의 거리를 확인하여 충돌 여부를 검사합니다.
        food_eaten = True
        grow_snake()  # 뱀의 꼬리 추가
        food_position = random_food_show()  # 새로운 음식 생성
        score += 1
        print(score)
        food_eaten = False

    move()

screen.exitonclick()
