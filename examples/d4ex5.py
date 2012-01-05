#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((640,480))

done = False
while not done:
    event = pygame.event.poll()

    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        Done = True
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse %d,%d" % pygame.mouse.get_pos()

print "ByeBye"
