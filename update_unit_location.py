__author__ = 'rckvn'

import pygame # import pygame
import time # import time
import random # import random
import collections

# My functions
import functions

pygame.init()


def run(gameDisplay,game,units):

    # x and y offset
    x0 = game.map_off[0]
    y0 = game.map_off[1]

    # Tester
    def tester(x,y):
        colour = (0,255,255)
        pygame.draw.rect(gameDisplay, colour, [50+x, 50+y, 10, 10])

    def main():
        # unit 1
        (x,y) = functions.display_coordinates(game,units.unit1.location,units.unit1.size[1]) # Calculate location in pixels
        gameDisplay.blit(units.unit1.image,(x,y))

        # unit 2
        (x,y) = functions.display_coordinates(game,units.unit2.location,units.unit2.size[1]) # Calculate location in pixels
        gameDisplay.blit(units.unit2.image,(x,y))

        # Update display
        pygame.display.update() # Alternative: pygame.display.flip()

    main()