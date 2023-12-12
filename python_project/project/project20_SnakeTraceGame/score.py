from turtle import Turtle
SCORE = 0

class Score():
    
    def __init__(self) -> None:
        self.score = SCORE
        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 270)
        self.update_scoreboard()
        
    def __add__(self, other):
        if isinstance(other, int):
            return self.score + other
        else:
            return NotImplemented
        
    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()