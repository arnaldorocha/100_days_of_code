import pygame
import neat
import os
import random

pygame.font.init()

WIN_WIDTH = 800
WIN_HEIGHT = 400

GEN = 0
STAT_FONT = pygame.font.SysFont("comicsans", 30)

# Dino básico
class Dino:
    IMG = pygame.Surface((40, 40))
    IMG.fill((0, 0, 0))

    def __init__(self):
        self.x = 50
        self.y = 300
        self.vel_y = 0
        self.gravity = 1.5
        self.jump_strength = -15
        self.is_jumping = False
        self.alive = True
        self.score = 0

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_strength
            self.is_jumping = True

    def move(self):
        self.vel_y += self.gravity
        self.y += self.vel_y
        if self.y >= 300:
            self.y = 300
            self.is_jumping = False

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.IMG)

class Obstacle:
    IMG = pygame.Surface((20, 50))
    IMG.fill((255, 0, 0))

    def __init__(self, x):
        self.x = x
        self.y = 300
        self.vel = 10

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

    def collide(self, dino):
        dino_mask = dino.get_mask()
        obstacle_mask = pygame.mask.from_surface(self.IMG)
        offset = (int(self.x - dino.x), int(self.y - round(dino.y)))
        collision_point = dino_mask.overlap(obstacle_mask, offset)
        return collision_point is not None

def draw_window(win, dinos, obstacles, score, gen):
    win.fill((255, 255, 255))
    for obstacle in obstacles:
        obstacle.draw(win)
    for dino in dinos:
        dino.draw(win)

    text = STAT_FONT.render(f"Score: {score}", 1, (0, 0, 0))
    win.blit(text, (10, 10))
    text_gen = STAT_FONT.render(f"Geração: {gen}", 1, (0, 0, 0))
    win.blit(text_gen, (10, 40))
    pygame.display.update()

def main(genomes, config):
    global GEN
    GEN += 1

    nets = []
    ge = []
    dinos = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        dinos.append(Dino())
        ge.append(genome)

    obstacles = [Obstacle(900)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run and len(dinos) > 0:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        # adicionar obstáculo
        if len(obstacles) == 0 or obstacles[-1].x < 500:
            obstacles.append(Obstacle(random.randint(850, 1000)))

        # mover obstáculos
        rem = []
        for obstacle in obstacles:
            obstacle.move()
            for x, dino in enumerate(dinos):
                if obstacle.collide(dino):
                    ge[x].fitness -= 1
                    dinos.pop(x)
                    nets.pop(x)
                    ge.pop(x)
            if obstacle.x + 20 < 0:
                rem.append(obstacle)

        for r in rem:
            obstacles.remove(r)
            score += 1
            for g in ge:
                g.fitness += 5

        for x, dino in enumerate(dinos):
            dino.move()
            ge[x].fitness += 0.1
            # entrada da IA: distância até obstáculo e velocidade
            if len(obstacles) > 0:
                output = nets[x].activate((obstacles[0].x - dino.x, obstacles[0].vel))
                if output[0] > 0.5:
                    dino.jump()

        draw_window(win, dinos, obstacles, score, GEN)

def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    p.run(main, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
