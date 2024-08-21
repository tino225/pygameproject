import pygame, random, math
from ajustes import *
class Dibujo(pygame.sprite.Sprite):
    def __init__(self, pos, tamaño, imagen):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.rect = self.image.get_rect()


 
        self.rect.center = pos
 
        if imagen != "":
            self.image  = imagen 
            self.image = pygame.transform.scale(self.image, tamaño)
        else:
            self.image.fill((255, 100, 0))

  

        spritesvisibles.add(self)
        #spritescolision.add(self)
        allsprites.add(self)
       # dibujosprite.add(self)
