import pygame as pg
from units import Units
import os


class Player(Units):
    def __init__(self):
        super(Player, self).__init__([460, 700], 'frogger-small.png')
        # TODO do we need to set the image things or since its done in units we dont need to?

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 120 * delta

    def down(self, delta):
        if self.rect.y < 480:
            self.rect.y += 120 * delta

