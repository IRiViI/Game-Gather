__author__ = 'rckvn'

def test():
    print('test zz')

def game_coordinates(game,s,height):
    # Converts from pixel location to grid location
    # Input the game list, the list s and the height; example: grid_size(game,[10,20],3)

    sn = [None,None]

    sn[0] = s[0] - game.map_off[0]
    sn[1] = game.display_size[1] - s[1] - game.map_off[1] + height

    return sn

def display_coordinates(game,s,height):
    # Converts from grid location to pixel location
    # Input the game list, the list s and the height; example: grid_size(game,[10,20],3)

    sn = [None,None]

    sn[0] = s[0] + game.map_off[0]
    sn[1] = game.display_size[1] - s[1] - game.map_off[1] - height

    return sn

def grid_size(game,s):
    # Converts from pixel size to coordinate size
    # Input the game list and the list s example: grid_size(game,[10,20])

    sn = [None,None]

    sn[0] = s[0] * game.grid_size[0]
    sn[1] = s[1] * game.grid_size[1]

    return sn