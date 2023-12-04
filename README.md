# cis343-project4-pygame

Simple game in Python. Objective of the game is for the player to collect all 7 stars. In order to get to the stars, player must cross in front of cars without getting hit, and cross a river on logs and turtles. The player will have 3 lives in order to achieve this. As an added feature, the player gets to choose what animal to play as (a cat, dog, or bird).

Player class implements all logic for the player (points). It inherits from the Units class.

Enemies class implements all logic for the enemies (cars). It inherits from the Units class.

Utilities class implements logic for objects player needs to use to win (stars, logs, turtles). It also inherits fron the Units class.

Units class implements all common logic between player, enemies, and utilities (moving, drawing, etc).

Game class includes initial set up of the game and our main defintion.

ASSETS

Log image: https://openclipart.org/detail/218084/pixel-log-side
- Asset has no copyright under CC0 1.0 Universal

Below images (turtle, cat, dog, and bird) are all sourced from Pixilart.com, which states here (https://www.pixilart.com/terms) has no copyrighting on the art unless otherwise stated. All of the below images did not have an additional copyright statement.

Turtle image: https://www.pixilart.com/tuekeleven

Cat image: https://www.pixilart.com/art/32-x-32-cat-42e019c236fe77a

Dog image: https://www.pixilart.com/art/free-profile-picture-sr2ecb018a49aaws3?ft=tags&ft_id=

Bird image: https://www.pixilart.com/art/pelicano-sr2b8864418e2db?ft=tags&ft_id=

Star image: Hand drawn by Kate

Red Car image: https://www.pngwing.com/en/free-png-noukg
- listed available for non-commercial use 

Blue car image: https://www.pngwing.com/en/free-png-zvoaf
- listed available for non-commercial use

Green car image: https://www.pngwing.com/en/free-png-nnnka
- listed available for non-commercial use

Background image: https://imgur.com/gallery/vEccR
- according to https://imgur.com/tos we have the right to use images from the site for personal use

Font: https://fonts.google.com/specimen/Potta+One
- license listed uner SIL Open Font License, Version 1.1


