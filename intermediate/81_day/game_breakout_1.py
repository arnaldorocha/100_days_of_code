import turtle
import time
import random

# Configuração da janela
win = turtle.Screen()
win.title("Breakout - Clone com Controle Fluido")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Criação da raquete
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Criação da bola
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -100)

ball.dx = 0.5
ball.dy = 0.5

# Lista de blocos
blocks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for y in range(250, 150, -20):
    for x in range(-350, 350, 70):
        block = turtle.Turtle()
        block.shape("square")
        block.color(random.choice(colors))
        block.shapesize(stretch_wid=1, stretch_len=3)
        block.penup()
        block.goto(x, y)
        blocks.append(block)

# Variáveis de controle das teclas
move_left = False
move_right = False

# Funções para atualizar os flags
def start_move_left():
    global move_left
    move_left = True

def stop_move_left():
    global move_left
    move_left = False

def start_move_right():
    global move_right
    move_right = True

def stop_move_right():
    global move_right
    move_right = False

# Controles de teclado
win.listen()
win.onkeypress(start_move_left, "Left")
win.onkeyrelease(stop_move_left, "Left")
win.onkeypress(start_move_right, "Right")
win.onkeyrelease(stop_move_right, "Right")

# Loop principal do jogo
while True:
    win.update()

    # Movimento fluido da raquete
    if move_left and paddle.xcor() > -340:
        paddle.setx(paddle.xcor() - 10)
    if move_right and paddle.xcor() < 340:
        paddle.setx(paddle.xcor() + 10)

    # Movimento da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colisão com as laterais
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    # Colisão com o topo
    if ball.ycor() > 290:
        ball.dy *= -1

    # Colisão com a raquete
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1

    # Colisão com os blocos
    for block in blocks:
        if ball.distance(block) < 35:
            ball.dy *= -1
            block.goto(1000, 1000)
            blocks.remove(block)
            break

    # Condição de derrota
    if ball.ycor() < -290:
        print("Game Over!")
        time.sleep(2)
        win.bye()

    # Condição de vitória
    if len(blocks) == 0:
        print("Você venceu! Todos os blocos destruídos!")
        time.sleep(2)
        win.bye()
