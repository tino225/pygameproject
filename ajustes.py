import pygame
m2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                            X",
"X                                            X",
"X   P                                        X",
"X                                            X",
"X                                            X",
"X            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                            X",
"X        X                   X  X            X",
"X       XX                   X               X",
"X        X                   X            XXXX",
"X        X                   X               X",
"X        X                   XX              X",
"X        X                   X               X",
"XX       X                   X               X",
"X        X                   X               X",
"X        X                   X               X",
"X        X                   X               X",
"X        X                   X               X",
"X        X                   X               X",
"X       XX                   X               X",
"X        X          E        X               X",
"X        X                   X               X",
"X        X                   X               X",
"X        X                   X               X",
"X        X                   X               X",
"X                                            X",
"X--------------------------------------------X"
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]


m1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                           ",
"X                                                                                                                          X",
"X                                                                                                                          X",
"X                                                                                                                         X",
"X                                                                                                                          X",
"X                                                                                                                          X",
"X                                                                                                                         X",
"X                                                                                                                          X",
"X                                                                                              E                          X",
"X                                                                                                                          X",
"X            P                                                                                                             X",
"X                                                                                                      E                   X",
"X                                                                                                                         X",
"X                                                                                                                          X",
"X                                                          e                                                                X",
"X                                                                                                                           X",
"X        X                 E                                                                       i      i                X",
"X                                                                                                                          X",
"X                                                                                                                          X",
"X                                                                                                                          X",
"X                                                                       XX                                                 X",
"X    XXXXXX                                                                                                                X",
"X         X                                                                                                                   X",
"X         X                               X                                                                                 ",
"X         X                               X                                                                                 ",
"X         X                               X             p                                 X--------------------------------------------------------------------------------------------------------------------------X                                X",
"X--------------------------------------------------------------------------------------------------------------------------X",
]

m2 = [
"XXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X P                                                                                           ",
"X                                                                                             ", 
"X                                                                                             ", 
"X                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 X", 
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                               X",

]

# Grupos de sprites
spritesvisibles = pygame.sprite.Group()
spritescolision = pygame.sprite.Group()
spritesupdate = pygame.sprite.Group()
botongrup = pygame.sprite.Group()
playergrup = pygame.sprite.GroupSingle()
enemigrup = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
objgrup= pygame.sprite.Group()



# Configuración de Pygame
pygame.init()
screen = pygame.display.set_mode((1196,740))
clock = pygame.time.Clock()
running = True
dt = 0