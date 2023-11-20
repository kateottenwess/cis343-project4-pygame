import pygame as pg
from pygame.locals import *



class Game():
    def __init__(self):
        value = 1


def main():
    # start pygame
    pg.init()
    
    # get screen object
    screen = pg.display.set_mode((1024, 768))
    running = True
   # instantiate game object here!
    #clock =

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # update things that need to be updated

        # draw & re render outputs
        screen.fill(255, 255, 255)
        #our_go.draw(screen)
        pg.display.flip()
        delta = clock.tick(60)/1000     # gives us how many ms the frame has taken
       
        pg.display.flip()


main()

