#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Testing labyrinth loading and drawing from file "map.txt"
"""

import os
import pygame
from pygame.locals import*
import random

### DATA ###

#screen parameters
sprite_number_x = 15
sprite_number_y = 16
sprite_size = 32
screen_width = sprite_number_x * sprite_size
screen_height = sprite_number_y * sprite_size


#title
title = "Aidez McGyver à s'échapper"

#path to images
wall_image = 'brick_gray0.png'
floor_image = 'floor_sand_stone0.png'
mcgyver_image = 'macgyver32.png'
keeper_image = 'gardien32.png'
needle_image = 'needle0.png'
blowgun_image = 'blowgun1.png'
ether_image = 'brilliant_blue.png'
inventory_image ='unseen.png'
slot_image = 'slot.png'


### CLASSES ###

class Level():
    """Level creation"""

    def __init__(self,map):
        self.map = map
        self.map_frame = 0

    def load(self):
        """Load level from file 'map.txt'"""

        with open("map.txt", "r") as map:
            map_frame = []
            for line in map:
                map_line = []
                for char in line:
                    if char != '\n':
                        map_line.append(char)
                map_frame.append(map_line)
            self.frame = map_frame


    def draw(self, screen):

        wall = pygame.image.load(wall_image).convert()
        floor = pygame.image.load(floor_image).convert()
        inventory = pygame.image.load(inventory_image).convert()
        slot = pygame.image.load(slot_image).convert()

        n_line = 0
        for line in self.frame:
            n_tile = 0
            for sprite in line:
                x = n_tile * sprite_size
                y = n_line * sprite_size
                if sprite == 'X':
                    screen.blit(wall, (x,y))
                elif sprite == '_':
                    screen.blit(floor, (x,y))
                elif sprite == 'U':
                    screen.blit(inventory, (x,y))
                elif sprite == 'I':
                    screen.blit(slot, (x,y))
                n_tile += 1
            n_line += 1


class Sprite():
    """General class to manage sprites in the game"""

    def __init__(self, image, name, tile_y, tile_x, level):

        self.image = pygame.image.load(image).convert_alpha()
        self.name = ""
        self.tile_x = tile_x #actual x tile location
        self.tile_y = tile_y #actual y tile location
        self.x = tile_x * sprite_size #actual x location of sprite in pixels
        self.y = tile_y * sprite_size #actual y location of sprite in pixels
        self.level = level
        sprite_instances.append(self)


    def move(self, direction):
        """move sprite"""
        if direction == 'right':
            if self.tile_x < (sprite_number_x - 1):
                if self.level.frame[self.tile_y][self.tile_x + 1] != 'X':
                    if self.level.frame[self.tile_y][self.tile_x + 1] != 'I':
                        self.tile_x += 1
                        self.x = self.tile_x * sprite_size
        
        elif direction == 'left':
            if self.tile_x > 0:
                if self.level.frame[self.tile_y][self.tile_x - 1] != 'X':
                    if self.level.frame[self.tile_y][self.tile_x - 1] != 'I':   
                        self.tile_x -= 1
                        self.x = self.tile_x * sprite_size
            
        elif direction == 'up':
            if self.tile_y > 0:
                if self.level.frame[self.tile_y-1][self.tile_x] != 'X':
                    if self.level.frame[self.tile_y-1][self.tile_x] != 'I':
                        self.tile_y -= 1
                        self.y = self.tile_y * sprite_size

        elif direction == 'down':
            if self.tile_y < (sprite_number_y - 1):
                if self.level.frame[self.tile_y+1][self.tile_x] != 'X':
                    if self.level.frame[self.tile_y+1][self.tile_x] != 'I':
                        self.tile_y += 1
                        self.y = self.tile_y * sprite_size
    

    def spawn(self, tile_y, tile_x):
        """spawn a sprite and put an O symbol in level to prevent spawning other sprites
        on the same tile"""
        self.tile_y = tile_y
        self.tile_x = tile_x
        self.level.frame[self.tile_y][self.tile_x] == 'O'
        self.y = self.tile_y * sprite_size
        self.x = self.tile_x * sprite_size

    def rdm_spawn(self):
        """randomely spawn sprite avoiding walls 'X' and other spawned sprites 'O'"""
        spawned = False
        while not spawned:

            self.tile_y = random.randrange(1,14)
            self.tile_x = random.randrange(1,14)

            if self.level.frame[self.tile_y][self.tile_x] != 'X':
                if self.level.frame[self.tile_y][self.tile_x] != 'O': 

                    self.level.frame[self.tile_y][self.tile_x] == 'O'
                    self.y = self.tile_y * sprite_size
                    self.x = self.tile_x * sprite_size
                    spawned = True

    def pickup(self, slot_x):
        """Transfer item to inventory slot"""
        new_inventory.items_set.add(self.name)
        self.tile_y = 15
        self.tile_x = slot_x
        self.y = self.tile_y * sprite_size
        self.x = self.tile_x * sprite_size

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Inventory():
    """character inventory, items required to win the game against the boss"""
    def __init__(self):
        self.items_set = set([])



### MAIN ###

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("bookman", 24)

start = font.render("Aidez McGyver à s'échapper", True, (0, 0, 255))
manual = font.render("Trouvez un moyen de vous débarasser du gardien", True, (0, 0, 255))
win = font.render("\o/ McGyver s'est échappé \o/", True, (0, 255, 0))
loss = font.render("T_T McGyver s'est fait attraper T_T", True, (255, 0, 0))


pygame.display.set_caption(title)

screen.fill((0,0,0))

screen.blit(start,(screen_width // 2 - start.get_width() // 2, screen_height // 2 - start.get_height() // 2))
screen.blit(manual,(screen_width // 2 - manual.get_width() // 2, screen_height - manual.get_height()))

pygame.display.flip()

pygame.time.wait(3000)

running = True

new_level = Level(map)
new_level.load()
new_level.draw(screen)

new_inventory = Inventory()

sprite_instances = []
characters = []
items = []

player = Sprite(mcgyver_image, "player", 0, 0, new_level)
characters.append(player)
player.spawn(13,1)

keeper = Sprite(keeper_image, "keeper", 0, 0, new_level)
characters.append(keeper)
keeper.spawn(1,13)

needle = Sprite(needle_image, "needle", 0, 0, new_level)
items.append(needle)

blowgun = Sprite(blowgun_image, "blowgun", 0, 0, new_level)
items.append(blowgun)

ether = Sprite(ether_image, "ether", 0, 0, new_level)
items.append(ether)


for i in items:
    i.rdm_spawn()

while running:

    pygame.time.Clock().tick(10)

    new_level.draw(screen)

    for sprite in sprite_instances:
       sprite.draw()

    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move('left')
            elif event.key == K_UP:
                player.move('up')
            elif event.key == K_DOWN:
                player.move('down')
            elif event.key == K_RIGHT:
                player.move('right')
       

    if (player.tile_x, player.tile_y) == (needle.tile_x, needle.tile_y):
        needle.pickup(6)
        
    elif (player.tile_x, player.tile_y) == (blowgun.tile_x, blowgun.tile_y):
        blowgun.pickup(7)
       
    elif (player.tile_x, player.tile_y) == (ether.tile_x, ether.tile_y):
        ether.pickup(8)
        

    if (player.tile_x, player.tile_y) == (keeper.tile_x, keeper.tile_y):
        if new_inventory.items_set == ([blowgun.name,ether.name,needle.name]):

            screen.fill((0,0,0))

            screen.blit(win,(screen_width // 2 - win.get_width() // 2, screen_height // 2 - win.get_height() // 2))

            pygame.display.flip()

            pygame.time.wait(3000)

            running = False

        else:

            screen.fill((0,0,0))

            screen.blit(loss,(screen_width // 2 - loss.get_width() // 2, screen_height // 2 - loss.get_height() // 2))

            pygame.display.flip()

            pygame.time.wait(3000)

            running = False

