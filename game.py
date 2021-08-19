import pygame
from pygame.constants import DROPTEXT, KEYDOWN, K_SPACE, K_UP, K_w
from var import *
from player import Player
from world import World
from map import world_list


pygame.init() 
clock = pygame.time.Clock()

pygame.display.set_caption('Ninja')
pygame.display.set_icon(icon)


world = World(world_list)
player = Player(100, 540)


while run:
    clock.tick(fps)

    # -- scrolling/camera movement
    scroll[0] += (player.rect.x - scroll[0] - 470)/20
    scroll[1] += (player.rect.y - scroll[1] - 320)/20

    # -- blitting decorations 'n shit
    screen.fill(color_3)
    screen.blit(moon_img, (1500 - int(scroll[0]), -300 - int(scroll[1])))

    screen.blit(tree_1, (1200 - int(scroll[0]), 800 - int(scroll[1])))
    screen.blit(tree_3, (610 - int(scroll[0]), 570 - int(scroll[1])))
    screen.blit(tree_2, (1320 - int(scroll[0]), 500 - int(scroll[1])))
    screen.blit(bush_1, (1390 - int(scroll[0]), 610 - int(scroll[1])))
    screen.blit(rock_4, (1210 - int(scroll[0]), 935 - int(scroll[1])))

    world.draw()


    player.update_animation()
    player.draw()

    # -- update player actions
    if player.alive:
        if player.in_air == True:
            player.update_action(2)
        elif moving_left or moving_right:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(moving_left, moving_right, world)


    # -- controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
               player.attempt_jump()
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False


    pygame.display.update()