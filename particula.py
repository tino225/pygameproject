import pygame, random, math
from ajustes import *
from claseboton import *
#from clasedibujoo import *
from hitbox import *
from bala import *
from vision import*

from enemigo1 import*
from dibujarlinea import*
from hitbox2 import *
from pilar import *



class particula(pygame.sprite.Sprite):
    def __init__(self, tamaño, color, velocidad, direccion, gravedad, duracion, crecer, invulnerable, pos, direcciony):
        super().__init__()
        self.image = pygame.Surface(tamaño)

        self.image.fill((255, 100, 200))
        self.rect = self.image.get_rect()
        self.id = 12
        self.rect.center = (pos)
        self.direccion = pygame.Vector2() 
        self.direccionx= direccion
        self.velocidad = velocidad
        self.crecer = crecer 
        self.direccion.y = direcciony 
        self.invulnerable = invulnerable 
        self.direcciony = direcciony
        self.birth = pygame.time.get_ticks()
        self.duracion = duracion

        self.gravedad = gravedad 
        self.tiempo = 0




        allsprites.add(self)


        spritesvisibles.add(self)
        #self.cols = spritescolision
        #spritescolision.add(self)
        spritesupdate.add(self)
        #enemigrup.add(self)

    def update(self):
        self.tiempo = pygame.time.get_ticks()

        if self.velocidad != 0:
            self.rect.x += self.velocidad*self.direccionx
        if self.direcciony != 0:
            self.direccion.y += self.gravedad
            self.rect.y += self.direccion.y 

        if self.crecer > 0:
            self.rect.width += self.crecer
            self.rect.height += self.crecer 

        if self.invulnerable == False:
            for i in spritescolision.sprites():
                if self.rect.colliderect(i.rect) and self.invulnerable == False:
                    self.kill()
        if self.tiempo - self.birth> self.duracion:
            self.kill()






