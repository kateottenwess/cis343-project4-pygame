import pygame
import pygame as pg
from player import Player
from enemies import Enemies
from utilities import Utilities
# this is "from (filename) import (class name)
from pygame.locals import *
import os
import pygame.freetype


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
    bg = Game('./assets/frogger-background.png', [0, 0])

    # Get font setup
    pg.font.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/", "PottaOne-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    WHITE = (254, 254, 254)
    RED = (246, 46, 46)

    # create player object
    player = Player(0, 3)

    # TODO we don't have to keep it this way I am just testing the images
    car1 = Enemies('frogger-car1.png', [100, 610])
    car2 = Enemies('frogger-car2.png', [860, 565])
    car3 = Enemies('frogger-car3.png', [100, 520])
    car12 = Enemies('frogger-car1.png', [100, 475])
    car22 = Enemies('frogger-car2.png', [860, 425])
    log1 = Utilities('frogger-log.png', [-100, 330])
    turtle = Utilities('frogger-turtle.png', [100, 275])
    log2 = Utilities('frogger-log.png', [100, 220])
    turtle2 = Utilities('frogger-turtle.png', [100, 170])

    enemies = pg.sprite.Group()

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

    # set up logs
    logs = []

    log1 = Utilities('frogger-log.png', [-100, 330])
    log2 = Utilities('frogger-log.png', [350, 330])
    log3 = Utilities('frogger-log.png', [650, 330])
    log4 = Utilities('frogger-log.png', [150, 220])
    log5 = Utilities('frogger-log.png', [450, 220])
    log6 = Utilities('frogger-log.png', [850, 220])

    logs.append(log1)
    logs.append(log2)
    logs.append(log3)
    logs.append(log4)
    logs.append(log5)
    logs.append(log6)

    # car 1
    '''
    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemies((i, j))
            enemies.add(enemy)
    '''

    # Startup the main game loop
    running = True
    delta = 0
    # shotDelta = 500
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    score = 0

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # update things that need to be updated
        # move player
        keys = pg.key.get_pressed()
        if keys[KEYDOWN]:
            player.down(delta)
        if keys[K_LEFT]:
            player.left(delta)
        if keys[KEYUP]:
            player.up(delta)
        if keys[K_RIGHT]:
            player.right(delta)
        if len(flies) == 0:
            print("You've consumed all the flies!")
            return

        # TODO determine if checks need to be done here if frogger hit car or fell in water

        # draw
        # below (2) are used to create background
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)

        player.update(delta)

        for log in logs:
            log.update_log(0.01)

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

        for log in logs:
            log.draw(screen)

        turtle.draw(screen)
        player.draw(screen)

        # redraw lives and score

        font.render_to(screen, (10, 10), "Lives: ", RED, None, size=60)
        font.render_to(screen, (215, 10), str(player.lives), WHITE, None, size=60)
        font.render_to(screen, (350, 10), "Score: ", RED, None, size=60)
        font.render_to(screen, (575, 10), str(player.points), WHITE, None, size=60)

        # flip when drawing is done

        pg.display.flip()

        delta = clock.tick(fps) / 1000  # gives us how many ms the frame has taken


if __name__ == "__main__":
    main()
    pg.quit()
