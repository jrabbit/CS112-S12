#!/usr/bin/env python

from random import randrange

from time import sleep

import pygame

# initialize pygame
pygame.init()

# make a screen
screen = pygame.display.set_mode((640, 480))

while True:
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    color = (r,g,b)

    screen.fill(color)
    pygame.display.flip()

    sleep(1)
