import random
import pygame as pg


def generate_random_color():
    return random.randrange(255), random.randrange(255), random.randrange(255)


class Ennemy:
    def __init__(self, life, force):
        self.life = life
        self.force = force

    def draw_mob(self, screen, width, height):
        color = generate_random_color()
        x, y = random.randint(0, width), random.randint(0, height)
        pg.draw.circle(screen, color, (x, y), 10)

    def lose_life(self, hit):
        self.life -= hit
