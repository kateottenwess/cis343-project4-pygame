import pygame as pg
from player import Player
from enemies import Enemies
from utilities import Utilities
from pygame.locals import *
import os
import pygame.freetype


class Game(pg.sprite.Sprite):

    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    @staticmethod
    def start_display(screen, font, color):
        screen.fill((171, 221, 246))

        font.render_to(screen, (10, 10), "Choose your Character", color, None, size=60)
        image_cat = pg.image.load(os.path.join('assets', 'cat.png')).convert_alpha()
        rect_cat = image_cat.get_rect()
        rect_cat.x, rect_cat.y = 150, 300
        image_dog = pg.image.load(os.path.join('assets', 'dog.png')).convert_alpha()
        rect_dog = image_dog.get_rect()
        rect_dog.x, rect_dog.y = 400, 300
        image_bird = pg.image.load(os.path.join('assets', 'bird.png')).convert_alpha()
        rect_bird = image_bird.get_rect()
        rect_bird.x, rect_bird.y = 650, 300
        screen.blit(image_cat, rect_cat)
        screen.blit(image_dog, rect_dog)
        screen.blit(image_bird, rect_bird)
        font.render_to(screen, (60, 400), "Press a for Cat          Press s for Dog          Press d for Bird", color,
                       None,
                       size=20)


def main():
    # start pg
    pg.init()

    screen = pg.display.set_mode((960, 720))

    # Get font setup
    pg.font.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets/", "PottaOne-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    WHITE = (254, 254, 254)
    RED = (246, 46, 46)

    Game.start_display(screen, font, WHITE)

    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)

    pg.display.flip()
    image = ''
    got_image = False

    while not got_image:
        clock.tick(60)

        pygame.event.pump()

        keys = pg.key.get_pressed()
        if keys[K_a]:
            image = 'cat.png'
            got_image = True
        if keys[K_s]:
            image = 'dog.png'
            got_image = True
        if keys[K_d]:
            image = 'bird.png'
            got_image = True

    # create player object
    player = Player(0, 3, image)

    pg.display.flip()

    # get screen object
    screen = pg.display.set_mode((960, 720))
    bg = Game('./assets/background.png', [0, 0])

    # create enemies and utilities
    stars_group = Utilities.init_stars()
    fast_cars = Enemies.init_fast_cars()
    turtles = Utilities.init_turtles()
    logs = Utilities.init_logs()
    slow_cars = Enemies.init_slow_cars()

    # Startup the main game loop
    running = True
    delta = 0

    # MAIN GAME LOOP
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
        if len(stars_group) == 0:
            # Add a You've won screen?
            print("You've collected all the stars!")
            return

        # TODO determine if checks need to be done here if frogger hit car or fell in water

        player.update(delta)

        for log in logs:
            log.update_right(0.01)

        for turtle in turtles:
            turtle.update_left(0.01)

        for car in slow_cars:
            car.update_right(0.01)

        for car in fast_cars:
            car.update_left(0.0211)

        # Checks for collisions between player and any of the flies, the True removes a fly from the flies group when
        # collision occurs
        star_hits = pg.sprite.spritecollide(player, stars_group, True)

        for hit in star_hits:
            # Increment score when frog eats a fly 
            player.points += 100
            player.reset()

        # Checks for collisions between player and any of the cars  ----------------------------------------------
        slow_hits = pg.sprite.spritecollide(player, slow_cars, False)
        fast_hits = pg.sprite.spritecollide(player, fast_cars, False)

        for hit in slow_hits:
            # Decrement player lives when they get hit
            if player.lives > 0:
                player.lives -= 1
                player.reset()
            else:
                # Add a You've lost screen?
                print("DEAD.....You lost!")
                return

        for hit in fast_hits:
            # Decrement player lives when they get hit
            if player.lives > 0:
                player.lives -= 1
                player.reset()
            else:
                # Add a You've lost screen?
                print("DEAD.....You lost!")
                return

        # Check for collisions between frog and river (if falling into the river)
        if 330 >= player.rect.bottom >= 210:
            # Check for collisions between frog and logs
            log_hits = pygame.sprite.spritecollide(player, logs, False)
            # Check for collisions between frog and turtles
            turtle_hits = pygame.sprite.spritecollide(player, turtles, False)

            if log_hits or turtle_hits:  # Use 'or' to check if either logs or turtles are hit
                # Update frog's position based on the first log or turtle hit (if any)
                if log_hits:
                    player.rect.x = log_hits[0].rect.x
                elif turtle_hits:
                    player.rect.x = turtle_hits[0].rect.x
            else:
                # Frog fell into the river without hitting logs or turtles
                player.lives -= 1
                player.reset()

        # Checking for collisions with logs or turtles to ride them -------------------------------------------

        # draw
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)

        for fly in stars_group:  # changed to group
            fly.draw(screen)

        for log in logs:
            log.draw(screen)

        for turtle in turtles:
            turtle.draw(screen)

        for car in fast_cars:
            car.draw(screen)

        for car in slow_cars:
            car.draw(screen)

        for log in logs:
            if player.rect.colliderect(log.rect):
                player.rect.x = log.rect.x

        for turtle in turtles:
            if player.rect.colliderect(turtle.rect):
                player.rect.x = turtle.rect.x

        # redraw lives and score

        font.render_to(screen, (10, 10), "Lives: ", RED, None, size=60)
        font.render_to(screen, (215, 10), str(player.lives), WHITE, None, size=60)
        font.render_to(screen, (350, 10), "Score: ", RED, None, size=60)
        font.render_to(screen, (575, 10), str(player.points), WHITE, None, size=60)

        player.draw(screen)

        # flip when drawing is done

        pg.display.flip()

        delta = clock.tick(fps) / 1000  # gives us how many ms the frame has taken


if __name__ == "__main__":
    main()
    pg.quit()
