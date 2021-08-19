import pygame
import os


# -- colors
black = (0,0,0)
dark_blue = (15, 29, 43)
red = (255, 0, 0)
bg = (4, 21, 36)
blue = (0,0,255)
color_1 = (12, 24, 31)
color_2 = (21, 40, 27)
color_3 = (16, 29, 41)

# -- tile images
tile_1 = pygame.image.load("./assets/tiles/1.png")
#tile_1 = pygame.image.load(os.path.join((os.getcwd()), "./assets/tiles/1.png"))
tile_1.set_colorkey(black)
tile_2 = pygame.image.load("./assets/tiles/2.png")
tile_2.set_colorkey(black)
tile_3 = pygame.image.load("./assets/tiles/3.png")
tile_3.set_colorkey(black)
tile_4 = pygame.image.load("./assets/tiles/4.png")
tile_4.set_colorkey(black)
tile_5 = pygame.image.load("./assets/tiles/5.png")
tile_5.set_colorkey(black)
tile_6 = pygame.image.load("./assets/tiles/6.png")
tile_6.set_colorkey(black)
tile_7 = pygame.image.load("./assets/tiles/7.png")
tile_7.set_colorkey(black)
tile_8 = pygame.image.load("./assets/tiles/8.png")
tile_8.set_colorkey(black)
tile_9 = pygame.image.load("./assets/tiles/9.png")
tile_9.set_colorkey(black)


# -- images
#temple
temple_img = pygame.image.load("./assets/images/temple.png")
temple_img = pygame.transform.scale(temple_img, (930, 580))
temple_img.set_colorkey(black)
#moon
moon_img = pygame.image.load("./assets/images/moon.png")
moon_img = pygame.transform.scale(moon_img, (74, 72))
moon_img.set_colorkey(black)
#player
player_img = pygame.image.load("./assets/ninja/idle/0.png")
player_img = pygame.transform.scale(player_img, (70, 64))
player_img.set_colorkey(black)
#trees
img = pygame.image.load("./assets/images/tree_1.png")
tree_1 = pygame.transform.scale(img, (156, 164))
tree_1.set_colorkey(black)
img = pygame.image.load("./assets/images/tree_2.png")
tree_2 = pygame.transform.scale(img, (188, 138))
tree_2.set_colorkey(black)
img = pygame.image.load("./assets/images/tree_3.png")
tree_3 = pygame.transform.scale(img, (126, 136))
tree_3.set_colorkey(black)
#bushes
img = pygame.image.load("./assets/images/bush_1.png")
bush_1 = pygame.transform.scale(img, (102, 60))
bush_1.set_colorkey(black)
img = pygame.image.load("./assets/images/bush_2.png")
bush_2 = pygame.transform.scale(img, (128, 74))
bush_2.set_colorkey(black)
#crystals
img = pygame.image.load("./assets/images/crystal_1.png")
crystal_1 = pygame.transform.scale(img, (62, 54))
crystal_1.set_colorkey(black)
img = pygame.image.load("./assets/images/crystal_2.png")
crystal_2 = pygame.transform.scale(img, (42, 76))
crystal_2.set_colorkey(black)
img = pygame.image.load("./assets/images/crystal_3.png")
crystal_3 = pygame.transform.scale(img, (62, 54))
crystal_3.set_colorkey(black)
#rocks
img = pygame.image.load("./assets/images/rock_1.png")
rock_1 = pygame.transform.scale(img, (62, 32))
rock_1.set_colorkey(black)
img = pygame.image.load("./assets/images/rock_2.png")
rock_2 = pygame.transform.scale(img, (64, 32))
rock_2.set_colorkey(black)
img = pygame.image.load("./assets/images/rock_3.png")
rock_3 = pygame.transform.scale(img, (74, 32))
rock_3.set_colorkey(black)
img = pygame.image.load("./assets/images/rock_4.png")
rock_4 = pygame.transform.scale(img, (42, 18))
rock_4.set_colorkey(black)


# -- variables
run = True
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = 60
TILE_SIZE = 50
moving_left = False
moving_right = False
scroll = [0, 0]
icon = pygame.image.load("./assets/ninja/idle/0.png")