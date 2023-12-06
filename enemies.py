import pygame as pg
from units import Units

''' By Anna Rabe and Kate Ottenwess'''

class Enemies(Units):
    """ The Enemy class for the Game. Contains the methods and attributes for the cars
    that can kill the player.

    Attributes:
        n/a
        
    """
    
    def __init__(self, image_name, start_location):
        super(Enemies, self).__init__(start_location, image_name)

   # Initializes fast car enemies
    @staticmethod
    def init_fast_cars():
        fast_cars = []

        car5 = Enemies('car2.png', [860, 565])
        car6 = Enemies('car2.png', [300, 565])
        car7 = Enemies('car3.png', [50, 520])
        car8 = Enemies('car3.png', [650, 520])
        car9 = Enemies('car2.png', [950, 425])
        car10 = Enemies('car2.png', [425, 425])

        fast_cars.append(car5)
        fast_cars.append(car6)
        fast_cars.append(car7)
        fast_cars.append(car8)
        fast_cars.append(car9)
        fast_cars.append(car10)

        # creating a sprite group out of slow cars for sprite collide fxn call
        fast_car_group = pg.sprite.Group(fast_cars)
        return fast_car_group

    # Initializes slow car enemies
    @staticmethod
    def init_slow_cars():
        slow_cars = []

        car1 = Enemies('car1.png', [100, 610])
        car2 = Enemies('car1.png', [450, 610])
        car3 = Enemies('car1.png', [0, 475])
        car4 = Enemies('car1.png', [600, 475])

        slow_cars.append(car1)
        slow_cars.append(car2)
        slow_cars.append(car3)
        slow_cars.append(car4)

        # creating a sprite group out of slow cars for sprite collide fxn call
        slow_car_group = pg.sprite.Group(slow_cars)
        return slow_car_group
