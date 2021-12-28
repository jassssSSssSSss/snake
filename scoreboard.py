
from turtle import Turtle
from food import Food
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
#for hard text constant things put top bc easy to find if you wanna make changes 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg = f"Score : {self.score}", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER.lol.", align = ALIGNMENT, font = FONT)


        
        
    
    



