from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turns off the screen updates for better performance

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
# Create the paddles and ball

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Sleep for a short duration to control the speed of the game
    screen.update()  # Update the screen to reflect 
    ball.move()  # Move the ball
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce off the wall
        ball.bounce_y()
    # Detect collision with paddles
    if  ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
    # Check if the ball is within the paddle's y range and its x position is within the paddle's x range    
        ball.bounce_x()
        # needs to bounce off the paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        # needs to bounce off the wall 


screen.exitonclick()
# The code sets up a screen for a Pong game using the turtle graphics library. It creates a black background,
#  sets the screen size to 800x600 pixels, and gives the window the title "Pong Game". 
# Finally, it waits for a click on the screen to exit the program.