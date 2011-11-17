#!/usr/bin/env python
"""

Currently does not work
"""


from random import randrange

import pygame
from pygame import draw
from pygame.time import Clock
from pygame.locals import *

# GLOBALS
SCREEN_SIZE = SCREEN_W, SCREEN_H = 640, 480

# initialize pygame
pygame.init()

# make a screen
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = Clock()
running = True

# set initial color
screen.fill((255,0,0))
pygame.display.flip()

# while running
while running:
    while pygame.event.peek([KEYDOWN, QUIT, MOUSEBUTTONDOWN]):
        event = pygame.event.poll()
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            r = randrange(256)
            g = randrange(256)
            b = randrange(256)
            screen.fill((r,g,b))
            pygame.display.flip()

print "quitting"
