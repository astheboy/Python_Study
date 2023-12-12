from turtle import Turtle
snake_num = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self) -> None:
        self.all_snakes = []
        self.snake_positions = []
        self.start_snake()
      
            
    def start_snake(self):
        for i in range(snake_num):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.pensize(20)
            snake.goto(x=0 + (i * 20), y=0)
            self.all_snakes.append(snake)
            self.snake_positions.append(snake.pos())
    
    def grow_snake(self):
        snake_tail = Turtle(shape="square")
        snake_tail.color("white")
        snake_tail.penup()
        snake_tail.pensize(20)
        snake_tail.goto(self.all_snakes[len(self.all_snakes) - 1].pos())
        self.all_snakes.append(snake_tail)


    def up(self):
        if self.all_snakes[0].heading() != DOWN:
            self.all_snakes[0].setheading(UP)


    def down(self):
        if self.all_snakes[0].heading() != UP:
            self.all_snakes[0].setheading(DOWN)

    def right(self):
        if self.all_snakes[0].heading() != LEFT:
            self.all_snakes[0].setheading(RIGHT)


    def left(self):
        if self.all_snakes[0].heading() != RIGHT:
            self.all_snakes[0].setheading(LEFT)



    def trace_move(self):
        # global snake_positions
        for i, snake in enumerate(self.all_snakes):
            if i < len(self.snake_positions):
                if i == 0:
                    snake.forward(MOVE_DISTANCE)
                else:
                    snake.goto(self.snake_positions[i - 1])

        self.snake_positions = [snake.pos() for snake in self.all_snakes]