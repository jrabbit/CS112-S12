#!/usr/bin/env python
"""
draw3.py

draw lines with step, multiple lines
"""
import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400,400))
done = False
bg = (0,0,0)
fg = (255,0,0)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

        # draw
        screen.fill(bg)

        for i in range(0,400,8):
            pygame.draw.line(screen, fg, (0,i), (i,399))
            pygame.draw.line(screen, fg, (0,i), (399-i,0))
            pygame.draw.line(screen, fg, (i,0), (399,i))
            pygame.draw.line(screen, fg, (i,399), (399,399-i))

        # refresh
        pygame.display.flip()
        
print "ByeBye"
