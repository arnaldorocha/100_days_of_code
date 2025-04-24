from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Configuração da tela
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Controles
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Loop principal do jogo
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detectar colisão com a comida
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # Aumentar a pontuação
        scoreboard.increase_score()

    if  snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # Detectar colisão com a parede


    # Detectar colisão com a cauda
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

