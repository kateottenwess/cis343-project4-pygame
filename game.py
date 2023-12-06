import pygame as pg
from player import Player
from enemies import Enemies
from utilities import Utilities
from pygame.locals import *
import os
import pygame.freetype


"""
    PyGame 8 - Bit Arcade Game
    CIS 343
    By Anna Rabe and Kate Ottenwess
    
    _summary_
    Use the keyboard to select a character to start. Then, use the arrow
    keys to navigate through the road of cars without getting hit. Next,
    navigate across the river without falling in by jumping from logs to 
    turtles, until you reach a star. Collect all the stars without losing
    your lives and you win!
"""

class Game(pg.sprite.Sprite):

    """ The Game class for the Game. Contains the initializer for the game
        attributes, and function to start up the game display.

    Attributes:
        self.image: The background image for the game.
        self.rect: The rectangle containing the player position.
        self.river_top: The upper y-cooridinates of the rivers location.
        self.river_bottom: The lower y-cooridinates of the rivers location.
        
    """
        
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.river_top = 380
        self.river_bottom = 180

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
    
    """ The Main Game Loop. Creates an instance of the game class, 
    initializing it, and running it. 
    
    Takes user input to select a character, initializing it with the selected image.
    Creates sprite groups for each utility and enemy type. Checks sprite groups for 
    collisions with the player and executes appropriate actions. Updates player movement,
    lives, and points as game progresses, checking for winning and losing conditions 
    until one is met.
    """
    
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
        
        # Taking user input to determine character selection
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
    game = Game('./assets/background.png', [0, 0])

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

        # update player
        player.update(delta)

        if len(stars_group) == 0:
            print("You've collected all the stars!")
            return

        for log in logs:
            log.update_right(0.01)

        for turtle in turtles:
            turtle.update_left(0.01)

        for car in slow_cars:
            car.update_right(0.01)

        for car in fast_cars:
            car.update_left(0.0211)

        # Checks for collisions between player and any of the stars, the True removes a star from the stars group when
        # collision occurs
        star_hits = pg.sprite.spritecollide(player, stars_group, True)

        for hit in star_hits:
            # Increment score when player collects a star 
            player.points += 100
            player.reset()

        # Checks for collisions between player and any of the cars  ----------------------------------------------
        slow_hits = pg.sprite.spritecollide(player, slow_cars, False)
        fast_hits = pg.sprite.spritecollide(player, fast_cars, False)

        for hit in slow_hits + fast_hits:
            # Decrement player lives when they get hit
            if player.lives > 0:
                player.lives -= 1
                player.reset()
            else:
                print("DEAD.....You lost!")
                return

        # Check for collisions between player and river -----------------------------------------------------------
        if game.river_top > player.rect.bottom >= game.river_bottom:
            # Check for collisions between player and logs
            log_hits = pygame.sprite.spritecollide(player, logs, False)
            # Check for collisions between player and turtles
            turtle_hits = pygame.sprite.spritecollide(player, turtles, False)

            # Checking for collisions with logs or turtles to ride them -------------------------------------------
            if log_hits or turtle_hits:  # Use 'or' to check if either logs or turtles are hit
                # Update player position based on the log or turtle hit (if any)
                if log_hits:
                    player.rect.x = log_hits[0].rect.x
                elif turtle_hits:
                    player.rect.x = turtle_hits[0].rect.x
            else:
                # player fell into the river without hitting logs or turtles
                player.lives -= 1
                player.reset()

        # draw
        screen.fill([255, 255, 255])
        screen.blit(game.image, game.rect)

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
