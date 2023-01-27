import pygame as pg
from items_stats import *
from rooms import Room, Player
import numpy as np
from ennemies import gen_enemy
import collections as col

S_WIDTH, S_HIGHT = 800, 700
# R_WIDTH, R_HIGHT = 300, 500
R_COLOR = [122, 52, 24]
D_w, D_h = 50, 10
D_COLOR = [196, 102, 65]
current_room = (0,0)

room_grid = np.array([Room(gen_enemy(), (i,j)) for i,j in col.product(range(4), range(4))]).resize((4,4))

coffre1 = Chest()

def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HIGHT))

    player = Player(100,100)

    run = True
    while run:
        clock.tick(50)
        # code à mettre ici pour ce qu'il se passe entre 2 images
        
        screen.fill((133, 80, 64))
        screen.blit(coffre1.texture,(200,200))
        Room.swith_rooms(player)
        pg.draw.circle(screen, (200,0,200), (player.x,player.y), 10)
        room_grid[*current_room].draw_room()
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN and (event.key == pg.K_q or event.key == pg.K_ESCAPE):
                run = False

        keys = pg.key.get_pressed()
        
        if keys[pg.K_DOWN]:
            player.y += Stats["SPD"]/10
        
        if keys[pg.K_UP]:
            player.y -= Stats["SPD"]/10

        if keys[pg.K_LEFT]:
            player.x -= Stats["SPD"]/10
        
        if keys[pg.K_RIGHT]:
            player.x += Stats["SPD"]/10

        if keys[pg.K_o]:
            coffre1.open()

    pg.quit()


if __name__ == "__main__":
    main()