
from Image import load_image

def get_level_background(level):
    return load_image('bg/level' + str(level) + '.png')

def get_treasure_sprite(level):
    return load_image('treasures/treasure' + str(level) + '.png')

caillou_start_pos = [
    (250, 200),
    (400, 200),
    (700, 350),
    (700, 350)
]

def get_caillou_start_pos(level):
    return caillou_start_pos[level-1]

treasure_coords = [
    [500, 500],
    [500, 600],
    [300, 700],
    [500, 700]
]

def get_treasure_coords(level):
    return treasure_coords[level-1]