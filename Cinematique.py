
import pygame

NUMBER_OF_IMAGES_CUTSCENE_0 = 14
NUMBER_OF_IMAGES_CUTSCENE_1 = 9
NUMBER_OF_IMAGES_CUTSCENE_2 = 10
NUMBER_OF_IMAGES_CUTSCENE_3 = 11
NUMBER_OF_IMAGES_CUTSCENE_4 = 9

DIALOG_PATH_SPYRO =  'Dialogue_Spyro/Dialogue'
DIALOG_PATH_DRMARIO = 'Dialogue_DrMario/Dialogue'
DIALOG_PATH_PIKACHU =  'Dialogue_Pikachu/Dialogue'
DIALOG_PATH_OLIMAR= 'Dialogue_Olimar/Dialogue'
DIALOG_PATH_FIN= 'Dialogue_Fin/Dialogue'
DIALOG_EXT = '.png'



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
        clock.tick(0.35)

def cinematique_2(screen, display, clock):
    for i in range (NUMBER_OF_IMAGES_CUTSCENE_2):
        img = pygame.image.load(DIALOG_PATH_PIKACHU + str(i) + DIALOG_EXT).convert()
        img.set_colorkey((45, 73, 255))
        screen.blit(pygame.transform.scale(img, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(0.35)

def cinematique_3(screen, display, clock):
    for i in range (NUMBER_OF_IMAGES_CUTSCENE_3):
        img = pygame.image.load(DIALOG_PATH_OLIMAR + str(i) + DIALOG_EXT).convert()
        img.set_colorkey((45, 73, 255))
        screen.blit(pygame.transform.scale(img, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(0.35)

def cinematique_4(screen, display, clock):
    for i in range (NUMBER_OF_IMAGES_CUTSCENE_4):
        img = pygame.image.load(DIALOG_PATH_FIN + str(i) + DIALOG_EXT).convert()
        img.set_colorkey((45, 73, 255))
        screen.blit(pygame.transform.scale(img, screen.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(0.35)