import turtle
import time
import random

# Configuração da janela
win = turtle.Screen()
win.title("Breakout - Clone com Python Turtle")
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

ball.dx = 0.7
ball.dy = 0.7

# Aceleração progressiva da bola
ball.dx *= 1.001
ball.dy *= 1.001


# Lista de blocos
blocks = []

colors = ["red", "orange", "yellow", "green", "blue"]

# Criar os blocos
for y in range(250, 150, -20):
    for x in range(-350, 350, 70):
        block = turtle.Turtle()
        block.shape("square")
        block.color(random.choice(colors))
        block.shapesize(stretch_wid=1, stretch_len=3)
        block.penup()
        block.goto(x, y)
        blocks.append(block)

# Funções de movimento
def paddle_left():
    x = paddle.xcor()
    if x > -340:
        paddle.setx(x - 30)

def paddle_right():
    x = paddle.xcor()
    if x < 340:
        paddle.setx(x + 30)

# Controles do teclado
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# Loop principal do jogo
while True:
    win.update()
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
            block.goto(1000, 1000)  # Move o bloco para longe (desaparece)
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
