import pygame as pg

S_WIDTH, S_HEIGHT = 800, 700
R_COLOR = [122, 52, 24]
D_w, D_h = 50, 10
D_COLOR = [196, 102, 65]
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

class Doors():
    
    def __init__(self):
        self.doors = [pg.Rect((S_WIDTH-D_w)/2, 0, D_w, D_h),                # Up door
                      pg.Rect((S_WIDTH-D_w)/2, S_HEIGHT-D_h, D_w, D_h),     # Down door
                      pg.Rect(0, (S_HEIGHT-D_w)/2, D_h, D_w),               # Left door
                      pg.Rect(S_WIDTH-D_h, (S_HEIGHT-D_w)/2, D_h, D_w)]     # Right door

class Room():

    def __init__(self, enemies, room_id):
        self.display = pg.Rect(0, 0, S_WIDTH, S_HEIGHT)
        self.enemies = enemies 
        self.doors = Doors().doors
        self.id = room_id


    def draw_room(self):
        pg.draw.rect(screen, R_COLOR, self.display, width= 5)

        for door in self.doors:
            pg.draw.rect(screen, D_COLOR, door, width= D_h//2)

        for enemy in self.enemies:
            enemy.draw_mob(screen, S_WIDTH, S_HEIGHT)
    
    def swith_rooms(self):
        if (player.x <= D_h) and ((S_HEIGHT-D_w)/2 <= player.y <= (S_HEIGHT+D_w)/2):
            None