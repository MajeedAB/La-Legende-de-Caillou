import pygame
from Caillou import Caillou
from Image import load_image
from LevelAssets import get_tile_sprites
from constants import TILE_SIZE


NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

PHYSICS_TILES = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

class Plateforme:

    def __init__(self, game, tile_size=TILE_SIZE):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []
        self.tile_images = get_tile_sprites()

        # for i in range(10):
        #     self.tilemap[str(3 + i) + ';10'] = {'type': 'var1', 'variant': 1, 'pos': (3 + i, 10)}
        #     self.tilemap['10;' + str(5 + i)] = {'type': 'var2', 'variant': 1, 'pos': (10, 5 + i)}
        # print("self.tilemap:", self.tilemap)
    

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects


    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(pygame.transform.scale(self.tile_images[0], (self.tile_size, self.tile_size)), (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            # if tile['type'] == 'var1':
            #     tile_idx = tile['type']
            # if tile['type'] == 'var2':
            #     tile_idx = 1
            # if tile['type'] == 'var3':
            #     tile_idx = 2
            surf.blit(pygame.transform.scale(self.tile_images[tile['type']], (self.tile_size, self.tile_size)), (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size- offset[1]))

