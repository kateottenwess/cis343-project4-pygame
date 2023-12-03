import pygame as pg
from units import Units


class Enemies(Units):
    def __init__(self, image_name, start_location):
        super(Enemies, self).__init__(start_location, image_name)

    # TODO create a function to determine if player is hit by enemy

    # Maybe constantly compare player location to enemy locations,
    # and if they intersect then count it as getting hit?
    # Thats my best idea
    @staticmethod
    def init_fast_cars():
        fast_cars = []

        car5 = Enemies('frogger-car2.png', [860, 565])
        car6 = Enemies('frogger-car2.png', [300, 565])
        car7 = Enemies('frogger-car3.png', [50, 520])
        car8 = Enemies('frogger-car3.png', [650, 520])
        car9 = Enemies('frogger-car2.png', [950, 425])
        car10 = Enemies('frogger-car2.png', [425, 425])

        fast_cars.append(car5)
        fast_cars.append(car6)
        fast_cars.append(car7)
        fast_cars.append(car8)
        fast_cars.append(car9)
        fast_cars.append(car10)

        # creating a sprite group out of slow cars for sprite collide fxn call
        fast_car_group = pg.sprite.Group(fast_cars)
        return fast_car_group

    @staticmethod
    def init_slow_cars():
        # set up slower cars
        slow_cars = []

        car1 = Enemies('frogger-car1.png', [100, 610])
        car2 = Enemies('frogger-car1.png', [450, 610])
        car3 = Enemies('frogger-car1.png', [0, 475])
        car4 = Enemies('frogger-car1.png', [600, 475])

        slow_cars.append(car1)
        slow_cars.append(car2)
        slow_cars.append(car3)
        slow_cars.append(car4)

        # creating a sprite group out of slow cars for sprite collide fxn call
        slow_car_group = pg.sprite.Group(slow_cars)
        return slow_car_group
