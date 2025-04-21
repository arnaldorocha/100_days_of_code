from turtle import Screen, Turtle
from snake import Snake
import time
# This is a simple implementation of a snake game using the turtle graphics library in Python.


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# The game loop

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Control the speed of the game

    snake.move() # Move the snake


screen.exitonclick()  # Wait for a click to exit