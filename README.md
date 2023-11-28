# cis343-project4-pygame

Simple Frogger implementation in Python. This only implements the first level of Frogger (i.e frogger does not get new enemies if he completes a level).
Froggers goal in this version is to collect all 7 flies. He has 3 lives to try and achieve this. 
Specifics of Frogger removed from this version:
-Turtles do not sink, and therefor will not be considered an enemy
-Flies do not appear randomly but instead exist constantly unless frogger collects it

Player class implements all logic for Frogger. It inherits from the Units class.

Enemies class implements all logic for the enemies (cars). It inherits from the Units class.

Utilities class implements logic for objects frogger needs to use to win (flies, logs, turtles). It also inherits fron the Units class.

Units class implements all common logic between Frogger, enemies, and utilities (moving, drawing, etc).

Game class includes initial set up of the game and our main defintion.



