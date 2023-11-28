import pygame as pg
import os


class Units(pg.sprite.Sprite):
    def __init__(self, start_location, image_name):
        super(Units, self).__init__()
        self.image = pg.image.load(os.path.join('assets', image_name)).convert_alpha()
        self.rect = self.image.get_rect()
        self.direction = 1
        self.rect.centerx = start_location[0]
        self.rect.centery = start_location[1]
        self.start_location = start_location
        # not entirely sure why he has the direction set to 1 in example code
        # TODO do we need to create properties for all of the sprite vals

        # define any other functions that enemy and player may have in common here but I don't think there are any since
        # they move differently

    # TODO why is this yelling

    ''' @direction.setter
    def direction(self, value):
        self.__direction = value
    '''

    def draw(self, screen):
        screen.blit(self.image, self.rect)
