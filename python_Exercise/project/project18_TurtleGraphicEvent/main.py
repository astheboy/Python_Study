from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def rotation_right():
    tim.right(10)
    
def rotation_left():
    tim.left(10)
    
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="a", fun=rotation_right)
screen.onkey(key="d", fun=rotation_left)

screen.exitonclick()