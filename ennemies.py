import random
import pygame as pg
from math import sqrt


def generate_random_color():
    return random.randrange(255), random.randrange(255), random.randrange(255)


def dist(point1, point2):
    x, y = point1
    a, b = point2
    return sqrt((x - a) ** 2 + (y - b) ** 2)


class Ennemy:
    def __init__(
        self,
        hp,
        atk,
        x=random.randint(0, 800),
        y=random.randint(0, 700),
        trap=False,
    ):
        self.hp = hp
        self.atk = atk
        self.trap = trap
        self.x = x
        self.y = y

    def draw_mob(self, screen):
        if self.trap:
            color = (128, 128, 128)
        else:
            color = (255, 0, 0)
        pg.draw.circle(screen, color, (self.x, self.y), 10)

    def lose_health(self, hit):
        if not self.trap:
            self.life -= hit
