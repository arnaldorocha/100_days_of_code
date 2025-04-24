from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

difficulty = screen.textinput("Escolha a dificuldade", "Digite: facil, medio ou dificil").lower()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
cars = CarManager(difficulty)


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_car()
    cars.move_cars()
    
    # 🚗 Detecção de colisão
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # 🏁 Verificação se chegou no topo
    if player.at_finish_line():
        player.reset_position()
        cars.level_up()
        scoreboard.increase_score()

screen.exitonclick()
