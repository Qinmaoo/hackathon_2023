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
    def __init__(
        self,
        hp,
        atk,
        spd,
        x=random.normalvariate(800 / 2, 800 / 4),
        y=random.normalvariate(700 / 2, 700 / 4),
        trap=False,
    ):
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.trap = trap
        self.x = x
        self.y = y

    def sprite(self):
        return pg.transform.rotozoom((pg.image.load("textures/tom.png").convert_alpha()), 0, 0.2)

    def draw_mob(self, screen):
        if self.trap:
            screen.blit(self.sprite(), (self.x,self.y))

    def lose_health(self, hit):
        if not self.trap:
            self.hp -= hit

#Enemy types
std1 = Enemy(40,15,2)
std2 = Enemy(60,20,2.5)
std3 = Enemy(80,25,3)

off1 = Enemy(20,30,3)
off2 = Enemy(30,35,3.5)
off3 = Enemy(40,40,4)

def1 = Enemy(60,10,1.5)
def2 = Enemy(100,10,2)
def3 = Enemy(140,10,2.5)

boss = Enemy(200,30,2)

trap1 = Enemy(1,20,30, trap = True)
trap2 = Enemy(1,30,40, trap = True)
trap3 = Enemy(1,40,50, trap = True)


def gen_enemy():
    nb = random.randint(NB_MOB_MIN, NB_MOB_MAX)
    list_res = []
    for i in range(nb):
        list_res.append(std1)
    return list_res