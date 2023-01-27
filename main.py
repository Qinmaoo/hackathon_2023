import pygame as pg

def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((600, 500))

    x,y = 0,0
    delta = 10

    hp = 100
    atk = 10
    df = 0

    run = True
    while run:
        clock.tick(50)

        # code à mettre ici pour ce qu'il se passe entre 2 images

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    run = False
                
                if event.key == pg.K_DOWN:
                    y -= delta
                
                if event.key == pg.K_UP:
                    y += delta

                if event.key == pg.K_LEFT:
                    x -= delta
                
                if event.key == pg.K_RIGHT:
                    x += delta
    pg.quit()


if __name__ == "__main__":
    main()