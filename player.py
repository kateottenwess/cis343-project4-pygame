from units import Units


class Player(Units):
    def __init__(self, points, lives):
        super(Player, self).__init__([460, 700], 'frogger-small.png')
        self.__points = points
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
        self.points = points

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
        # TODO is this being blank the reason mr frog isn't moving
        pass

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
