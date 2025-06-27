import pygame
import pickle
import neat
import os
from main import Dino, Obstacle, draw_window  # reaproveita classes

def jogar_campeao(config_path, genome_path):
    with open(genome_path, "rb") as f:
        genome = pickle.load(f)

    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    net = neat.nn.FeedForwardNetwork.create(genome, config)
    dino = Dino()
    obstacles = [Obstacle(800)]

    win = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    score = 0
    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if len(obstacles) == 0 or obstacles[-1].x < 500:
            obstacles.append(Obstacle(850))

        for obstacle in obstacles:
            obstacle.move()
            if obstacle.collide(dino):
                run = False

        if obstacles[0].x + 20 < 0:
            obstacles.pop(0)
            score += 1

        dino.move()
        output = net.activate((obstacles[0].x - dino.x, obstacles[0].vel))
        if output[0] > 0.5:
            dino.jump()

        draw_window(win, [dino], obstacles, score, "Campeão")

    pygame.quit()

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    jogar_campeao(os.path.join(path, "config-feedforward.txt"), "melhor_dino.pkl")
