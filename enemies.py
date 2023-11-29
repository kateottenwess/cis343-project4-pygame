import pygame as pg
from units import Units


class Enemies(Units):
    def __init__(self, image_name, start_location):
        super(Enemies, self).__init__(start_location, image_name)
        # TODO do we need to set the image things or since its done in units we dont need to?

    # TODO create a function to determine if player is hit by enemy
