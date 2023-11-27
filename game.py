import pygame
import pygame as pg
from pygame.locals import *

class Game(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        value = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def main():
    # start pygame
    pg.init()
    
    # get screen object
    screen = pg.display.set_mode((960, 720))
    bg = Game('./assets/frogger-background.png', [0, 0])
    running = True
   # instantiate game object here!
    #clock =

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # update things that need to be updated

        # draw & re render outputs
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)
        #our_go.draw(screen)
        pg.display.flip()
        clock = pg.time.Clock()
        delta = clock.tick(60)/1000     # gives us how many ms the frame has taken
       
        pg.display.flip()


if __name__ == "__main__":
    main()