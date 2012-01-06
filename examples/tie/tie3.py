#!/usr/bin/env python
"""
tie3.py

draws a tie anywhere
"""

import pygame
from pygame import draw
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((0,0,0))
done = False

def draw_tie(surf, color, pos):
    x,y = pos
    draw.rect(surf, color, (x,y,5,40))
    draw.rect(surf, color, (x+35,y,5,40))
    draw.rect(surf, color, (x,y+17,40,5))
    draw.circle(surf, color, (x+20,y+20), 10)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    # draw tie fighter
    draw_tie(screen, (255,0,0), (20, 200))
    draw_tie(screen, (255,128,255), (0, 0))
    draw_tie(screen, (255,255,0), (300, 400))
    
    pygame.display.flip()

print "ByeBye"
