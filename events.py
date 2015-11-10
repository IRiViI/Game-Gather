__author__ = 'rckvn'

import pygame # import pygame
import time # import time
import random # import random
import collections

# My functions
import functions

pygame.init()



def move(self,step,units):
    # Move to destination

    if self.location[0] < self.destination[0]:
        self.location[0] += step
    elif self.location[0] > self.destination[0]:
        self.location[0] -= step

    if self.location[1] < self.destination[1]:
        self.location[1] += step
    elif self.location[1] > self.destination[1]:
        self.location[1] -= step

def select_action(pos,units,game):

    # Fields
    fields = list(units._fields)    # Read fields
    num_fields = len(fields)        # Number of fields

    # Make list
    selects = []

    # For every object
    for i in range(num_fields):
        area = units[i].area    # Get the area of the unit
        num_grids = len(area)   # Get the number of girds used by the unit

        check_unit = True
        j = 0

        while check_unit:
            s = [area[j][0],area[j][1]]     # grid location

            if pos == s:
                selects.append(fields[i])   # Add name to select list
                check_unit = False          # Stop checking when a match is found

            j += 1

            if j == num_grids:
                check_unit = False          # Stop checking when all grids are checked

    return selects

def redirect_unit(units,game):
    # Action upon pushing right mouse button

    # Fields
    fields_left = list(game.selected)       # Selected units
    num_fields_left = len(fields_left)      # Number of selected units

    fields_right = list(game.selected)       # Selected units
    num_fields_right = len(fields_left)      # Number of selected units

    # Make list
    selects = []

    # For every object
    for i in range(num_fields):
        area = units[i].area    # Get the area of the unit
        num_grids = len(area)   # Get the number of girds used by the unit

def update_area(self,grid_size):
# Check which tiles are occupied by the object

    self.area = [[None for i in range(2)] for i in range(16)]

    check_area = True
    i = 0
    while check_area == True:

        x = int(self.location[0]/10)*10

        #range(self.location[0],10,self.location[0] + self.size[0])
        while x < self.location[0] + self.size[0]:
            y = int(self.location[1]/10)*10

            while y < self.location[1] + self.size[1]:

                self.area[i][0] = x
                self.area[i][1] = y

                i += 1
                y += grid_size[1]

            x += grid_size[0]

        check_area = False

def move_units(game,units):
    # Order units to move

    move(units.unit1,game.inter_step,units)
    update_area(units.unit1,game.grid_size)

    move(units.unit2,game.inter_step,units)
    update_area(units.unit2,game.grid_size)


def refresh_background():
    # Refresh the background
    1

def process_input(event,units,game):
    # Process inputs by keyboard and mouse

    # If the window is closed
    if event.type == pygame.QUIT:

        # Quite
        pygame.quit()
        quit()

    # Click with mouse
    if event.type == pygame.MOUSEBUTTONUP:

        # Get mouse position upon clicking
        s = list(pygame.mouse.get_pos())            # Get position of mouse

        pos = functions.game_coordinates(game,s,0)  # Convert to location on map


        # Get the location on the grid
        pos_grid = [None,None]
        pos_grid[0] = int(pos[0]/10)*10
        pos_grid[1] = int(pos[1]/10)*10

        # Act upon clicking
        selected = select_action(pos_grid,units,game)

        # Act upon type mouse button
        if event.button == 1:   # Select with left mouse button
            game.selected = selected
        elif event.button == 3: # Select with right mouse button
            game.right_select = selected
            redirect_unit(units,game)


