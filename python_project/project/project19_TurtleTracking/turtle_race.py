from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="어떤 거북이가 이길까요?",
    prompt="승리가 예상되는 거북이의 색상 이름(red, orange, yellow, green, blue, purple)을 입력하세요: ",
)
all_turtles = []
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + colors.index(color) * 40)

    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"축하합니다. 맞췄습니다! {turtle.pencolor()} 거북이가 승리했습니다!")
            else:
                print(f"아쉽습니다. 틀렸습니다! {turtle.pencolor()} 거북이가 승리했습니다!")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
