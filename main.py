import pygame as pg
from rooms import Room

S_WIDTH, S_HEIGHT = 800, 700



def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

    x,y = 100,100
    delta = 10

    HP = 100
    ATK = 10
    DEF = 0

    run = True
    while run:
        clock.tick(50)
        # code à mettre ici pour ce qu'il se passe entre 2 images
        
        screen.fill((0,0,0))
        pg.draw.circle(screen, (0,0,255), (x,y), 10)
        Room.draw_room()
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