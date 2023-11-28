from units import Units


class Utilities(Units):
    def __init__(self, image_name, start_location):
        super(Utilities, self).__init__(start_location, image_name)
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
