import pygame


# -- colors
black = (0,0,0)
dark_blue = (15, 29, 43)
red = (255, 0, 0)
bg = (4, 21, 36)
blue = (0,0,255)

# -- tile images
tile_1 = pygame.image.load("./assets/tiles/1.png")
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
player_img = pygame.image.load("./ninja/idle/0.png")
player_img = pygame.transform.scale(player_img, (70, 64))
player_img.set_colorkey(black)

# -- variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = 60
TILE_SIZE = 50
moving_left = False
moving_right = False
scroll = [0, 0]