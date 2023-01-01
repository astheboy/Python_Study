from turtle import Turtle, Screen


timmy = Turtle()  #클래스의 첫글자는 대문자로 작성하고 ()를 통해 새로운 객체를 형성
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.pendown()
for i in range(20):
    for i in range(4):
        timmy.forward(100)
        timmy.right(90)
    timmy.left(90)
    for i in range(4):
        timmy.forward(100)
        timmy.left(90)
    timmy.right(i*3)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



