import pygame as pg
import random

S_WIDTH, S_HIGHT = 800, 700
screen = pg.display.set_mode((S_WIDTH, S_HIGHT))


opened_texture = pg.transform.rotozoom(
    (pg.image.load("textures/opened_chest.png").convert_alpha()), 0, 0.05
)
closed_texture = pg.transform.rotozoom(
    (pg.image.load("textures/closed_chest.png").convert_alpha()), 0, 0.05
)


Stats = {"HP_MAX": 100, "ATK": 10, "SPD": 25, "DEF": 0, "RANGE": 50, "FIRE_RATE": 100}
HP = 100


class Item:
    def __init__(self, name, effect):
        self.name = name
        self.texture = pg.image.load(
            f"textures/{self.name.replace(' ', '_') }.webp"
        ).convert_alpha()
        self.effect = effect

    def item_get(self):
        for st in Stats.keys():
            Stats[st] += self.effect[st]


brimstone = Item(
    "Brimstone",
    {"HP_MAX": 0, "ATK": 5, "SPD": 0, "DEF": 0, "RANGE": 20, "FIRE_RATE": 10},
)

magicmush = Item(
    "Magic Mushroom",
    {"HP_MAX": 10, "ATK": 3, "SPD": 5, "DEF": 3, "RANGE": 10, "FIRE_RATE": -10},
)

ipecac = Item(
    "Ipecac",
    {"HP_MAX": 0, "ATK": 10, "SPD": 0, "DEF": -3, "RANGE": 20, "FIRE_RATE": 15},
)

plan_c = Item(
    "Plan C", {"HP_MAX": 0, "ATK": 5, "SPD": 0, "DEF": 0, "RANGE": 20, "FIRE_RATE": 10}
)

c_section = Item(
    "C Section",
    {"HP_MAX": 0, "ATK": 5, "SPD": 0, "DEF": 0, "RANGE": 5, "FIRE_RATE": 10},
)

bobby = Item(
    "Brother Bobby",
    {"HP_MAX": 0, "ATK": 1, "SPD": 0, "DEF": 2, "RANGE": 10, "FIRE_RATE": -10},
)

maggy = Item(
    "Sister Maggy",
    {"HP_MAX": 0, "ATK": 1, "SPD": 0, "DEF": 2, "RANGE": 10, "FIRE_RATE": -10},
)

lilbrim = Item(
    "Lil Brimstone",
    {"HP_MAX": 0, "ATK": 2, "SPD": 0, "DEF": 0, "RANGE": 10, "FIRE_RATE": 0},
)

item_list = [brimstone, magicmush, ipecac, plan_c, c_section, bobby, maggy, lilbrim]


class Chest:
    def __init__(
        self, item, status="closed", texture=closed_texture
    ):
        self.content = item
        self.status = status  # Ouvert/fermé
        self.texture = texture

    def open(self):
        self.status = "opened"
        item_texture = self.content.texture
        coffre_texture = opened_texture
        merged = coffre_texture.copy()
        merged.blit(pg.transform.rotozoom(item_texture, 0, 1), (15, 3))
        self.texture = merged


""" if event.key == pg.K_o:
        coffre1.texture.fill((255,255,255))
        coffre1.open()
        print(coffre1.content)
"""
