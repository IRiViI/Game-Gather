__author__ = 'rckvn'

# General addons
import pygame # import pygame
pygame.init()
#gc.collect()
import collections  # Make collections

# Game addons
import functions

def units(game,units):

    # Figures of units
    # Unit 1
    foot = pygame.image.load('Images/voetbal.png')
    (xt,yt) = functions.grid_size(game,[units.unit1.height,units.unit1.width])
    foot = pygame.transform.scale(foot,(xt,yt))

    # Unit 2
    bask = pygame.image.load('Images/Basketball.png')
    (xt,yt) = functions.grid_size(game,[units.unit2.height,units.unit2.width])
    bask = pygame.transform.scale(bask,(xt,yt))

    return(foot,bask)