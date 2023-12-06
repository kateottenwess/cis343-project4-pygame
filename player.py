from units import Units
import pygame as pg

''' By Anna Rabe and Kate Ottenwess'''

class Player(Units):
    """ The Player class for the Game. Contains the methods and attributes
    relating to updating the player's status throughout game changes.

    Attributes:
        lives: The remaining lives the player has, starts at 3, game ends if they reach 0.
        points: The amount of points the player has earned, maximum is 700. 
                Game ends if they reach this.
        
    """
    def __init__(self, points, lives, image):
        super(Player, self).__init__([460, 700], image)
        self.__points = points
        self.__lives = lives
        
    # getter for points that the player has
    @property
    def points(self):
        return self.__points
    
    # getter for lives that the player has left
    @property
    def lives(self):
        return self.__lives
    
    # setter for points that the player has
    @points.setter
    def points(self, points):
        if not points:
            raise ValueError("Points cannot be blank.")
        if not isinstance(points, int):
            raise ValueError("Points must be an int.")
        if points < 0:
            raise ValueError("Points can not be negative")
        self.__points = points

    # setter for lives that the player has left
    @lives.setter
    def lives(self, lives):
        if not lives:
            raise ValueError("YOU LOST.")
        if not isinstance(lives, int):
            raise ValueError("Lives must be an int.")
        if lives < 0 or lives > 3:
            raise ValueError("Player must have within 0 and 3 lives")
        self.__lives = lives

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Updates players position based on the arrow keys that the user presses.
    def update(self, delta):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pg.K_RIGHT] and self.rect.right < 960:
            self.rect.x += 5
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pg.K_DOWN] and self.rect.bottom < 720:
            self.rect.y += 5

    # Resets the player back to its starting position at the bottom of the screen.
    def reset(self):
        self.rect.x = 460
        self.rect.y = 700
