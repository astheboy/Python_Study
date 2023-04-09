# 무작위로 원과 삼각형, 사각형을 그리는 프로그램
import turtle
import random


def drawRandomCircle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("red")
    t.speed(0)
    for i in range(100):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        r = random.randint(1, 100)
        t.up()
        t.goto(x, y)
        t.down()
        t.circle(r)


def drawRandomTriangle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    t.speed(0)
    for i in range(100):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        r = random.randint(1, 100)
        t.up()
        t.goto(x, y)
        t.down()
        t.begin_fill()
        t.forward(r)
        t.left(120)
        t.forward(r)
        t.left(120)
        t.forward(r)
        t.left(120)
        t.end_fill()


def drawRandomSquare():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    t.speed(0)
    for i in range(100):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        r = random.randint(1, 100)
        t.up()
        t.goto(x, y)
        t.down()
        t.begin_fill()
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.end_fill()


def drawRandomShape():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("black")
    t.speed(0)
    for i in range(100):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        r = random.randint(1, 100)
        t.up()
        t.goto(x, y)
        t.down()
        t.begin_fill()
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.forward(r)
        t.left(90)
        t.end_fill()


# drawRandomShape()
drawRandomCircle()
