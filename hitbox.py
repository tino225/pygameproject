import pygame, random, math
from clasedibujoo import *
from ajustes import*
class Hitbox(pygame.sprite.Sprite):
    def __init__(self, typee, pos, tamaño, imagen, piso, tamañoimag ):
        super().__init__()
        self.id = random.uniform(0, 10000000000000000000000000)
        self.image = pygame.Surface(tamaño)
        self.rect = self.image.get_rect()
        self.tiempo = pygame.time.get_ticks()
        #self.image.fill((255, 100, 0))

        self.tipo = piso
        self.rect.center = pos
        self.dibujo = Dibujo((pos), tamañoimag, imagen)
 

         

  
        self.type = typee
        #spritesvisibles.add(self)
        spritescolision.add(self)
        allsprites.add(self)


