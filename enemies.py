import pygame as pg
from units import Units


class Enemies(Units):
    def __init__(self, image_name):
        super(Enemies, self).__init__([370, 240], image_name, [50, 30])
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
