import pygame as pg


def main():
    clock = pg.time.Clock()

    pg.init()
    screen = pg.display.set_mode((600, 500))

    done = False
    while not done:
        clock.tick(50)

        # code à mettre ici pour ce qu'il se passe entre 2 images

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    done = True
    pg.quit()


if __name__ == "__main__":
    main()
