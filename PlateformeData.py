
import math

from constants import TILE_SIZE

TILE_OFFSET_X = -10
TILE_OFFSET_Y = -8

def set_tiles_data_level(game, level):
    if(level == 1):
        set_tiles_1(game)
    if(level == 2):
        set_tiles_2(game)

def add_line(tile_list, start, end):
    for i in range(start[0], end[0]):
        j = math.floor(start[1] + (end[1] - start[1]) * (i / (end[0] - start[0])))
        tile_list.append((i, j))

def add_rect(tile_list, top_left, bot_right):
    for i in range(top_left[0], bot_right[0]):
        for j in range(top_left[1], bot_right[1]):
            tile_list.append((i, j))

def set_tiles_1(game):
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
    tile_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0 ],
        [0, 0, -1, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0 ],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],
    ]
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


def set_tiles_2(tilemap):
    for i in range(10):
        pass
        # tilemap[str(3 + i) + ';10'] = {'type': 'var1', 'variant': 1, 'pos': (3 + i, 10)}
        # tilemap['10;' + str(5 + i)] = {'type': 'var2', 'variant': 1, 'pos': (10, 5 + i)}
