import turtle
import time
import random

try:
    import winsound
    sound_enabled = True
except ImportError:
    sound_enabled = False

# Função para tocar som (somente Windows)
def play_sound():
    if sound_enabled:
        winsound.Beep(1000, 100)  # Frequência: 1000Hz, Duração: 100ms

# Configuração da janela
win = turtle.Screen()
win.title("Breakout com Pontos, Vidas e Sons - Python Turtle")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Pontuação e vidas
score = 0
lives = 3

# Placar
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score} | Vidas: {lives}", align="center", font=("Arial", 16, "bold"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score} | Vidas: {lives}", align="center", font=("Arial", 16, "bold"))

# Raquete
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Bola
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -100)
ball.dx = 0.5
ball.dy = 0.5

# Blocos
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

# Movimento fluido da raquete
move_left = False
move_right = False

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

# Controles
win.listen()
win.onkeypress(start_move_left, "Left")
win.onkeyrelease(stop_move_left, "Left")
win.onkeypress(start_move_right, "Right")
win.onkeyrelease(stop_move_right, "Right")

# Função de reset da bola após perder vida
def reset_ball():
    global ball
    ball.goto(0, -100)
    ball.dx = random.choice([-0.5, 0.5])
    ball.dy = 0.5
    time.sleep(1)

# Loop principal
while True:
    win.update()

    # Movimento da raquete
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
        play_sound()

    # Colisão com o topo
    if ball.ycor() > 290:
        ball.dy *= -1
        play_sound()

    # Colisão com a raquete
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1
        play_sound()

    # Colisão com blocos
    for block in blocks:
        if ball.distance(block) < 35:
            ball.dy *= -1
            play_sound()
            block.goto(1000, 1000)
            blocks.remove(block)
            score += 10
            update_score()
            break

    # Bola caiu (perde vida)
    if ball.ycor() < -290:
        lives -= 1
        update_score()
        if lives == 0:
            score_display.goto(0, 0)
            score_display.write(f"GAME OVER!\nPontuação final: {score}", align="center", font=("Arial", 18, "bold"))
            time.sleep(3)
            win.bye()
        else:
            reset_ball()

    # Vitória
    if len(blocks) == 0:
        score_display.goto(0, 0)
        score_display.write(f"PARABÉNS!\nVocê venceu!\nPontuação final: {score}", align="center", font=("Arial", 18, "bold"))
        time.sleep(3)
        win.bye()
