import pygame as pg
from items_stats import *
from rooms import Room
from ennemies import *

S_WIDTH, S_HIGHT = 800, 700
# R_WIDTH, R_HIGHT = 300, 500
R_COLOR = [122, 52, 24]
D_w, D_h = 50, 10
D_COLOR = [196, 102, 65]


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


coffre1 = Chest()


def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HIGHT))

    player = Player(100, 100)

    run = True
    while run:
        clock.tick(50)
        # code à mettre ici pour ce qu'il se passe entre 2 images

        screen.fill((133, 80, 64))
        screen.blit(coffre1.texture, (200, 200))
        pg.draw.circle(screen, (200, 0, 200), (player.x, player.y), 10)
        mob1 = Ennemy(50, 2)
        room1 = Room([mob1], 1)
        room1.draw_room(screen)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN and (
                event.key == pg.K_q or event.key == pg.K_ESCAPE
            ):
                run = False

        keys = pg.key.get_pressed()

        if keys[pg.K_DOWN]:
            player.y += Stats["SPD"] / 10

        if keys[pg.K_UP]:
            player.y -= Stats["SPD"] / 10

        if keys[pg.K_LEFT]:
            player.x -= Stats["SPD"] / 10

        if keys[pg.K_RIGHT]:
            player.x += Stats["SPD"] / 10

        if keys[pg.K_o]:
            coffre1.open()

    pg.quit()


if __name__ == "__main__":
    main()
