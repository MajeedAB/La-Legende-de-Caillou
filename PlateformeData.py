
import math

from constants import TILE_SIZE

TILE_OFFSET_X = -10
TILE_OFFSET_Y = -8

tile_matrix_1 = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 3, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 3, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0 ],
    [3, 0, -1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ],
    [3, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0 ],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
]

tile_matrix_2 = [
    [3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3 ],
    [3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3 ],
    [3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3 ],
    [3, 3, 3, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 3, 3, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 1, 0, 1, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 1, 1, 1, 1, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 3 ],
    [3, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, -2, 0, 3 ],
    [3, 0, -1, 0, 0, 1, 0, 1, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0 ],
]

tile_matrix_3 = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3 ],
    [0, 0, 3, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0 ],
    [0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0 ],
    [3, 3, 3, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3 ],
    [5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5 ],
    [5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5 ],
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5 ],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ],
]

tile_matrix_4 = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, -2, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
]

tile_matrix_list = [tile_matrix_1, tile_matrix_2, tile_matrix_3, tile_matrix_4]

def set_tiles_data_level(game, level):
    set_tiles(game, tile_matrix_list[level-1])

def add_line(tile_list, start, end):
    for i in range(start[0], end[0]):
        j = math.floor(start[1] + (end[1] - start[1]) * (i / (end[0] - start[0])))
        tile_list.append((i, j))

def add_rect(tile_list, top_left, bot_right):
    for i in range(top_left[0], bot_right[0]):
        for j in range(top_left[1], bot_right[1]):
            tile_list.append((i, j))

def set_tiles(game, tile_matrix):
    game.plateforme.tilemap = {}
    tile_list = []
    # add_line(tile_list, (-5, 1), (2, 5))
    # add_line(tile_list, (-5, 0), (-4, 0))
    # add_line(tile_list, (-5, -1), (-4, -1))
    # add_line(tile_list, (-5, -2), (-4, -2))
    # add_line(tile_list, (2, 5), (8, 2))
    # add_line(tile_list, (-5, 3), (-10, 2))
    # add_rect(tile_list, (-5, 3), (8, 10))
    game.treasure_coords[0] = 15
    game.treasure_coords[1] = -20
    
    for i,l in enumerate(tile_matrix):
        for j,el in enumerate(l):
            if(el == 0):
                continue
            elif(el == -2):
                game.treasure_coords[0] = (j + TILE_OFFSET_X) * TILE_SIZE
                game.treasure_coords[1] = (i + TILE_OFFSET_Y) * TILE_SIZE
                continue
            elif(el == -1):
                game.player.pos[0] = (j + TILE_OFFSET_X) * TILE_SIZE
                game.player.pos[1] = (i + TILE_OFFSET_Y) * TILE_SIZE
                continue
            key = str(j + TILE_OFFSET_X) + ';' + str(i + TILE_OFFSET_Y)
            variant = el-1
            game.plateforme.tilemap[key] = {'type': variant, 'variant': 1, 'pos': (j + TILE_OFFSET_X, i + TILE_OFFSET_Y)}