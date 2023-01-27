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

#Enemy types
std1 = Enemy(40,15,2)
std2 = Enemy(60,20,3)
std3 = Enemy(80,25,4)

off1 = Enemy(20,30,4)
off2 = Enemy(30,35,5)
off3 = Enemy(40,40,6)

def1 = Enemy(60,10,1)
def2 = Enemy(100,10,1)
def3 = Enemy(140,10,2)

boss = Enemy(200,30,3)

trap1 = Enemy(1,20,30, trap = True)
trap2 = Enemy(1,30,40, trap = True)
trap3 = Enemy(1,40,50, trap = True)


def gen_enemy():
    nb = random.randint(NB_MOB_MIN, NB_MOB_MAX)
    list_res = []
    for i in range(nb):
        list_res.append(std1)
    return list_res