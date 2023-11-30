from units import Units
import pygame as pg


class Player(Units):
    def __init__(self, points, lives):
        super(Player, self).__init__([460, 700], 'frogger-small.png')
        self.__points = 0
        self.__lives = lives
        # TODO do we need to set the image things or since its done in units we dont need to?

    @property
    def points(self):
        return self.__points

    @property
    def lives(self):
        return self.__lives

    @points.setter
    def points(self, points):
        if not points:
            raise ValueError("Points cannot be blank.")
        if not isinstance(points, int):
            raise ValueError("Name must be an int.")
        if points < 0:
            raise ValueError("Points can not be negative")
        self.__points = points

    @lives.setter
    def lives(self, lives):
        if not lives:
            raise ValueError("lives cannot be blank.")
        if not isinstance(lives, int):
            raise ValueError("Name must be an int.")
        if lives < 0 or lives > 3:
            raise ValueError("Player must have within 0 and 3 lives")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        # TODO is this being blank the reason mr frog isn't moving ? Maybe lets test an implmentation...
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pg.K_RIGHT] and self.rect.right < 960:
            self.rect.x += 5
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pg.K_DOWN] and self.rect.bottom < 720:
            self.rect.y += 5

    def reset(self):
        self.rect.x = 460
        self.rect.y = 700

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 120 * delta
        # TODO

    def down(self, delta):
        if self.rect.y < 480:
            self.rect.y += 120 * delta
        # TODO

    def left(self, delta):
        pass
        # TODO

    def right(self, delta):
        pass
        # TODO
