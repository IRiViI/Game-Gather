__author__ = 'rckvn'

import pygame # import pygame
pygame.init()

# Figures of units
# Tile 1
tile_1 = pygame.image.load('Images/tile_Image_1.jpg')

# Tile 2
tile_2 = pygame.image.load('Images/tile_Image_2.jpg')

class background():

    size = [100,100]

    tilemap_layout = []

    tile_1 = pygame.transform.scale(tile_1,size)
    tile_2 = pygame.transform.scale(tile_2,size)
