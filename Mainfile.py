

__author__ = 'Rick Vink'

# General addons
import pygame # import pygame
import time # import time
import random # import random
import collections  # Make collections
pygame.init()
#gc.collect()

# Game addons
import functions
import update_background
import initiate_units
import update_unit_location
import events
import background_list
import game_list


# Make game
game = game_list.Game()   # Object with all the parameters of the game

# Game window
gameDisplay = pygame.display.set_mode((game.display_size[0],game.display_size[1]))


# Map background
def map_background(game):
    colour = (255,255,255)
    pygame.draw.rect(gameDisplay, colour, [game.map_off[0], game.map_off[1], game.map_size[0], game.map_size[1]])


def game_loop():

    # Clock
    clock = pygame.time.Clock()

    # Set Exit state
    gameExit = False

    map_background(game) # Temperary function

    # Initiate background object
    background = background_list.background()        # Object with all the parameters of the background
    update_background.initiate(gameDisplay,game,background)  # Create field

    # Make units
    units = initiate_units.run(game)        # Create units

    # While loop
    while not gameExit:

        update_background.generate_map(gameDisplay,game,background)
        events.move_units(game,units)
        update_unit_location.run(gameDisplay,game,units)

        # Get input(s)
        for event in pygame.event.get():

            events.process_input(event,units,game)

        # Update clock (60 frames per second)
        clock.tick(60)

game_loop()




