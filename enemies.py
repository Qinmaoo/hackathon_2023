import random
import pygame as pg
from math import sqrt

NB_MOB_MIN = 1
NB_MOB_MAX = 7


def generate_random_color():
    return random.randrange(255), random.randrange(255), random.randrange(255)


def dist(point1, point2):
    x, y = point1
    a, b = point2
    return sqrt((x - a) ** 2 + (y - b) ** 2)


def gen_enemy():
    nb = random.randint(NB_MOB_MIN, NB_MOB_MAX)
    list_res = []
    for i in range(nb):
        list_res.append(Enemy(30, 2, 10))
    return list_res


class Enemy:
    def __init__(self, hp, atk, spd, x=None, y=None, trap=False):
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.trap = trap
        if x is None:
            self.x = random.normalvariate(800 / 2, 800 / 4)
        else:
            self.x = x
        if y is None:
            self.y = random.normalvariate(700 / 2, 700 / 4)
        else:
            self.y = y

    def draw_mob(self, screen):
        if self.trap:
            color = (128, 128, 128)
        else:
            color = (255, 0, 0)
        pg.draw.circle(screen, color, (self.x, self.y), 20)

    def lose_health(self, hit):
        if not self.trap:
            self.hp -= hit
