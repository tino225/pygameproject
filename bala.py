import pygame, random, math
from ajustes import *

class bala(pygame.sprite.Sprite):
    def __init__(self, pos, direccion, velocidad, duracion, direcciony, idd):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.rect = self.image.get_rect()
        #self.image.fill((255, 100, 0))

        self.velocidad = velocidad 
        self.duracion = duracion 
        self.tiempoinit = pygame.time.get_ticks()
        self.direccion = pygame.Vector2()
        self.atravesable = False
        self.golpeado = ""
        self.saltar = False
        self.direccion.x = direccion
        self.direccion.y = direcciony
        self.velocidadx, self.velocidady = velocidad[0], velocidad[1]
        self.colisiones = spritescolision
        self.tipo = "bala"
        self.id = idd


        self.rect.center = pos


 

         


        spritesvisibles.add(self)
        #spritescolision.add(self)
        enemigrup.add(self)

        spritesupdate.add(self)
        allsprites.add(self)
    def update(self):
        self.tiempo = pygame.time.get_ticks()
        self.rect.x += self.velocidadx 
        if self.tiempo - self.tiempoinit > self.duracion:
            self.kill()

        for i in self.colisiones:
            if self.rect.colliderect(i.rect) and self.id != i.id and i.tipo != "P":
                self.kill()

 
            if i.tipo == "P" and self.rect.colliderect(i.rect) and self.id != i.id :
                    if self.velocidadx > 0:

                        self.rect.right = i.rect.left
                        self.velocidadx *= -1







                    elif self.velocidadx < 0 :

                        self.rect.left= i.rect.right
                        self.velocidadx *= -1






            


        self.rect.y += self.velocidady

        for i in self.colisiones:
            if self.rect.colliderect(i.rect) and self.id != i.id and i.tipo != "P":
                self.kill()

            if i.tipo == "P" and self.rect.colliderect(i.rect) and self.id != i.id :
                    if self.velocidady > 0:

                        self.rect.bottom = i.rect.top
                        self.velocidady *= -1







                    elif self.velocidady < 0 :

                        self.rect.top= i.rect.bottom
                        self.velocidady *= -1

 



