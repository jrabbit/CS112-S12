#!/usr/bin/env python
"""
tie1.py
draws a tie fighter in the upper corner of the screen
"""

import pygame
from pygame import draw
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True


    # draw tie fighter
    draw.rect(screen, (255,0,0), (0,0,5,40))
    draw.rect(screen, (255,0,0), (35,0,5,40))
    draw.rect(screen, (255,0,0), (0,17,40,5))
    draw.circle(screen, (255,0,0), (20,20), 10)
    
    pygame.display.flip()

print "ByeBye"
