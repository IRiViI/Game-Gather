__author__ = 'rckvn'

import pygame # import pygame
pygame.init()

class Game(object):

     # ---- Editable ----

    nameGame = 'Resource Wars'  # Game name

    # Define width and height display
    display_size = [800,600]

    # Define width map
    map_size = [700,500]

    # Define location of map
    map_off = [50,50]

    # Define number of tiles
    number_tilesX = 7            # Number of tiles x
    number_tilesY = 5            # Number of tiles y

    # Grids per tile
    grid = 10

    # Intermediate steps
    inter_step = 1

    # ---- Not editable ----

    # Initialize tilmapLayout
    tilemap_layout = []  #

    # Tile sizes
    tile_size = [int(map_size[0] / number_tilesX),int(map_size[1] / number_tilesY)]

    # Grid sizes
    grid_size = [int(tile_size[0]/grid),int(tile_size[1]/grid)]

    # Selected objects
    selected = []

    # Selected objects right mouse button
    right_select = []