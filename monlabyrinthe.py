#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Testing labyrinth loading and drawing from file "map.txt"
"""

import os

class Level:
    def __init__(self, map):
    	self.map = map
    	self.frame = 0

def load(self):

#if os.path.exists(map):
    with open(self.map, "r") as map:
    	map_frame = []
    	for line in map:
    		map_line = []
    		for char in line:
    			if char != '\n':
    			    map_line.append(char)
    		map_frame.append(map_line)
    	self.frame = map_frame
    	print("OK")

new_level = Level()
new_level.load(frame)


print("pass")


#def draw(self):

    #print(map_frame)
    #print(map_frame[0][0])
    #print('au moins ca ca marche')

#Draw()

os.system("pause")