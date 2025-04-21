from turtle import Screen, Turtle
import time
# This is a simple implementation of a snake game using the turtle graphics library in Python.


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []  # List to hold the segments of the snake

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    # Add the new segment to the list of segments
    segments.append(new_segment)

screen.listen()  # Listen for keyboard input

game_is_on = True   # Variable to control the game loop     
while game_is_on:

    screen.update()
    time.sleep(0.1)  # Pause for a short time to control the speed of the snake
    for seg_num in range(len(segments) - 1, 0, -1):
        new_X = segments[seg_num - 1].xcor()
        new_Y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_X, new_Y)
    segments[0].forward(20)  # Move the first segment forward
    # Check for collision with the walls
    if segments[0].xcor() > 290 or segments[0].xcor() < -290 or segments[0].ycor() > 290 or segments[0].ycor() < -290:
        game_is_on = False  # End the game if the snake collides with the walls
    # Check for collision with the snake itself

    
screen.exitonclick()  # Wait for a click to exit