from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game!")
screen.tracer(0)  # Turns off the screen updates

game_is_on = True

snake_num = 3
all_snakes = []
snake_positions = []

for i in range(snake_num):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.pensize(20)
    snake.goto(x=0 + (i * 20), y=0)
    all_snakes.append(snake)
    snake_positions.append(snake.pos())


def head_move_up():
    new_position = (all_snakes[0].pos()[0], all_snakes[0].pos()[1]+20)
    all_snakes[0].setpos(*new_position)
    snake_positions.insert(0, new_position)


def head_move_down():
    new_position = (all_snakes[0].pos()[0], all_snakes[0].pos()[1]-20)
    all_snakes[0].setpos(*new_position)
    snake_positions.insert(0, new_position)


def head_move_right():
    new_position = (all_snakes[0].pos()[0]+20, all_snakes[0].pos()[1])
    all_snakes[0].setpos(*new_position)
    snake_positions.insert(0, new_position)


def head_move_left():
    new_position = (all_snakes[0].pos()[0]-20, all_snakes[0].pos()[1])
    all_snakes[0].setpos(*new_position)
    snake_positions.insert(0, new_position)


def trace_move():
    for i, snake in enumerate(all_snakes):
        if i < len(snake_positions):
            snake.setpos(snake_positions[i])


def move():
    screen.onkeypress(key="w", fun=head_move_up)
    screen.onkeypress(key="s", fun=head_move_down)
    screen.onkeypress(key="d", fun=head_move_right)
    screen.onkeypress(key="a", fun=head_move_left)
    trace_move()


screen.listen()

while game_is_on:
    screen.update()  # Updates the screen
    time.sleep(0.1)  # Slows down the game
    move()

screen.exitonclick()
