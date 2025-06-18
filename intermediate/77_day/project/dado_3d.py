from vpython import *
import random

# Cria a cena 3D
scene.title = "Jogar Dado 3D"
scene.width = 600
scene.height = 600

# Criar um cubo que representará o dado
dice = box(size=vector(2,2,2), color=color.white)

# Criar os pontos do dado em cada face (exemplo simples)
dots = []

def create_dots():
    # Limpa pontos anteriores
    global dots
    for d in dots:
        d.visible = False
    dots = []
    
    # Posiciona pontos conforme o número do dado
    # Exemplo: pontos no centro e cantos
    positions = {
        1: [(0,0,1.01)],
        2: [(-0.5,-0.5,1.01), (0.5,0.5,1.01)],
        3: [(-0.5,-0.5,1.01), (0,0,1.01), (0.5,0.5,1.01)],
        4: [(-0.5,-0.5,1.01), (-0.5,0.5,1.01), (0.5,-0.5,1.01), (0.5,0.5,1.01)],
        5: [(-0.5,-0.5,1.01), (-0.5,0.5,1.01), (0,0,1.01), (0.5,-0.5,1.01), (0.5,0.5,1.01)],
        6: [(-0.5,-0.7,1.01), (-0.5,0,1.01), (-0.5,0.7,1.01), (0.5,-0.7,1.01), (0.5,0,1.01), (0.5,0.7,1.01)]
    }
    for pos in positions[current_number]:
        dot = sphere(pos=vector(pos[0], pos[1], pos[2]), radius=0.15, color=color.black)
        dots.append(dot)

def roll_dice():
    global current_number
    for _ in range(20):
        # gira o dado aleatoriamente
        dice.rotate(angle=0.3, axis=vector(1,0,0))
        dice.rotate(angle=0.3, axis=vector(0,1,0))
        rate(30)
    current_number = random.randint(1,6)
    create_dots()

current_number = 1
create_dots()

# Botão para rolar dado
def button_action():
    roll_dice()

button(text="Lançar Dado", bind=lambda _: button_action())


while True:
    rate(30)
