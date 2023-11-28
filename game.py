import pygame
import pygame as pg
from player import Player
from enemies import Enemies
from utilities import Utilities
# this is "from (filename) import (class name)
from pygame.locals import *
import os


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

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    WHITE = (254, 254, 254)

    player = Player(0, 3)

    # we don't have to keep it this way I am just testing the images
    car1 = Enemies('frogger-car1.png', [100, 610])
    car2 = Enemies('frogger-car2.png', [860, 565])
    car3 = Enemies('frogger-car3.png', [100, 520])
    car12 = Enemies('frogger-car1.png', [100, 475])
    car22 = Enemies('frogger-car2.png', [860, 425])
    log1 = Utilities('frogger-log.png', [100, 330])
    turtle = Utilities('frogger-turtle.png', [100, 275])
    log2 = Utilities('frogger-log.png', [100, 220])
    turtle2 = Utilities('frogger-turtle.png', [100, 170])

    enemies = pg.sprite.Group()

    # TODO this is not right but a rough outline from the source code given

    # set up flies TODO is there a better way to do this
    flies = []

    fly1 = Utilities('frogger-fly.png', [75, 110])
    fly2 = Utilities('frogger-fly.png', [210, 110])
    fly3 = Utilities('frogger-fly.png', [345, 110])
    fly4 = Utilities('frogger-fly.png', [480, 110])
    fly5 = Utilities('frogger-fly.png', [620, 110])
    fly6 = Utilities('frogger-fly.png', [760, 110])
    fly7 = Utilities('frogger-fly.png', [895, 110])

    flies.append(fly1)
    flies.append(fly2)
    flies.append(fly3)
    flies.append(fly4)
    flies.append(fly5)
    flies.append(fly6)
    flies.append(fly7)

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
        car1.draw(screen)
        car2.draw(screen)
        car3.draw(screen)
        car12.draw(screen)
        car22.draw(screen)
        log1.draw(screen)
        log2.draw(screen)
        turtle2.draw(screen)

        for fly in flies:
            fly.draw(screen)

        turtle.draw(screen)

        delta = clock.tick(60) / 1000  # gives us how many ms the frame has taken

        pg.display.flip()


if __name__ == "__main__":
    main()
