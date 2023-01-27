import random
import pygame as pg


def generate_random_color():
    return random.randrange(255), random.randrange(255), random.randrange(255)


class Ennemy:
    def __init__(self, life, force, trap=False):
        self.life = life
        self.force = force
        self.trap = trap

    def draw_mob(self, screen, width, height):
        if self.trap:
            color = (128, 128, 128)
        else:
            color = (255, 0, 0)
        x, y = random.randint(0, width), random.randint(0, height)
        pg.draw.circle(screen, color, (x, y), 10)

    def lose_life(self, hit):
        if not self.trap:
            self.life -= hit
