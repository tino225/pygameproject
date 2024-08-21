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



class pilar(pygame.sprite.Sprite):
    def __init__(self, pos, tamaño, imagen, tamañoimag, content, objetoimag, colorobj, tamañoobj):
        super().__init__()
        self.id = random.uniform(0, 10000000000000000000000000)
        self.image = pygame.Surface(tamaño)
        self.rect = self.image.get_rect()
        self.tiempo = pygame.time.get_ticks()
        self.tamañoobj = tamañoobj
        self.image.fill((255, 100, 0))
        self.content = content
        self.imageobj = objetoimag
        self.colorobj = colorobj
        self.content = content
        self.a = ""
        self.tipo = "pilar"

        self.movi = 1
        self.velocidad = 2
        self.cheked = False


        self.rect.center = pos

        self.aposin = self.rect.center[1]
        #self.dibujo = Dibujo((pos), tamañoimag, imagen)
 

        
        spritesvisibles.add(self)
        #spritescolision.add(self)
        allsprites.add(self)
        spritesupdate.add(self)
        objgrup.add(self)
    def update(self):



        if abs(abs(self.aposin)-abs(self.rect.y)) > 20:


           self.movi *= -1

        print(abs(abs(self.aposin)-abs(self.rect.y)) )












        self.dif = (abs(self.rect.y)-abs(self.aposin))/10
 
        self.rect.y += (abs(self.dif)+1)* self.movi 
 






















