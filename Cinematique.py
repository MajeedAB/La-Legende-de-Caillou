
import pygame

NUMBER_OF_IMAGES_CUTSCENE_0 = 14
DIALOG_PATH =  'Dialogue_Spyro/Dialogue'
DIALOG_EXT = '.png'

def cinematique_0(screen, display, clock):
    for i in range (NUMBER_OF_IMAGES_CUTSCENE_0):
        img = pygame.image.load(DIALOG_PATH + str(i) + DIALOG_EXT).convert()
        img.set_colorkey((45, 73, 255))
        screen.blit(pygame.transform.scale(img, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(0.5)

