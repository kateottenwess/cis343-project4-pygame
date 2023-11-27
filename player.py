import pygame as pg
import units

class Player(units):
    def __init__(self):
        super(Player, self).__init__([370, 240], "frogger.png")


    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def update(self, delta):
        pass

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 120*delta
            
    def down(self, delta):       
        if self.rect.y < 480:
            self.rect.y += 120*delta