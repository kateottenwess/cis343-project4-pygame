import pygame as pg
from player import Player
from enemies import Enemies
from utilities import Utilities
# this is "from (filename) import (class name)
from pygame.locals import *
import os
import pygame.freetype


class Game(pg.sprite.Sprite):
    
    def __init__(self, image_file, location):
        value = 1
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        # TODO create properties and setters?
        
        # creating a sprite group out of flies for sprite collide fxn call
        self.fly_group = self.init_flies(); 

    def init_flies(self):
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
        
        fly_group = pg.sprite.Group(flies)  
        return fly_group
        

# TODO is this supposed to be in class
def main():
    # start pg
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

    # set up logs TODO is there a better way to do this
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
    
    # creating a sprite group out of logs for sprite collide fxn call
    log_group = pg.sprite.Group(logs)  

    # set up turtles
    turtles = []

    turtle1 = Utilities('frogger-turtle.png', [100, 275])
    turtle2 = Utilities('frogger-turtle.png', [150, 275])
    turtle3 = Utilities('frogger-turtle.png', [200, 275])
    turtle4 = Utilities('frogger-turtle.png', [500, 275])
    turtle5 = Utilities('frogger-turtle.png', [550, 275])
    turtle6 = Utilities('frogger-turtle.png', [600, 275])
    turtle7 = Utilities('frogger-turtle.png', [300, 170])
    turtle8 = Utilities('frogger-turtle.png', [350, 170])
    turtle9 = Utilities('frogger-turtle.png', [400, 170])
    turtle10 = Utilities('frogger-turtle.png', [800, 170])
    turtle11 = Utilities('frogger-turtle.png', [850, 170])
    turtle12 = Utilities('frogger-turtle.png', [900, 170])

    turtles.append(turtle1)
    turtles.append(turtle2)
    turtles.append(turtle3)
    turtles.append(turtle4)
    turtles.append(turtle5)
    turtles.append(turtle6)
    turtles.append(turtle7)
    turtles.append(turtle8)
    turtles.append(turtle9)
    turtles.append(turtle10)
    turtles.append(turtle11)
    turtles.append(turtle12)
    
    # creating a sprite group out of fly list for sprite collide fxn call
    turtle_group = pg.sprite.Group(turtles)  

    # set up slower cars
    slow_cars = []

    car1 = Enemies('frogger-car1.png', [100, 610])
    car2 = Enemies('frogger-car1.png', [450, 610])
    car3 = Enemies('frogger-car1.png', [0, 475])
    car4 = Enemies('frogger-car1.png', [600, 475])

    slow_cars.append(car1)
    slow_cars.append(car2)
    slow_cars.append(car3)
    slow_cars.append(car4)
    
    # creating a sprite group out of slow cars for sprite collide fxn call
    slow_car_group = pg.sprite.Group(slow_cars)  

    # set up faster cars
    fast_cars = []

    car5 = Enemies('frogger-car2.png', [860, 565])
    car6 = Enemies('frogger-car2.png', [300, 565])
    car7 = Enemies('frogger-car3.png', [50, 520])
    car8 = Enemies('frogger-car3.png', [650, 520])
    car9 = Enemies('frogger-car2.png', [950, 425])
    car10 = Enemies('frogger-car2.png', [425, 425])

    fast_cars.append(car5)
    fast_cars.append(car6)
    fast_cars.append(car7)
    fast_cars.append(car8)
    fast_cars.append(car9)
    fast_cars.append(car10)

    # creating a sprite group out of slow cars for sprite collide fxn call
    fast_car_group = pg.sprite.Group(fast_cars)  

    # Startup the main game loop
    running = True
    delta = 0
    # shotDelta = 500
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    score = 0

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
        if len(bg.fly_group) == 0:     
            # Add a You've won screen?
            print("You've consumed all the flies!")
            return

        # TODO determine if checks need to be done here if frogger hit car or fell in waater

        player.update(delta)

        for log in logs:
            log.update_right(0.01)

        for turtle in turtles:
            turtle.update_left(0.01)

        for car in slow_cars:
            car.update_right(0.01)

        for car in fast_cars:
            car.update_left(0.0211)

        # Checks for collisions between player and any of the flies, the True removes a fly from the flies group when collision occurs
        fly_hits = pg.sprite.spritecollide(player, bg.fly_group, True)
        
        for hit in fly_hits:
            # Increment score when frog eats a fly 
            player.points += 100
            player.reset()
         
        # Checks for collisions between player and any of the cars  ----------------------------------------------
        slow_hits = pg.sprite.spritecollide(player, slow_car_group, False)
        fast_hits = pg.sprite.spritecollide(player, fast_car_group, False)
        
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
        # Checking for collisions with logs or turtles to ride them -------------------------------------------
            
        # Check for collisions between frog and logs
        log_hits = pygame.sprite.spritecollide(player, log_group, False)
        for log in log_hits:
            # Update frog's position based on the log's movement
            player.rect.x = log.rect.x 

        # Check for collisions between frog and turtles
        turtle_hits = pygame.sprite.spritecollide(player, turtle_group, False)
        for turtle in turtle_hits:
            # Update frog's position based on the turtle's movement
            player.rect.x = turtle.rect.x 
            
        # draw
        screen.fill([255, 255, 255])
        screen.blit(bg.image, bg.rect)

        for fly in bg.fly_group:  # changed to group
            fly.draw(screen)

        for log in logs:
            log.draw(screen)

        for turtle in turtles:
            turtle.draw(screen)

        for car in fast_cars:
            car.draw(screen)

        for car in slow_cars:
            car.draw(screen)

        # redraw lives and score

        font.render_to(screen, (10, 10), "Lives: ", RED, None, size=60)
        font.render_to(screen, (215, 10), str(player.lives), WHITE, None, size=60)
        font.render_to(screen, (350, 10), "Score: ", RED, None, size=60)
        font.render_to(screen, (575, 10), str(player.points), WHITE, None, size=60)

        player.draw(screen)

        # flip when drawing is done

        pg.display.flip()

        delta = clock.tick(fps) / 1000  # gives us how many ms the frame has taken
        
    '''
    # Check for collisions between frog and river (if falling into the river)
    if player.rect.bottom < river_surface_rect.top:         # find cooridinates
        # Frog fell into the river
        player.rect.center = (player.rect.width // 2, player.rect.height - 50)
        player.lives -= 1
        player.reset()  
    ''' 


if __name__ == "__main__":
    main()
    pg.quit()
