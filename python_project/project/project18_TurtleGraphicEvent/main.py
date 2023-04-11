import random
from turtle import Turtle, Screen

""" tim = Turtle()
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

screen.exitonclick() """


# 터틀 스크린 생성
screen = Turtle.Screen()

# 터틀 객체 생성
t = Turtle.Turtle()

# 삼각형 그리기 함수


def draw_triangle(x, y):
    # 터틀 위치 이동
    t.penup()
    t.goto(x, y)
    t.pendown()

    # 삼각형 그리기
    for i in range(3):
        t.forward(50)
        t.left(120)


# 100개의 삼각형 그리기
# for i in range(100):
#     # 무작위 위치 생성
#     x = random.randint(-300, 300)
#     y = random.randint(-300, 300)

#     # 삼각형 그리기 함수 호출
#     draw_triangle(x, y)

# # 터틀 종료
# turtle.done()


# 100개의 원을 무작위로 그리는 코드
def draw_circle():
    # 무작위 위치 생성
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    # 터틀 위치 이동
    t.penup()
    t.goto(x, y)
    t.pendown()

    # 원 그리기
    t.circle(50)
