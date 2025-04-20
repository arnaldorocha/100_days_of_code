from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Run")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-250, y_positions[turtle_index])
    turtles.append(new_turtle)

race_on = True

random_distances = list(range(0, 11))

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! Your bet was on the {user_bet} turtle, and it is the winner!")
            else:
                print(f"You've lost! Your bet was on the {user_bet} turtle, but the {winning_color} turtle is the winner!")
            race_on = False
            break
        random_distance = random.choice(random_distances)
        turtle.forward(random_distance)

screen.exitonclick()