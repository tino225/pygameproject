import pygame, random, math
from ajustes import*
class sierra(pygame.sprite.Sprite):
    def __init__(self, pos, tamaño, velocidad, endstr, aceleracion, slowfin, espera):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.rect = self.image.get_rect()
        self.image.fill((0, 100, 255))
        self.tipo = "sierra"
        self.direccion = pygame.Vector2()
        self.espera = espera
        self.tiempo = pygame.time.get_ticks()
        self.posinx, self.posiny = pos[0], pos[1]
        self.haciad = 1

        self.rect.center = pos

        self.endx, self.endy = endstr[0], endstr[1]
        self.velocidad = velocidad
        self.aceleracion = aceleracion
        self.slowfin = slowfin 

        spritesvisibles.add(self)
        spritescolision.add(self)
        spritesupdate.add(self)
        allsprites.add(self)

    def movx(self):
        if self.haciad == -1:


            if self.rect.x >= self.posinx and self.direccion.x == 1:

                self.rect.x = self.posinx 
                self.haciad = 1 
                self.direccion.x = -1
                

            elif self.rect.x <= self.posinx and self.direccion.x == -1:
                self.direccion.x = 1
                self.rect.x = self.posinx 
                self.haciad = 1 
                

            if self.rect.x > self.posinx and self.haciad != 1 and self.direccion.x !=-1:
                self.direccion.x = -1

            elif self.rect.x < self.posinx and self.haciad != 1 and self.direccion.x != 1:
                self.direccion.x = 1



        elif self.haciad == 1:









            if self.rect.x >= self.endx and self.direccion.x == 1:
                print("wuudddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
                self.rect.x = self.endx 
                self.haciad = -1 
                self.direccion.x = -1
                

            elif self.rect.x <= self.endx and self.direccion.x == -1:
                self.direccion.x = 1
                self.rect.x = self.endx 
                self.haciad = -1 
                

            if self.rect.x > self.endx and self.haciad != -1 and self.direccion.x !=-1:
                self.direccion.x = -1

            elif self.rect.x < self.endx and self.haciad != -1 and self.direccion.x != 1:
                self.direccion.x = 1
                print(self.haciad)
                print("lslsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")









        print(self.direccion.x, self.haciad)
        self.rect.x += self.velocidad * self.direccion.x 




    def update(self):
        self.movx()
