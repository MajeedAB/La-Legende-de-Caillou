
import pygame

NUMBER_OF_IMAGES_CUTSCENE_0 = 14
DIALOG_PATH_DRMARIO = 'Dialogue_DrMario/Dialogue'
DIALOG_PATH_SPYRO =  'Dialogue_Spyro/Dialogue'
DIALOG_EXT = '.png'

NUMBER_OF_IMAGES_CUTSCENE_1 = 9


def cinematique_0(screen, display, clock):
    for i in range (NUMBER_OF_IMAGES_CUTSCENE_0):
        img = pygame.image.load(DIALOG_PATH_SPYRO + str(i) + DIALOG_EXT).convert()
        img.set_colorkey((45, 73, 255))
        screen.blit(pygame.transform.scale(img, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(0.5)

def cinematique_1(screen, display, clock):
    for i in range (NUMBER_OF_IMAGES_CUTSCENE_1):
        img = pygame.image.load(DIALOG_PATH_DRMARIO + str(i) + DIALOG_EXT).convert()
        img.set_colorkey((45, 73, 255))
        screen.blit(pygame.transform.scale(img, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(0.5)