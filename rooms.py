import pygame as pg
from enemies import *

S_WIDTH, S_HEIGHT = 800, 700
R_COLOR = [122, 52, 24]
D_w, D_h = 50, 30
D_COLOR = [196, 102, 65]

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Doors:
    def __init__(self):
        self.doors = [
            pg.Rect((S_WIDTH - D_w) / 2, 0, D_w, D_h),                      # Up door
            pg.Rect((S_WIDTH - D_w) / 2, S_HEIGHT - D_h, D_w, D_h),         # Down door
            pg.Rect(0, (S_HEIGHT - D_w) / 2, D_h, D_w),                     # Left door
            pg.Rect(S_WIDTH - D_h, (S_HEIGHT - D_w) / 2, D_h, D_w),         # Right door
        ]                                                              


class Room:
    def __init__(self, enemies, room_id):
        self.display = pg.Rect(0, 0, S_WIDTH, S_HEIGHT)
        self.enemies = enemies
        self.doors = Doors().doors
        self.id = room_id

    def draw_room(self, screen):
        pg.draw.rect(screen, R_COLOR, self.display, width=15)

        for door in self.doors:
            pg.draw.rect(screen, D_COLOR, door, width=D_h // 2)

        for enemy in self.enemies:
            enemy.draw_mob(screen)
    
    def interact_wall(self, player):
        if player.x < 15:
            player.x = 15
        elif player.x + 45 > S_WIDTH - 15:
            player.x = S_WIDTH - 60
        elif player.y < 15:
            player.y = 15
        elif player.y > S_HEIGHT - 60:
            player.y = S_HEIGHT - 60

    
    def swith_rooms(self, player, current_room):
        i,j = current_room
        if (player.x < D_h) and ((S_HEIGHT-D_w)/2 < player.y < (S_HEIGHT+D_w)/2):                       # through left door
            current_room = i, (j-1)%4
            player.x = S_WIDTH - D_h - 45
        
        elif (player.x > S_WIDTH-D_h - 45) and ((S_HEIGHT-D_w)/2 < player.y < (S_HEIGHT+D_w)/2):        # Through right door
            current_room = i, (j+1)%4
            player.x = D_h
        
        elif (S_WIDTH-D_w)/2 < player.x < (S_WIDTH+D_w)/2 and (player.y < D_h):                         # Through up door
            current_room = (i-1)%4, j
            player.y = S_HEIGHT - D_h - 60
        
        elif (S_WIDTH-D_w)/2 < player.x < (S_WIDTH+D_w)/2 and (player.y + 60 > S_HEIGHT - D_h):              # Through down door
            current_room = (i+1)%4, j
            player.y = D_h
        
    