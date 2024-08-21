import pygame

class Boton(pygame.sprite.Sprite):
    def __init__(self, typee, pos):
        super().__init__()
        self.image = pygame.Surface((200, 20))
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.animation = False
        self.type = typee
        self.tiempo = pygame.time.get_ticks()
        self.tiemposalto = 0
        self.duration = 5
        self.sss = 0

        spritesvisibles.add(self)
        spritesupdate.add(self)
        botongrup.add(self)
        allsprites.add(self)


    def update(self):
        self.tiempo = pygame.time.get_ticks()
        if self.animation and self.sss < self.duration:
            self.image.fill((255, 100, 200))
            self.sss += 1
        else:
            self.sss = 0
            self.image.fill((255, 100, 0))
            self.animation = False