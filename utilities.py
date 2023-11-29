from units import Units


class Utilities(Units):
    def __init__(self, image_name, start_location):
        super(Utilities, self).__init__(start_location, image_name)
        # TODO do we need to set the image things or since its done in units we dont need to?

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_log(self, delta):
        # logs move to the right
        self.rect.x += 100 * delta

        # if center of log goes past right edge, reset to left
        if self.rect.x > 960:
            self.rect.x = -200

    def update_turtle(self, delta):
        # turtles move to left
        self.rect.x += 100 * delta * -1

        # if center of log goes past left edge, reset to right
        if self.rect.x < -60:
            self.rect.x = 1000

    def up(self, delta):
        if self.rect.y > 0:
            self.rect.y -= 120 * delta

    def down(self, delta):
        if self.rect.y < 480:
            self.rect.y += 120 * delta
