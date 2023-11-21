
from Image import load_image

def get_level_background(level):
    return load_image('bg/level' + str(level) + '.png')

def get_treasure_sprite(level):
    return load_image('treasures/treasure' + str(level) + '.png')

def get_tile_sprites():
    return [
        load_image('platforms/p0.png'),
        load_image('platforms/p1.png'),
        load_image('platforms/p2.png'),
        load_image('platforms/p3.png'),
        load_image('platforms/p4.png'),
        load_image('platforms/p5.png'),
        # load_image('platforms/p6.png'),
        # load_image('platforms/p7.png'),
        # load_image('platforms/p8.png'),
        # load_image('platforms/p9.png'),
        # load_image('platforms/p10.png'),
        # load_image('platforms/p11.png'),
        # load_image('platforms/p12.png'),
        ]

caillou_start_pos = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0)
]

def get_caillou_start_pos(level):
    return caillou_start_pos[level-1]

treasure_coords = [
    [250, 150],
    [100, 100],
    [100, 100],
    [100, 100]
]

def get_treasure_coords(level):
    return treasure_coords[level-1]