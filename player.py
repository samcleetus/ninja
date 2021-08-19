import pygame
from var import *
from world import World

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #animation stuff
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        #------
        temp_list = []
        for i in range(1):
            img = pygame.image.load(f"./assets/ninja/idle/{i}.png")
            img = pygame.transform.scale(img, (70, 64))
            img.set_colorkey(black)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f"./assets/ninja/run/{i}.png")
            img = pygame.transform.scale(img, (70, 64))
            img.set_colorkey(black)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(1):
            img = pygame.image.load(f"./assets/ninja/jump/{i}.png")
            img = pygame.transform.scale(img, (70, 64))
            img.set_colorkey(black)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        #------
        #the rest
        self.direction = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.alive = True
        self.vel_y = 0
        self.jumps = 2
        self.max_jumps = 2
        self.speed = 7
        self.flip = False
        self.in_air = False



    def attempt_jump(self):
        if self.jumps:
            self.jumps -= 1
            self.vel_y = -25
            self.in_air = True


    def move(self, moving_left, moving_right, world):
        global run
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        if self.rect.bottom > 1700:
            self.rect.bottom = 1700
            self.alive = False
            self.update_action(0)



        #collsions 'n shit
        for tile in world.tile_list:
            #collisions in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                if self.in_air == False:
                    self.update_action(0)

            #collision in the y direction    
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if below the ground
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                #check if above the ground
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.jumps = self.max_jumps
                    self.in_air = False



        #update positions
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        animation_cooldown = 100

        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        
    def draw(self):
        new_img = (pygame.transform.flip(self.image, self.flip, False))
        screen.blit(new_img, (self.rect.x - scroll[0], self.rect.y - scroll[1]))