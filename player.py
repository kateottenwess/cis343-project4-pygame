import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__();
        self.image = pg.image.load("./megaman.jpg").convert_alpha() # can resolve windows drawing issues
        self.rect = self.image.get_rect()
        self.rect.centerx = 370
        self.rect.centery = 240
        
    def update():
        pass

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 120*delta
            
    def down(self, delta):       
        if self.rect.y < 480:
            self.rect.y += 120*delta