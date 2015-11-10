__author__ = 'rckvn'

import pygame # import pygame
import time # import time
import random # import random
import functions

pygame.init()

def generate_map(gameDisplay,game,background):
        # Generate the map

        for x in range(0,game.number_tilesX):

            for y in range(0,game.number_tilesY):

                # Location of tile
                s = functions.display_coordinates(game,[x*game.tile_size[0],y*game.tile_size[1]],background.size[1])

                if background.tilemap_layout[y][x] == 1:
                    # Lay grass tile
                    gameDisplay.blit(background.tile_1,s)

                elif background.tilemap_layout[y][x] == 0:
                    # Lay rock tile
                    gameDisplay.blit(background.tile_2,s)

def initiate(gameDisplay,game,background):

    # Tills have a length and width according to game.tile_width and game.tile_height
    # Add Tile image 1
    tileImg1 = pygame.image.load('Images/tile_Image_1.jpg')
    tileImg1 = pygame.transform.scale(tileImg1,(game.tile_size[0],game.tile_size[1]))

    # x and y offset
    x0 = game.map_off[0]
    y0 = game.map_off[1]

    def tilemap():
        # Create the matrix that holds the locations of the tiles

        tilemap_layout = [
            [0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0],
            [0,1,1,1,1,1,0],
            [0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0]
        ]

        return tilemap_layout

    def main():

        # Set window title
        pygame.display.set_caption(game.nameGame)

        # Generate the layout of the till map
        background.tilemap_layout = tilemap()

        # Generate map
        generate_map(gameDisplay,game,background)

        # Update display
        pygame.display.update() # Alternative: pygame.display.flip()

    main()