#!/usr/bin/env python
"""
tie2.py

draws a tie fighter in the upper corner of the screen with func
"""

import pygame
from pygame import draw
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
done = False

def draw_tie(surf, color):
    draw.rect(surf, color, (0,0,5,40))
    draw.rect(surf, color, (35,0,5,40))
    draw.rect(surf, color, (0,17,40,5))
    draw.circle(surf, color, (20,20), 10)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # draw tie fighter
    draw_tie(screen, (255,0,0))
    
    pygame.display.flip()

print "ByeBye"
