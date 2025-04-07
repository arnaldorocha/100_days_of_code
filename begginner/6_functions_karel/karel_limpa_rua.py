import turtle
import time

# Configuração inicial
rua = [0, 1, 1, 0, 1, 0, 0, 1]
tamanho_casa = 50
posicao = 0

# Criação da janela
janela = turtle.Screen()
janela.title("RoboKarel Limpa-Rua")
janela.bgcolor("white")

# Tartarugas (objetos)
desenhista = turtle.Turtle()
robo = turtle.Turtle()

# Configuração do desenhista
desenhista.penup()
desenhista.speed(0)
desenhista.hideturtle()

# Configuração do robô
robo.shape("circle")
robo.color("blue")
robo.penup()
robo.speed(1)

# Função para desenhar a rua
def desenhar_rua():
    desenhista.clear()
    for i in range(len(rua)):
        x = i * tamanho_casa - (len(rua) * tamanho_casa) // 2
        y = 0
        desenhista.goto(x, y)
        desenhista.pendown()
        if rua[i] == 1:
            desenhista.fillcolor("red")  # com lixo
        else:
            desenhista.fillcolor("green")  # limpo
        desenhista.begin_fill()
        for _ in range(4):
            desenhista.forward(tamanho_casa)
            desenhista.right(90)
        desenhista.end_fill()
        desenhista.penup()

# Função para mover o robô para uma posição
def mover_robo(pos):
    x = pos * tamanho_casa - (len(rua) * tamanho_casa) // 2 + tamanho_casa / 2
    robo.goto(x, -tamanho_casa / 2)

# Função para limpar a casa
def limpar():
    rua[posicao] = 0

# Execução
desenhar_rua()
mover_robo(posicao)

while posicao < len(rua):
    time.sleep(0.5)
    if rua[posicao] == 1:
        limpar()
        desenhar_rua()
    mover_robo(posicao)
    posicao += 1

# Final
robo.hideturtle()
print("Limpeza concluída!")
janela.mainloop()
