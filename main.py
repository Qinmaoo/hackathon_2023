import pygame as pg

S_WIDTH, S_HIGHT = 800, 700
# R_WIDTH, R_HIGHT = 300, 500
R_COLOR = [122, 52, 24]
D_w, D_h = 50, 10
D_COLOR = [196, 102, 65]

class Room(pg.Rect):

    def __init__(self, l, t, w, h):
        super().__init__(l, t, w, h)


def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HIGHT))

    def create_room():
        room_1 = Room(0, 0, S_WIDTH, S_HIGHT)
        door_t = Room((S_WIDTH-D_w)/2, 0, D_w, D_h)

        pg.draw.rect(screen, R_COLOR, room_1, width= 5)
        pg.draw.rect(screen, D_COLOR, door_t, width= D_h//2)

    x,y = 100,100

    #Stats
    HP = 100
    
    Stats = {
        "HP_MAX" : 100,
        "ATK" : 10,
        "DEF" : 0,
        "SPD" : 15,
        "RANGE" : 50,
        "FIRE_RATE" : 100
    }

    run = True
    while run:
        clock.tick(50)

        create_room()
        # code à mettre ici pour ce qu'il se passe entre 2 images
        
        screen.fill((0,0,0))
        pg.draw.circle(screen, (0,0,255), (x,y), 10)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN and (event.key == pg.K_q or event.key == pg.K_ESCAPE):
                run = False

        keys = pg.key.get_pressed()
        
        if keys[pg.K_DOWN]:
            y += Stats["SPD"]/10
        
        if keys[pg.K_UP]:
            y -= Stats["SPD"]/10

        if keys[pg.K_LEFT]:
            x -= Stats["SPD"]/10
        
        if keys[pg.K_RIGHT]:
            x += Stats["SPD"]/10

    pg.quit()


if __name__ == "__main__":
    main()
