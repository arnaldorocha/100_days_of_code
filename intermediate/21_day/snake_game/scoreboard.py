from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', align= ALIGMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align= ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align= ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGMENT, font=FONT)