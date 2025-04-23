from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Flags de movimento
r_move_up = False
r_move_down = False
l_move_up = False
l_move_down = False

# Funções para pressionar e soltar teclas
def r_up_press():    global r_move_up; r_move_up = True
def r_up_release():  global r_move_up; r_move_up = False
def r_down_press():  global r_move_down; r_move_down = True
def r_down_release():global r_move_down; r_move_down = False

def l_up_press():    global l_move_up; l_move_up = True
def l_up_release():  global l_move_up; l_move_up = False
def l_down_press():  global l_move_down; l_move_down = True
def l_down_release():global l_move_down; l_move_down = False

# Eventos do teclado
screen.listen()
screen.onkeypress(r_up_press, "Up")
screen.onkeyrelease(r_up_release, "Up")
screen.onkeypress(r_down_press, "Down")
screen.onkeyrelease(r_down_release, "Down")

screen.onkeypress(l_up_press, "w")
screen.onkeyrelease(l_up_release, "w")
screen.onkeypress(l_down_press, "s")
screen.onkeyrelease(l_down_release, "s")

# Loop do jogo com atualização de movimento contínua
def game_loop():
    # Atualiza movimento das raquetes
    if r_move_up:
        r_paddle.go_up()
    if r_move_down:
        r_paddle.go_down()
    if l_move_up:
        l_paddle.go_up()
    if l_move_down:
        l_paddle.go_down()

    ball.move()
    time.sleep(ball.move_speed)

    # Colisão com parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Colisão com raquete
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Pontuação
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    screen.update()
    screen.ontimer(game_loop, 20)  # chama a si mesma a cada 20ms

# Inicia o loop
game_loop()
screen.mainloop()
