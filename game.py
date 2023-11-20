import pygame as pg


def main():
    # start pygame
    pg.init()

    # get screen object
    screen = pg.display.set_mode((1024, 768))

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # update things that need to be updated

        # draw

        pg.display.flip()


main()

