#!/usr/bin/env python

from random import randint

from time import sleep

import pygame
from pygame import draw

# initialize pygame
pygame.init()

# make a screen
screen = pygame.display.set_mode((640, 480))

while True:
    event = pygame.event.poll()
    
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)

    screen.fill(color)
    pygame.display.flip()

    sleep(1)
