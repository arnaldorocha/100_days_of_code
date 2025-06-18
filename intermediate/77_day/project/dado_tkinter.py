import tkinter as tk
import pygame
import random
import threading
import time
import sys

# Inicializa Pygame
pygame.init()

# Configura a janela Pygame (onde o dado vai aparecer)
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dado Virtual")

# Carregar imagens do dado
dice_images = []
for i in range(1, 7):
    image = pygame.image.load(f'dice{i}.png')
    image = pygame.transform.scale(image, (150, 150))  # redimensionar
    dice_images.append(image)

# Função para desenhar dado na tela Pygame
def draw_dice(face):
    screen.fill((255, 255, 255))  # fundo branco
    screen.blit(dice_images[face - 1], ((WIDTH - 150)//2, (HEIGHT - 150)//2))
    pygame.display.flip()

# Função para animar dado girando
def roll_animation():
    for _ in range(15):
        face = random.randint(1, 6)
        draw_dice(face)
        time.sleep(0.1)
    return face

# Thread que roda a animação (para não travar o Tkinter)
def roll_dice_thread():
    btn_roll.config(state=tk.DISABLED)
    face = roll_animation()
    draw_dice(face)
    btn_roll.config(state=tk.NORMAL)

# Função chamada ao clicar no botão Tkinter
def on_roll_click():
    threading.Thread(target=roll_dice_thread, daemon=True).start()

# Criar janela Tkinter
root = tk.Tk()
root.title("Controle do Dado Virtual")

btn_roll = tk.Button(root, text="Lançar Dado", command=on_roll_click)
btn_roll.pack(pady=20)

# Inicializa Pygame e mostra dado 1 ao abrir
draw_dice(1)

# Função para manter o Pygame rodando e receber eventos
def pygame_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                root.quit()
                sys.exit()
        time.sleep(0.01)

# Rodar o loop do pygame em uma thread para não travar o Tkinter
threading.Thread(target=pygame_loop, daemon=True).start()

root.mainloop()
