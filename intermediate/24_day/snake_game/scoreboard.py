from turtle import Turtle
import os

ALIGMENT = 'center'
FONT = ('Courier', 14, 'normal')

# Caminho absoluto para o arquivo data.txt
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "data.txt")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open(DATA_FILE) as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
            with open(DATA_FILE, mode="w") as data:
                data.write("0")

        self.color("white")
        self.penup()
        self.goto(0, 270) 
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


# from turtle import Turtle

# ALIGMENT = 'center'
# FONT = ('Courier', 14, 'normal')

# class Scoreboard(Turtle):
    
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         try:
#             with open("data.txt") as data:
#                 self.high_score = int(data.read())
#         except FileNotFoundError:
#             self.high_score = 0
#             with open("data.txt", mode="w") as data:
#                 data.write("0")

#         self.color("white")
#         self.penup()
#         self.goto(0, 270) 
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.clear()
#         self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGMENT, font=FONT)
    
#     def reset(self):
#         if self.score > self.high_score:
#             self.high_score = self.score
#             with open("data.txt", mode="w") as data:
#                 data.write(f"{self.high_score}")
#         self.score = 0
#         self.update_scoreboard()

#     def increase_score(self):
#         self.score += 1
#         self.update_scoreboard()



# from turtle import Turtle
# ALIGMENT = 'center'
# FONT = ('Courier', 14, 'normal')


# class Scoreboard(Turtle):
    
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         with open("data.txt") as data:
#             self.high_score = int(data.read())
#         self.color("white")
#         self.penup()
#         self.goto(0, 270) 
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.clear()
#         self.write(f'Score: {self.score} High Score: {self.high_score}', align= ALIGMENT, font=FONT)
    
#     def reset(self):
#         if self.score > self.high_score:
#             self.high_score = self.score
#             with open("data.txt", mode="w") as data:
#                 data.write(f"{self.high_score}")
#         self.score = 0
#         self.update_scoreboard()

#     def increase_score(self):
#         self.score += 1
#         self.update_scoreboard()


    