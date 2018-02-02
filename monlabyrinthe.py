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
inventory_image ='slot.png'

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

            
#    def draw(self):
#       """Draw the loaded level in console"""
#
#        i = 0
#        while i < len(self.frame):
#            print("|".join(self.frame[i]))
#            i += 1

    def draw(self, screen):

        wall = pygame.image.load(wall_image).convert()
        floor = pygame.image.load(floor_image).convert()
        inventory = pygame.image.load(inventory_image).convert()

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
                elif sprite == 'I':
                    screen.blit(inventory, (x,y))
                n_tile += 1
            n_line += 1


class Sprite():
    """General class to manage sprites in the game"""
    def __init__(self, image, tile_y, tile_x, level):
        self.image = pygame.image.load(image).convert_alpha()
        self.tile_x = tile_x #actual x tile location
        self.tile_y = tile_y #actual y tile location
        self.x = tile_x * sprite_size #actual x location of sprite in pixels
        self.y = tile_y * sprite_size #actual y location of sprite in pixels
        self.level = level

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


class Inventory():
    """character inventory, items required to win the game against the boss"""
    def __init__(self):
        self.items_set = set([])

    def pickup(self):    
        self.items_set.add()

    def draw(self):
        pass


### MAIN ###

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption(title)


game = 1

new_level = Level(map)
new_level.load()
new_level.draw(screen)

new_inventory = Inventory()
player = Sprite(mcgyver_image, 13, 1, new_level)
keeper = Sprite(keeper_image, 1, 13, new_level)
needle = Sprite(needle_image, random.randrange(2,13), random.randrange(2,13), new_level)
blowgun = Sprite(blowgun_image, random.randrange(2,13), random.randrange(2,13), new_level)
ether = Sprite(ether_image, random.randrange(2,13), random.randrange(2,13), new_level)

while game == 1:

    pygame.time.Clock().tick(10)
    new_level.draw(screen)
    screen.blit(player.image, (player.x, player.y))
    screen.blit(keeper.image, (keeper.x, keeper.y))
    screen.blit(needle.image, (needle.x, needle.y))
    screen.blit(blowgun.image, (blowgun.x, blowgun.y))
    screen.blit(ether.image, (ether.x, ether.y))
    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            game = 0
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move('left')
            elif event.key == K_UP:
                player.move('up')
            elif event.key == K_DOWN:
                player.move('down')
            elif event.key == K_RIGHT:
                player.move('right')
       

    if (player.x, player.y) == (needle.x, needle.y):
        new_inventory.items_set.add("needle")
        needle.tile_y = 15
        needle.tile_x = 2
        

    elif (player.x, player.y) == (blowgun.x, blowgun.y):
        new_inventory.items_set.add("blowgun")
        blowgun.tile_y = 15
        blowgun.tile_x = 4

    elif (player.x, player.y) == (ether.x, ether.y):
        new_inventory.items_set.add("ether")
        ether.tile_y = 15
        ether.tile_x = 6


    if (player.x, player.y) == (keeper.x, keeper.y):
        if new_inventory.items_set == {"needle", "blowgun", "ether"}:
            game = 0

