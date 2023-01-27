import pygame as pg
import pygame_menu as pgm
from items_stats import *
from rooms import Room, Player
import numpy as np
from enemies import gen_enemy, dist
from itertools import product

S_WIDTH, S_HEIGHT = 800, 700
R_COLOR = [122, 52, 24]
D_w, D_h = 50, 30
D_COLOR = [196, 102, 65]

room_grid = {}
for i,j in product(range(4), range(4)):
    enem = gen_enemy()
    room_grid[(i,j)] = Room(enem, (i,j))

coffre1 = Chest()


def change_character(name="Alban", photo="alban.jpg"):
    return photo


def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

    player = Player(100, 100)

    white = (255, 255, 255)
    stat_font = pg.font.SysFont("Helvetica", 15)

    title_menu = pgm.Menu(
        height=0.8 * S_HIGHT,
        theme=pgm.themes.THEME_BLUE,
        title="Title screen",
        width=0.9 * S_WIDTH,
    )

    def disabling(menu=title_menu):
        menu.disable()

    logo = pgm.baseimage.BaseImage("textures/logo.png")
    title_menu.add.banner(logo, pgm.events.NONE)
    character_selection = title_menu.add.selector(
        "Character :",
        [
            ("Alban", "alban.png"),
            ("El Tuno", "alexis.png"),
            ("Aymeric", "aymeric.png"),
            ("Laure", "laure.png"),
            ("Matéo", "mateo.png"),
            ("Mattéo", "matteo.png"),
            ("Noah-Luc", "NL.png"),
            ("Noé", "noe.png"),
            ("Raphaelle", "raph.png"),
            ("Thibault", "thibault.png"),
            ("Tom", "tom.png"),
            ("Yoan", "yoan.png"),
        ],
        onchange=change_character,
    )
    title_menu.add.button("Start", disabling)
    title_menu.add.button("Quit", pgm.events.EXIT)

    room = Room(gen_enemy(),(0,0))

    is_attacking = False
    cooldown = 0

    run = True
    while run:
        clock.tick(50)

        # Entre affichage de deux images
        screen.fill((133, 80, 64))
        screen.blit(coffre1.texture, (200, 200))
        joueur = pg.transform.rotozoom(
            (
                pg.image.load(
                    "textures/" + character_selection.get_value()[0][1]
                ).convert_alpha()
            ),
            0,
            0.2,
        )
        attack = pg.transform.rotozoom(
            (pg.image.load("textures/attack.png").convert_alpha()), 0, 0.2
        )

        enemy_list = room.enemies

        text_atk = stat_font.render(f"ATK : {Stats['ATK']}", True, white)
        text_def = stat_font.render(f"DEF : {Stats['DEF']}", True, white)
        text_spd = stat_font.render(f"SPD : {Stats['SPD']}", True, white)
        text_range = stat_font.render(f"RNG : {Stats['RANGE']}", True, white)
        text_fire = stat_font.render(f"RTE : {Stats['FIRE_RATE']}", True, white)

        
        
        room_grid[rooms.current_room].interact_wall(player)
        room_grid[rooms.current_room].switch_rooms(player)

        screen.blit(text_atk, (20, 50))
        screen.blit(text_def, (20, 80))
        screen.blit(text_spd, (20, 110))
        screen.blit(text_range, (20, 140))
        screen.blit(text_fire, (20, 170))

        for enemy in enemy_list:
            if enemy.trap:
                pass
            else:
                if player.x < enemy.x:
                    enemy.x -= enemy.spd / 10
                elif player.x > enemy.x:
                    enemy.x += enemy.spd / 10
                if player.y < enemy.y:
                    enemy.y -= enemy.spd / 10
                elif player.y > enemy.y:
                    enemy.y += enemy.spd / 10
        
        if is_attacking:
            if cooldown == Stats["FIRE_RATE"]:
                for enemy in enemy_list:
                    pass

            cooldown -= 1

            if cooldown <= 0:
                is_attacking = False
                cooldown = 0

            screen.blit(attack, (player.x - 25, player.y - 25))

        
        screen.blit(joueur, (player.x, player.y))

        for enemy in enemy_list:
            screen.blit(enemy.sprite(), (enemy.x, enemy.y))

        room.draw_room(screen)

        pg.display.update()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN and (event.key == pg.K_q or event.key == pg.K_ESCAPE):
                run = False
            if event.type == pg.KEYDOWN and event.key == pg.K_c:
                title_menu.enable()
                title_menu.mainloop(screen)
                title_menu.disable()

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and cooldown == 0:
                is_attacking = True
                cooldown = Stats["FIRE_RATE"]

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

        pos_joueur = joueur.get_rect()
        pos_joueur.x, pos_joueur.y = player.x, player.y
        pos_coffre = coffre1.texture.get_rect()
        pos_coffre.x, pos_coffre.y = 200, 200
        if pos_joueur.colliderect(pos_coffre) and coffre1.status == "closed":
            coffre1.open()
            coffre1.content.item_get()

    pg.quit()


if __name__ == "__main__":
    main()
