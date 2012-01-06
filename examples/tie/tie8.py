#!/usr/bin/env python
"""
tie8.py

tie fighters now shrink
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
            size = 80
            ties.append([pos,color,size])

    # update
    # not crazy about this, but list comps are complicated
    for i in range(len(ties)-1, -1, -1):
        tie = ties[i]
        tie[2] -= 2
        if tie[2] <= 0:
            ties.pop(i)

    # draw
    screen.fill((0,0,0))
    for pos,color,size in ties:
        draw_tie(screen, pos, color, size)

    pygame.display.flip()
    pygame.time.wait(50)

print "ByeBye"
