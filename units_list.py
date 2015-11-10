__author__ = 'rckvn'

import pygame # import pygame
import numpy as np # unused
pygame.init()


# Figures of units
# Unit 1
foot = pygame.image.load('Images/voetbal.png')

# Unit 2
bask = pygame.image.load('Images/Basketball.png')

class Unit1:
    life = 10
    speed = 10
    size = [30,30]
    tile_area = 9
    destination = [None]*2
    location = [None]*2
    area = [[None for i in range(2)] for i in range(16)]
    image = pygame.transform.scale(foot,size)


class Unit2:
    life = 10
    speed = 10
    size = [30,30]
    destination = [None]*2
    location = [None]*2
    area = [[None for i in range(2)] for i in range(16)]
    image = pygame.transform.scale(bask,size)


