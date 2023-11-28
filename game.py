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

    # we don't have to keep it this way I am just testing the images
    car1 = Enemies('frogger-car1.png', [100, 610])
    car2 = Enemies('frogger-car2.png', [860, 565])
    car3 = Enemies('frogger-car3.png', [100, 520])
    car12 = Enemies('frogger-car1.png', [100, 475])
    car22 = Enemies('frogger-car2.png', [860, 425])
    log1 = Enemies('frogger-log.png', [100, 325])
    turtle = Enemies('frogger-turtle.png', [100, 290])

    enemies = pg.sprite.Group()

    # TODO this is not right but a rough outline from the source code given

    # set up flies TODO is there a better way to do this
    flies = []

    fly1 = Enemies('frogger-fly.png', [75, 110])
    fly2 = Enemies('frogger-fly.png', [210, 110])
    fly3 = Enemies('frogger-fly.png', [345, 110])
    fly4 = Enemies('frogger-fly.png', [480, 110])
    fly5 = Enemies('frogger-fly.png', [620, 110])
    fly6 = Enemies('frogger-fly.png', [760, 110])
    fly7 = Enemies('frogger-fly.png', [895, 110])

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

        for fly in flies:
            fly.draw(screen)


        turtle.draw(screen)

        delta = clock.tick(60) / 1000  # gives us how many ms the frame has taken

        pg.display.flip()


if __name__ == "__main__":
    main()
