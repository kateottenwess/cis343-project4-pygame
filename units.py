import pygame as pg
import os

''' By Anna Rabe and Kate Ottenwess'''

class Units(pg.sprite.Sprite):
    def __init__(self, start_location, image_name):
        super(Units, self).__init__()
        self.image = pg.image.load(os.path.join('assets', image_name)).convert_alpha()
        self.__rect = self.image.get_rect()
        self.direction = 1
        self.rect.centerx = start_location[0]
        self.rect.centery = start_location[1]
        self.start_location = start_location

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        if not rect:
            raise ValueError("Rect cannot be blank.")
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_right(self, delta):
        # moving right
        self.rect.x += 100 * delta

        # if center of object goes past right edge, reset to left
        if self.rect.x > 960:
            self.rect.x = -200

    def update_left(self, delta):
        # moving left
        self.rect.x += 100 * delta * -1

        # if center of object goes past left edge, reset to right
        if self.rect.x < -60:
            self.rect.x = 1000
            
