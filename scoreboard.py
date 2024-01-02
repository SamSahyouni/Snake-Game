from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')
LOCATION = (-20,220)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(LOCATION)
        self.color("white")
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LOCATION)
        self.write(f"score: {self.score} high score: {self.high_score}",True, align= ALIGNMENT,font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    def score_increase(self):
        self.clear()
        self.goto(LOCATION)
        self.score += 1
        self.update_scoreboard()

