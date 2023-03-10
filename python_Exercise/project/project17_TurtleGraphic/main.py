from turtle import Turtle, Screen
import random
import colorgram


# 삼각형에서 12각형까지 그리는 함수
def draw_shape(angle, direction):
    if direction == "right" :
        while angle != 12:
            tt.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            for _ in range(angle):
                tt.forward(100)
                tt.right(round(360/angle,1))
            angle += 1
    else:
        while angle != 12:
            tt.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            for _ in range(angle):
                tt.forward(100)
                tt.left(round(360/angle,1))
            angle += 1
    return

# 랜덤 색깔 추출 함수
def random_color():
    red = random.randint(1, 255)
    green = random.randint(1, 255)
    blue = random.randint(1, 255)
    
    random_colors = (red, green, blue)
    return random_colors

# 랜덤 각도로 선 그리기 함수
def random_draw(angle):
    while True :
        tt.pencolor(random_color())
        num = random.randint(1, 3)
        if num == 1 :
            tt.right(num*angle)
            tt.forward(20)
        elif num == 2: 
            tt.left(num*angle)
            tt.forward(20)
        else:
            tt.forward(20)
    return

# 일정한 각도로 원 그리기
def draw_circle(num, radius):
    for _ in range(num):
        tt.pencolor(random_color())
        tt.circle(radius)
        tt.left(int(360/num))
    
# 색상 추출 함수
def extract_color():
    rgb_colors=[]
    # colors = colorgram.extract('python_Exercise/project/project17_TurtleGraphic/image.jpg', 30)
    colors = colorgram.extract('python_Exercise/project/project17_TurtleGraphic/autumn.jpg', 30)
    
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        
        rgb_color = (r, g, b)
        rgb_colors.append(rgb_color)
        
    return rgb_colors

# 추출된 색상을 이용하여 점 그림 그리기
def print_dot():
    rgb_colors = extract_color()
    
    for i in range(20):        
        tt.penup()
        tt.goto(-300, -300+(i*30))
        for _ in range(15):
            
            tt.pendown()
            tt.dot(20, random.choice(rgb_colors))
            tt.penup()
            tt.forward(40)
    
    tt.penup()    
    return
    
tt = Turtle()
tt.shape("circle")
tt.speed("fastest")
tt.hideturtle()
screen = Screen()
screen.colormode(255)

# 점선 사각형 그리기
# for _ in range(4):
#     for _ in range(10):
#         tt.forward(10)
#         tt.penup()
#         tt.forward(10)
#         tt.pendown()
#     tt.left(90)

# 정삼각형, 정사각형, 정오각형, 정육각형 등 도형 그리기

# draw_shape(3,"right")
# draw_shape(3,"left")

# 랜덤 방향으로 회전하며 그려 나가기
# tt.pensize(5)
# random_draw(40)

# 여러개 원 그리기
# draw_circle(50, 100)

# 이미지로 색상을 추출하여 점 그리기
print_dot()
# 창의 클릭하면 종료
screen.exitonclick()

