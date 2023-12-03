from units import Units
import pygame as pg


class Utilities(Units):
    def __init__(self, image_name, start_location):
        super(Utilities, self).__init__(start_location, image_name)
        # TODO do we need to set the image things or since its done in units we dont need to?

    # update function for the flies
    def update_fly(self, delta):
        pass

    @staticmethod
    def init_flies():
        # set up flies TODO is there a better way to do this
        flies = []

        fly1 = Utilities('frogger-fly.png', [75, 110])
        fly2 = Utilities('frogger-fly.png', [210, 110])
        fly3 = Utilities('frogger-fly.png', [345, 110])
        fly4 = Utilities('frogger-fly.png', [480, 110])
        fly5 = Utilities('frogger-fly.png', [620, 110])
        fly6 = Utilities('frogger-fly.png', [760, 110])
        fly7 = Utilities('frogger-fly.png', [895, 110])

        flies.append(fly1)
        flies.append(fly2)
        flies.append(fly3)
        flies.append(fly4)
        flies.append(fly5)
        flies.append(fly6)
        flies.append(fly7)

        fly_group = pg.sprite.Group(flies)
        return fly_group

    @staticmethod
    def init_turtles():
        # set up turtles
        turtles = []

        turtle1 = Utilities('frogger-turtle.png', [100, 275])
        turtle2 = Utilities('frogger-turtle.png', [150, 275])
        turtle3 = Utilities('frogger-turtle.png', [200, 275])
        turtle4 = Utilities('frogger-turtle.png', [500, 275])
        turtle5 = Utilities('frogger-turtle.png', [550, 275])
        turtle6 = Utilities('frogger-turtle.png', [600, 275])
        turtle7 = Utilities('frogger-turtle.png', [300, 170])
        turtle8 = Utilities('frogger-turtle.png', [350, 170])
        turtle9 = Utilities('frogger-turtle.png', [400, 170])
        turtle10 = Utilities('frogger-turtle.png', [800, 170])
        turtle11 = Utilities('frogger-turtle.png', [850, 170])
        turtle12 = Utilities('frogger-turtle.png', [900, 170])

        turtles.append(turtle1)
        turtles.append(turtle2)
        turtles.append(turtle3)
        turtles.append(turtle4)
        turtles.append(turtle5)
        turtles.append(turtle6)
        turtles.append(turtle7)
        turtles.append(turtle8)
        turtles.append(turtle9)
        turtles.append(turtle10)
        turtles.append(turtle11)
        turtles.append(turtle12)

        # creating a sprite group out of fly list for sprite collide fxn call
        turtle_group = pg.sprite.Group(turtles)
        return turtle_group

    @staticmethod
    def init_logs():
        logs = []

        log1 = Utilities('frogger-log.png', [-100, 330])
        log2 = Utilities('frogger-log.png', [350, 330])
        log3 = Utilities('frogger-log.png', [650, 330])
        log4 = Utilities('frogger-log.png', [150, 220])
        log5 = Utilities('frogger-log.png', [450, 220])
        log6 = Utilities('frogger-log.png', [850, 220])

        logs.append(log1)
        logs.append(log2)
        logs.append(log3)
        logs.append(log4)
        logs.append(log5)
        logs.append(log6)

        # creating a sprite group out of logs for sprite collide fxn call
        log_group = pg.sprite.Group(logs)
        return log_group
