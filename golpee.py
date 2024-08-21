import pygame, random, math
from ajustes import*






class golpe(pygame.sprite.Sprite):
    def __init__(self, pos, generador, colisiones, duration, tamaño, empujey, empujex, stun, delay, mirando, genx):
        super().__init__()
        self.generador = generador
        self.image = pygame.Surface(tamaño)
        self.mcombstagg = self.generador.mcombstag
        self.image.fill((255, 100, 0))
        self.genx = genx
        self.rect = self.image.get_rect()
        self.delay = delay
        self.duration = duration
        allsprites.add(self)


        self.mirandoo = mirando
        if self.mirandoo == 1:#*self.generador.mirando


            self.rect.topright = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0]*1 , self.generador.rect.center[1] - 40)
        elif self.mirandoo == -1:
#self.rect.topleft = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0]*-1 + self.generador.mlist[self.mcombstagg][1][0] *-1, self.generador.rect.center[1] - 40)
            self.rect.topleft = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0] *-1, self.generador.rect.center[1] - 40)
        elif self.mirandoo == 3:
            self.mcombstagg = 4
            self.rect.center = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0]  , self.generador.rect.center[1] +50)
#self.generador.mlist[self.mcombstagg][1][0]

        self.empujex = empujex
        #self.mirandoo = self.generador.mirando 
        self.empujey = empujey 
        self.tiempomuert = 0
        self.enemys3 = []
        self.tiempoinit = pygame.time.get_ticks()
        self.podergolp = False


        self.colisiones = colisiones
        self.detecte = False
        self.stun = stun 

        #spritesvisibles.add(self)
        #spritescolision.add(self)
        spritesupdate.add(self)

    def update(self):
        self.tiempoo = pygame.time.get_ticks()

        # Debug: Mostrar el tiempo actual
      #  print("Tiempo actual:", self.tiempoo)
        if self.tiempoo - self.tiempoinit > self.delay:
            self.podergolp = True
            spritesvisibles.add(self)
            self.tiempomuert = pygame.time.get_ticks()
            self.delay = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000




        for i in self.colisiones.sprites():
            # Debug: Mostrar lista de enemigos antes de la colisión
            #print("Enemys antes de colisión:", self.enemys3)
            #if i.id in self.enemys3:
              #  pass

            if self.rect.colliderect(i.rect) and i.id not in self.enemys3 and not i.golpeado and self.podergolp == True or self.rect.colliderect(i.rect) and i.id not in self.enemys3 and not i.golpeado and self.mirandoo == True and self.podergolp == True:
             #   print("Detectada colisión con enemigo:", i.id)


                if self.mirandoo != 3:
                    i.aceleracion = 0
                    i.aceleracion += self.empujex * self.mirandoo
                    i.direccion.y = 0

                    print(i.id)
                    i.direccion.y = self.empujey
                    i.golpeado = True
                    i.golpeadocol = pygame.time.get_ticks()

                else:
                    self.generador.direccion.y = 0
                    self.generador.direccion.y += self.genx
                i.stun = self.stun 
                #print("golpeadooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                self.enemys3.append(i.id)  # Asegúrate de agregar el id del enemigo

            # Debug: Mostrar lista de enemigos después de la colisión
         #   print("Enemys después de colisión:", self.enemys3)

        # Verificar si el tiempo del golpe ha expirado
      #  print(self.tiempoo)
        print(self.tiempoo, self.tiempomuert)
        if self.tiempoo - self.tiempomuert > self.duration and self.podergolp == True:
            self.kill()

        # Debug: Mostrar lista de enemigos al final del update
      #  print("Enemys al final del update:", selfmm.enemys3)
      #(self.mlist[0][6][0]*-1 + self.mlist[self.mcombstag][1][0] *-1, self.rect.center[1] - 40)

        if self.mirandoo == 1:#*self.generador.mirando
            

            self.rect.topright = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0]*1 + self.generador.mlist[self.mcombstagg][1][0] *1, self.generador.rect.center[1] - 40)
        elif self.mirandoo == -1:
            self.rect.topleft = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0]*-1 + self.generador.mlist[self.mcombstagg][1][0] *-1, self.generador.rect.center[1] - 40)
            

        elif self.mirandoo == 3:
            self.mcombstagg = 4
            self.rect.center = (self.generador.rect.center[0]+self.generador.mlist[self.mcombstagg][6][0]  , self.generador.rect.center[1] +70)