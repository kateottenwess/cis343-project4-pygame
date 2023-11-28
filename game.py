import pygame
import pygame as pg
from player import Player
from enemies import Enemies
# this is "from (filename) import (class name)
from pygame.locals import *


class Game(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        value = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        # TODO create properties and setters?


# TODO is this supposed to be in class
def main():
    # start pygame
    pg.init()

    # get screen object
    screen = pg.display.set_mode((960, 720))

    player = Player()

    enemies = pg.sprite.Group()

    # TODO this is not right but a rough outline from the source code given

    # car 1
    '''
    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemies((i, j))
            enemies.add(enemy)
    '''


    bg = Game('./assets/frogger-background.png', [0, 0])
    running = True
    # instantiate game object here!
    clock = pg.time.Clock()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # update things that need to be updated

        # draw & re render outputs
        # below (2) are used to create background
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)
        # our_go.draw(screen)
        pg.display.flip()
        player.draw(screen)

        delta = clock.tick(60) / 1000  # gives us how many ms the frame has taken

        pg.display.flip()


if __name__ == "__main__":
    main()
