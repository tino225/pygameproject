import pygame, random, math
from ajustes import *



class Cursor(pygame.sprite.Sprite):
    def __init__(self, spritegrup):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.botoncooldown = 300
        self.time = 0
        self.stage = 0
        self.spritegrup = spritegrup
        spritesvisibles.add(self)
        spritesupdate.add(self)
        allsprites.add(self)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for i in self.spritegrup.sprites():
            if self.rect.colliderect(i.rect) and mouse[0] and pygame.time.get_ticks() - self.time > self.botoncooldown:
                self.time = pygame.time.get_ticks()
                i.animation = True