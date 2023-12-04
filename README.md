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


ASSETS
Fly image: https://tcrf.net/File:Frogger1997-june2psx-PinkFly.png#filehistory
- changes to image: image downsized to 48 x 35 pixels with background removed
- Assest available under Atribution 3.0 Unported

Log image: https://openclipart.org/detail/218084/pixel-log-side
- Asset has no copyright under CC0 1.0 Universal

Frog image: https://www.vhv.rs/viewpic/TTJwmmm_8-bit-frog-frogger-hd-png-download/
- Asset available for personal use only (which this is)

Turtle image: https://www.pixilart.com/tuekeleven
- Asset has no copyright according to https://www.pixilart.com/terms

Red Car image:

Blue car image:

Pink car image:

Background image:

Font:


