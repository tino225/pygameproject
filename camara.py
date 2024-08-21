import pygame, random, math
from ajustes import*












class Camara(pygame.sprite.Sprite):
    def __init__(self, spritesvisiblesn):
        super().__init__()
        self.spritess = spritesvisiblesn
        self.pixelesoff = 0
        self.ratiocamb = 0.001
        self.mirando = 1
        self.sumai = 0
        self.delaycam = 100
        self.playerofy = 0
        self.playerofx = 0
        self.e = False
        self.u = 0
        allsprites.add(self)
        









    def draw(self, screen, player):
        for i in self.spritess.sprites():
            if hasattr(i, 'image') and hasattr(i, 'rect') and abs(i.rect.x+player.offsetx+round(self.pixelesoff)) < 1200 and abs(i.rect.x+player.offsetx+round(self.pixelesoff)) > -10:


                self.playerofx = player.offsetx




              #  self.delaycam = pygame.time.get_ticks()

   
                if player.mirando == -1: 
                    if self.mirando == 1:
                        self.mirando = -1
                        self.ratiocamb = 0.00000001

                        #self.delaycam = pygame.time.get_ticks()


                    if self.pixelesoff < 81:
                        if self.ratiocamb < 0.28:
                            self.ratiocamb += 0.00005
                        self.pixelesoff += self.ratiocamb /8

                else:
                    if self.mirando == -1:
                        self.mirando = 1
                        self.ratiocamb =0.00000001

                        #self.delaycam = pygame.time.get_ticks()
                    if self.pixelesoff > -81:
                        if self.ratiocamb < 0.28:
                            self.ratiocamb += 0.00005
                        self.pixelesoff -= self.ratiocamb/8 


                if abs(abs(self.sumai) - abs(player.offsety - 50)) > 1 and self.u == 0:
                        self.delaycam = pygame.time.get_ticks()
                        self.playerofy = player.offsety

                        self.u = 1
                if abs(abs(self.sumai) - abs(player.offsety - 50)) < 1  and self.u == 1:
                        self.u = 0
                        self.e = False
                        self.playerofy = player.offsety

                        #print(player.tiempo - self.delaycam)
                if self.u == 1 and player.tiempo - self.delaycam> 200:
                    self.e = True

                    if self.sumai >player.offsety - 50:
                            self.sumai += -(abs(abs(self.sumai) - abs(player.offsety)))/ 3000
                    elif self.sumai < player.offsety - 50:
                            self.sumai += (abs(abs(self.sumai) - abs(player.offsety)))/ 3000

                    self.playerofy = player.offsety

             #   print(self.sumai)





#+ self.playerofy+50

                screen.blit(i.image, (i.rect.x+player.offsetx+round(self.pixelesoff), i.rect.y + round(self.sumai)))

















