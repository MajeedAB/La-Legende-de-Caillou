import sys
import time
import pygame
from Caillou import Caillou
from LevelAssets import get_caillou_start_pos, get_level_background, get_tile_sprites, get_treasure_coords, get_treasure_sprite
from Plateforme import Plateforme
from Image import load_image
from PlateformeData import set_tiles_data_level
from constants import BG_IMG_SCALE, GAME_HZ

DFLT_IMG_SZ = (1200, 860)
class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('La Legende de Caillou')

        self.level = 1
        self.screen = pygame.display.set_mode(DFLT_IMG_SZ)

        self.display = pygame.Surface(DFLT_IMG_SZ)

        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        self.player = Caillou(get_caillou_start_pos(self.level), (40, 75), self)
        self.scroll = [self.player.rect().centerx - self.display.get_width() / 2, self.player.rect().centery - self.display.get_height() / 2]
        self.plateforme = Plateforme(self)
        set_tiles_data_level(self, self.level)

        self.treasure_found = False
        # self.treasure_coords = get_treasure_coords(self.level)
        self.treasure_sprite = get_treasure_sprite(self.level)
        self.treasure_size = (40, 60)

        self.bg_image = get_level_background(self.level).convert()
        self.bg_image.set_colorkey((1, 2, 3))


    def next_level(self):
        # Do cutscene / level switch logic
        self.level += 1
        self.treasure_found = False
        self.treasure_sprite = get_treasure_sprite(self.level)
        # self.treasure_coords[0] = get_treasure_coords(self.level)[0]
        # self.treasure_coords[1] = get_treasure_coords(self.level)[1]
        # self.player.pos[0] = get_caillou_start_pos(self.level)[0]
        # self.player.pos[1] = get_caillou_start_pos(self.level)[1]
        self.scroll = [self.player.rect().centerx - self.display.get_width() / 2, self.player.rect().centery - self.display.get_height() / 2]
        self.render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
        self.player.velocity[0] = 0
        self.player.velocity[1] = 0
        self.clock.tick(1)

        self.bg_image = get_level_background(self.level).convert()
        self.bg_image.set_colorkey((1, 2, 3))

        set_tiles_data_level(self, self.level)
        self.plateforme.tile_images = get_tile_sprites(self.level)

    def run(self):
        while True:
            # self.screen.fill((255, 255, 255))  # Fill screen with white
            if self.treasure_found:
                self.next_level()
                continue

            if self.player.rect().collidepoint((self.treasure_coords[0] + self.treasure_size[0]/2, self.treasure_coords[1] + self.treasure_size[1]/2)):
                self.treasure_found = True

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            # img = pygame.transform.scale(img, DFLT_IMG_SZ)
            self.display.blit(pygame.transform.scale(self.bg_image, (DFLT_IMG_SZ[0] * BG_IMG_SCALE, DFLT_IMG_SZ[1] * BG_IMG_SCALE)), (-DFLT_IMG_SZ[0] - render_scroll[0], -DFLT_IMG_SZ[1] - render_scroll[1]))
                        
            self.plateforme.render(self.display, offset=render_scroll)
            self.player.update(self.plateforme, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            

            self.screen.blit(pygame.transform.scale(self.display.convert(), self.screen.get_size()), (0, 0))
            self.screen.blit(pygame.transform.scale(self.treasure_sprite, self.treasure_size), (self.treasure_coords[0] - render_scroll[0], self.treasure_coords[1] - render_scroll[1]))
            pygame.display.update()
            self.clock.tick(GAME_HZ)