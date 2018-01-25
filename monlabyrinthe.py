#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Testing labyrinth loading and drawing from file "map.txt"
"""

import os
from pynput import keyboard


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
            
    def draw(self):
        """Draw the loaded level in console"""

        i = 0
        while i < len(self.frame):
            print("|".join(self.frame[i]))
            i += 1 


class Character():
    """Creates character"""

    def __init__(self):
        self.avatar = "A"
        self.inventory = {}
        self.y = 0
        self.x = 0


    def spawn(self):
        """spawn character at starting position"""
        self.start_x = 1
        self.start_y = 13
        new_level.frame[self.start_y + self.y][self.start_x + self.x] = self.avatar


    def on_press(key):
        """listen keyboard input to set character direction"""
        try:
            k = key.char 
        except:
            k = key.name
        if key == keyboard.Key.esc:
            return False
        elif k == 'left':
            self.x -= 1
        elif k == 'top':
            self.y += 1
        elif k == 'bottom':
            self.y -= 1
        elif k == 'right':
            self.x += 1

    def pickup(self):


    #def move(self):
        """moves character from keyboard input"""
        

        
    
    

#direction = 0
new_level = Level(map)

new_level.load()
new_level.draw()

new_character = Character()
new_character.spawn()

new_level.draw()

#Move Character
#print("Commandes : \n j = GAUCHE | i = HAUT | k = BAS | l = DROITE | q = QUITTER")
#
#keyboard_press = input()
#
#if keyboard == "j":
#    print("GAUCHE")
#elif keyboard == "i":
#    print("HAUT")
#elif keyboard == "k":
#    print("BAS")
#elif keyboard == "l":
#    print("DROITE")
#elif keyboard == "q":
#    continue_game = 0
#else:
#    print("Utilisez les touches jikl pour vous déplacer et q pour quitter")

os.system("pause")