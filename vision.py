import pygame, random, math
from ajustes import*

class culo(pygame.sprite.Sprite):
    def __init__(self,pos, generador, colisiones):
        super().__init__()
        self.image = pygame.Surface((6,6))
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        

        self.generador = generador
        self.colisiones = colisiones
        self.detecte = False

        spritesvisibles.add(self)
       # spritescolision.add(self)
        spritesupdate.add(self)
        allsprites.add(self)






 

    def update(self):
        for i in self.colisiones.sprites(): 
            if self.rect.colliderect(i.rect) and self.generador.id != i.id:
                print("pilinnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

                self.generador.listv.append(1)
                self.kill()




        #if self.detecte == False:
        self.generador.listv.append(0)















        self.kill()