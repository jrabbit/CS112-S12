#!/usr/bin/env python
"""
tie7.py

draws a list of ties and adds new ones on click
"""
from random import randrange

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
ties = []
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            color = (randrange(100,256), randrange(100,256), randrange(100,256))
            size = randrange(30,80)
            ties.append((pos,color,size))

    # draw
    screen.fill((0,0,0))
    for tie in ties:
        pos,color,size = tie
        draw_tie(screen, pos, color, size)

    pygame.display.flip()

print "ByeBye"
