import os
import pygame

def load_image(path):
    img = pygame.image.load('./' + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir('./' + path)):
        images.append(load_image(path + '/' + img_name))
    return images