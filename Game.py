import pygame
from Caillou import Caillou
from Plateforme import Plateforme
from Image import load_image

DFLT_IMG_SZ = (1200, 860)
class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('La Legende de Caillou')

        self.screen = pygame.display.set_mode(DFLT_IMG_SZ)

        self.display = pygame.Surface(DFLT_IMG_SZ)

        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        self.player = Caillou((50, 50), (8, 15), self)
        self.scroll = [0, 0]
        self.tilemap = Plateforme(self)



    def run(self):

        while True:
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
            pygame.display.update()
            self.clock.tick(60)