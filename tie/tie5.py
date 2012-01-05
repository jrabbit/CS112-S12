#!/usr/bin/env python
"""
tie5.py

draws a tie where ya click! can change the size and color
"""

import pygame
from pygame import draw
from pygame.locals import *

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    wall = size/8
    x0,x1 = x - (size/2), x + (size/2)
    y0,y1 = y - (size/2), y + (size/2)

    draw.rect(surf, color, (x0, y0, wall, size))
    draw.rect(surf, color, (x1-wall, y0, wall, size))
    draw.rect(surf, color, (x0, y-(wall/2), size, wall))
    draw.circle(surf, color, (x, y), size/4)

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
        elif event.type == MOUSEBUTTONDOWN:
            draw_tie(screen, pygame.mouse.get_pos(), size=80)
    
    pygame.display.flip()

print "ByeBye"
