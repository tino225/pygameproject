import pygame, random, math
from clasedibujoo import *
from ajustes import*

class Hitbox2(pygame.sprite.Sprite):
    def __init__(self, typee, pos, tamaño, imagen, piso, tamañoimag, dur):
        super().__init__()
        self.id = random.uniform(0, 10000000000000000000000000)
        self.image = pygame.Surface(tamaño)
        self.rect = self.image.get_rect()
        self.tiempo = pygame.time.get_ticks()
        self.image.fill((255, 100, 0))
        self.tiempoinit = pygame.time.get_ticks()
        self.dur = dur


        self.tipo = piso
        self.rect.center = pos
        #self.dibujo = 
 

         

  
        self.type = typee
        spritesvisibles.add(self)
        spritescolision.add(self)
        allsprites.add(self)
        spritesupdate.add(self)
    def update(self):
        self.tiempo = pygame.time.get_ticks()
        if self.tiempo-self.tiempoinit > self.dur:
            self.kill()
            #self.dibujo.kill()

