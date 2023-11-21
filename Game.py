import time
import pygame
from Caillou import Caillou
from Plateforme import Plateforme
from Image import load_image
from constants import GAME_HZ

DFLT_IMG_SZ = (1200, 860)
class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('La Legende de Caillou')

        self.screen = pygame.display.set_mode(DFLT_IMG_SZ)

        self.display = pygame.Surface(DFLT_IMG_SZ)

        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        self.player = Caillou((50, 50), (40, 75), self)
        self.scroll = [0, 0]
        self.tilemap = Plateforme(self)

        self.paused = False


    def run(self):
        treasure_coords = (500, 500)
        treasure_sprite = load_image('treasures/treasure1.png')
        treasure_size = (50, 50)
        pause_count = 10
        while True:
            if self.paused:
                # Do cutscene / level switch logic
                pause_count -= 1
                if pause_count <= 0:
                    self.paused = False
                    pause_count = 10
                self.clock.tick(GAME_HZ)
                continue

            if self.player.rect().colliderect(pygame.Rect(treasure_coords[0], treasure_coords[1], treasure_size[0], treasure_size[1])):
                self.paused = True

            # img = pygame.transform.scale(img, DFLT_IMG_SZ)
            self.display.blit(pygame.transform.scale(load_image('player/shesh.png'), DFLT_IMG_SZ), (0, 0))
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.tilemap.render(self.display, offset=render_scroll)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
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
            

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.screen.blit(pygame.transform.scale(treasure_sprite, treasure_size), (treasure_coords))
            pygame.display.update()
            self.clock.tick(GAME_HZ)