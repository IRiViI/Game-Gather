__author__ = 'rckvn'

import pygame # import pygame
import time # import time
import random # import random
import collections

pygame.init()

# Game addons
import units_list

def run(game):

    def main():

        Units = collections.namedtuple('Point',['unit1','unit2'])

        unit1 = units_list.Unit1()
        unit1.location = [100,200]
        unit1.destination = [400,400]

        unit2 = units_list.Unit2()
        unit2.location = [100,100]
        unit2.destination = [500,400]

        units = Units(unit1,unit2)

        return(units)

    units = main()

    return(units)


