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
    delta = 10

    HP = 100
    ATK = 10
    DEF = 0

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

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    run = False
                
                if event.key == pg.K_DOWN:
                    y += delta
                
                if event.key == pg.K_UP:
                    y -= delta

                if event.key == pg.K_LEFT:
                    x -= delta
                
                if event.key == pg.K_RIGHT:
                    x += delta
    pg.quit()


if __name__ == "__main__":
    main()


    
