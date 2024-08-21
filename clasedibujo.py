import pygame, random, math

class Dibujo(pygame.sprite.Sprite):
    def __init__(self, pos, tamaño, imagen):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.rect = self.image.get_rect()


 
        self.rect.center = pos
 

        self.image  = imagen 
        self.image = pygame.transform.scale(self.image, tamaño)

  

        spritesvisibles.add(self)
        #spritescolision.add(self)
       # allsprites.add(self)