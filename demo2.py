import pygame, random, math


#mapa
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
"X                                            X",
"X                                            X",
"X                                            X",
"X                                            X",
"X                                            X",
"X                                           XX",
"X                                            X",
"X                                            X",
"X                                           X",
"X                                            X",
"X                                            X",
"X                                            X",
"X                                           X",
"X                           X                 X",
"X                                            X",
"X                                            X",
"X        X                                   X",
"X                                            X",
"X                                            X",
"X                                            X",
"X                                            X",
"X   P                               E        X",
"X                                            X",
"X                                            X",
"X                                            X",
"X                                            X",
"X--------------------------------------------X",
]

# Grupos de sprites
spritesvisibles = pygame.sprite.Group()
spritescolision = pygame.sprite.Group()
spritesupdate = pygame.sprite.Group()
botongrup = pygame.sprite.Group()
playergrup = pygame.sprite.GroupSingle()
enemigrup = pygame.sprite.Group()

# Configuración de Pygame
pygame.init()
screen = pygame.display.set_mode((1196,740))
clock = pygame.time.Clock()
running = True
dt = 0

# Posición inicial del jugador
player_pos = pygame.Vector2(50, screen.get_height() / 2)

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


    def update(self):
        self.tiempo = pygame.time.get_ticks()
        if self.animation and self.sss < self.duration:
            self.image.fill((255, 100, 200))
            self.sss += 1
        else:
            self.sss = 0
            self.image.fill((255, 100, 0))
            self.animation = False


class Bloque(pygame.sprite.Sprite):
    def __init__(self, typee, pos, tamaño, imagen):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.image.fill((255, 100, 0))
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.animation = False
        self.type = typee
        spritesvisibles.add(self)
        spritescolision.add(self)

    def update(self):
        self.tiempo = pygame.time.get_ticks()
        if self.animation and self.sss < self.duration:
            self.image.fill((255, 100, 200))
            self.sss += 1
        else:
            self.sss = 0
            self.image.fill((255, 100, 0))
            self.animation = False


class culo(pygame.sprite.Sprite):
    def __init__(self,pos, generador, colisiones):
        super().__init__()
        self.image = pygame.Surface((3,3))
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        

        self.generador = generador
        self.colisiones = colisiones
        self.detecte = False

        spritesvisibles.add(self)
        #spritescolision.add(self)
        spritesupdate.add(self)

    def update(self):
        for i in self.colisiones.sprites(): 
            if self.rect.colliderect(i.rect):
                self.detecte= True
            else:
                #self.generador.mirando= True
                pass

        if self.detecte == True:
            self.generador.listv.append(1)
            
        else:
            self.generador.listv.append(0)



        self.kill()



class golpe(pygame.sprite.Sprite):
    def __init__(self, pos, generador, colisiones, duration, tamaño, empujey, empujex, stun, delay):
        super().__init__()
        self.generador = generador
        self.image = pygame.Surface(tamaño)
        self.mcombstagg = self.generador.mcombstag
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
        self.delay = delay
        self.duration = duration

        if self.generador.mirando == 1:
            self.rect.topright = pos
            self.mirandoo = "D"
        else:
            self.rect.topleft = pos
            self.mirandoo = "I"


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
        else:
            if self.generador.mirando == 1:
                
                self.mirandoo = "D"
            else:
                
                self.mirandoo = "I"



        for i in self.colisiones.sprites():
            # Debug: Mostrar lista de enemigos antes de la colisión
            #print("Enemys antes de colisión:", self.enemys3)

            if self.rect.colliderect(i.rect) and i.id not in self.enemys3 and not i.golpeado and self.podergolp == True:
             #   print("Detectada colisión con enemigo:", i.id)

                i.aceleracion = 0
                i.aceleracion += self.empujex * self.generador.mirando 
                i.direccion.y = 0
                print(i.id)
                i.direccion.y = self.empujey
                i.golpeado = True
                i.golpeadocol = pygame.time.get_ticks()
                i.stun = self.stun 
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

        if self.mirandoo == "D":#*self.generador.mirando
            self.rect.topright = (self.generador.rect.center[0]+self.generador.rect.width/2*1 + self.generador.mlist[self.mcombstagg][1][0] *1, self.generador.rect.center[1] - 40)
        else:
            self.rect.topleft = (self.generador.rect.center[0]+self.generador.rect.width/2*-1 + self.generador.mlist[self.mcombstagg][1][0] *-1, self.generador.rect.center[1] - 40)
                
        #self.rect.center = (self.generador.rect.center[0] + self.generador.mlist[self.generador.mcombstag][1][0]  *self.generador.mirando, self.generador.rect.center[1] - 20)










def draw_line(start_pos, end_pos, parent, colisiones, width=1):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    distance = int(math.hypot(dx, dy))
    angle = math.atan2(dy, dx)

    for i in range(0, distance, 24):
        x = int(x1 + math.cos(angle) * i)
        y = int(y1 + math.sin(angle) * i)
        culo((x, y), parent, colisiones)
    
    # Si el ancho es mayor que 1, dibujar instancias adicionales
    if width > 1:
        for offset in range(1, width):
            for i in range(distance):
                x_offset = int(x1 + math.cos(angle) * i)
                y_offset = int(y1 + math.sin(angle) * i)
                
                # Agregar instancias arriba y abajo de la línea principal
                culo((x_offset, y_offset + offset), parent, colisiones)
                culo((x_offset, y_offset - offset), parent, colisiones)





class enemigo1(pygame.sprite.Sprite):
    def __init__(self, typee, pos, tamaño, colisiones, player, grupen):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.image.fill((255, 100, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.colisiones = colisiones
        self.animation = False
        self.velocidad = 6
        self.id = random.uniform(0, 1000000000)
        self.gravedad = 1
        self.player = player
        self.velocidadab = 0
        self.type = typee
        self.estado = 1
        self.tiempoen = 0
        self.stun = 0
        self.aceleracion = 0
        self.enemygr = grupen
        self.direccion = pygame.Vector2()
        self.mirando = "D"
        self.direccion.x = -1
        self.golpeado = False
        self.mirando = True
        self.listv = []
        self.golpeadocol = pygame.time.get_ticks()
        self.inenemy = False

        spritesvisibles.add(self)
        #spritescolision.add(self)
        spritesupdate.add(self)
        enemigrup.add(self)

    def sumas(self):
        self.direccion.y += self.gravedad 




        #self.rect.y += self.gravedad
        self.rect.y += self.direccion.y 

        if self.golpeado == True:
            if self.tiempo - self.golpeadocol > 10:
                self.golpeado = False







        





        


    def estadoo(self):
        if 1 not in self.listv and len(self.listv) != 0 and abs(self.rect.x - self.player.sprite.rect.x) < 400 and abs(self.rect.y- self.player.sprite.rect.y) <300and self.player.sprite.invulnerable == False and self.player.sprite.invulnerablesq == False:
                self.estado = 3
                #print("wuw------------------------------------------------------------")

        if abs(self.rect.x - self.player.sprite.rect.x) < 400 and abs(self.rect.y- self.player.sprite.rect.y) <300:

 
            draw_line((self.rect.center), (self.player.sprite.rect.center),self, self.colisiones)


#and abs(self.rect.x - self.player.sprite.rect.x) < 400 and abs(self.rect.y- self.player.sprite.rect.y) <300

       # "for i in self.colisiones.sprites():
            



         #   "if abs(self.rect.y- i.rect.y) <60 :
                #print(i.rect.y, self.rect.y)

              #  "if abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) <  abs(abs(self.rect.x) - abs(i.rect.x))-20 :
                    #print("uwu")
                    #print(self.rect.x, self.player.sprite.rect.x, i.rect.x)
                  # "#"pass
       


              #  else:
               #     self.inn = 1



                #print(i.rect.y, self.rect.y)


        if self.estado == 3 and 1  in self.listv or self.estado == 3 and abs(self.rect.x - self.player.sprite.rect.x) > 402 or self.estado == 3 and abs(self.rect.y- self.player.sprite.rect.y) >302 or self.estado == 3 and self.player.sprite.invulnerable == True or self.estado == 3 and self.player.sprite.invulnerablesq == True:
            self.direccion.x =self.mirando
            #print("uwu-------------------------------------------------------------------------------------")
            self.tiempoen = pygame.time.get_ticks()+2000
            self.estado = 2

        #print(self.estado, self.player.sprite.invulnerable)






      #  if abs(self.rect.x - self.player.sprite.rect.x) < 300 and abs(self.rect.y- self.player.sprite.rect.y) < 300 and self.inn != 1: 
      #      self.estado = 3
      # elif not abs(self.rect.x - self.player.sprite.rect.x) < 300 and self.estado == 3 or not abs(self.rect.y- self.player.sprite.rect.y) < 300 and self.estado == 3 or self.inn == 1 and self.estado == 3:
       #     self.estado = 2
            
       #     self.direccion.x = random.choice((1, -1))
       #     self.tiempoen = pygame.time.get_ticks()+2000
        #print(self.estado)





        if self.estado == 1 and self.tiempo - self.tiempoen > 800 :
                
                    self.estado = 2

                    self.tiempoen = pygame.time.get_ticks()
        elif self.estado == 2 and self.tiempo - self.tiempoen > 800:
                    self.estado = 1
                    self.tiempoen = pygame.time.get_ticks()

        self.listv.clear()

        if self.estado == 3:
            self.image.fill((255, 200, 200))
        if self.estado != 3:
            self.image.fill((255, 100, 200))       








            


    def movimiento(self):

        if self.estado == 1:
            self.velocidad = 1
            self.direccion.x = self.mirando

        elif self.estado == 3 and self.stun == False:

            if self.player.sprite.rect.center[0] - self.rect.center[0] < 0:
                self.velocidad = 4
                
                self.direccion.x = -1


            if self.player.sprite.rect.center[0] - self.rect.center[0]> 0:
                self.velocidad = 4
                
                self.direccion.x = 1
        else:
            self.direccion.x = 0





            




    def collitionsy(self):





        for i in self.colisiones.sprites():
            if self.rect.colliderect(i.rect):
                
                    if self.direccion.y > 0 :
                        #print(self.direccion.x, self.velocidad, round(self.aceleracion))
                        self.direccion.y = 0
                        self.inenemy = False
                        self.rect.bottom = i.rect.top
                        


                    elif self.direccion.y < 0 :
                        self.direccion.y = 0
                        self.rect.top = i.rect.bottom
                        print("insanooooooooooooooooooooooooooooooooooooooooooooooooooo")

        for i in self.enemygr.sprites():
            if self.rect.colliderect(i.rect):
                if self.id != i.id:
                    #if self.direccion.x< 0:
                         #   self.direccion.x = 1
                            
                            #i.direccion.x = -1
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )


                           # self.rect.left = i.rect.right
                            #self.direccion.x = 0

                    if self.direccion.y < 0:
                            self.rect.top = i.rect.bottom
                            self.direccion.y = 0
                            




                            
                    elif self.direccion.y > 0:
                            self.rect.bottom = i.rect.top
                            self.direccion.y = 0
                            #self.inenemy = True




        if self.rect.bottom - i.rect.top == 0:
            self.inenemy = True
            #print("jjj")
            self.velocidadab = i.velocidad*2
        else:
            self.inenemy = False



    def collitionsx(self):
        for i in self.colisiones.sprites():
                if self.rect.colliderect(i.rect):
                   # if self.direccion.x< 0:
                      #      self.direccion.x = 1
                            
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )


                        #    self.rect.left = i.rect.right
                            #self.direccion.x = 0

                    if (self.direccion.x*self.velocidad)+round(self.aceleracion) < 0:
                            self.direccion.x = 1
                            #self.aceleracion /= 8
                            self.aceleracion *= -1
                            
                            



                            self.rect.left = i.rect.right
                            print((self.direccion.x, self.velocidad), round(self.aceleracion))
                            print("uwu")


                
                

                    elif(self.direccion.x*self.velocidad)+round(self.aceleracion) > 0:
                        self.direccion.x = -1
                        #self.aceleracion /= 8
                        self.aceleracion *= -1
                        self.rect.right = i.rect.left





 

        for i in self.enemygr.sprites():
            if self.rect.colliderect(i.rect):
                if self.id != i.id:
                    print(self.id)
                    #if self.direccion.x< 0:
                         #   self.direccion.x = 1
                            
                            #i.direccion.x = -1
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )


                           # self.rect.left = i.rect.right
                            #self.direccion.x = 0

                    if (self.direccion.x*self.velocidad)+round(self.aceleracion) < 0:
                            print("izquierda--------------------------------------------------------------------")
                            self.rect.left = i.rect.right
                            self.direccion.x *= -1
                            i.direccion.x = self.direccion.x *-1

                            #self.aceleracion = 4
                            #i.direccion.x = -1
                            if abs(self.aceleracion) > abs(i.aceleracion):
                                print("yo mayor")

                                
                                i.aceleracion += self.aceleracion
                                self.aceleracion /= 2
                                #self.direccion.x = i.direccion.x




                            elif abs(i.aceleracion) > abs(self.aceleracion):
                                print("yo menor")
                                self.aceleracion += i.aceleracion
                                i.aceleracion/=2
                                #i.direccion.x = self.direccion.x
                            else:
                                print("iguales")
                                self.aceleracion = 4
                                
                                i.aceleracion = -4
                                #self.direccion.x *= -1
                                #i.direccion.x = self.direccion.x *-1



                    elif (self.direccion.x*self.velocidad)+round(self.aceleracion) > 0:
                            print("derecha---------------------------------------------------------------------")
                            self.rect.right = i.rect.left
                            self.direccion.x *= -1
                            #self.aceleracion = -4
                            i.direccion.x = self.direccion.x * -1

                            #i.direccion.x = 1
                            if abs(self.aceleracion) > abs(i.aceleracion):
                                print("yo mayor")
                                
                                i.aceleracion += self.aceleracion
                                self.aceleracion /= 2
                                #i.direccion.x = self.direccion.x


                            elif abs(i.aceleracion) > abs(self.aceleracion):
                                print("yo menor")
                                
                                self.aceleracion += i.aceleracion
                                i.aceleracion/=2
                                #self.direccion.x = i.direccion.x
                            else:
                                print("iguales")
                                self.aceleracion = -4
                                i.aceleracion = 4


                                






                            


       
          
                        


                    #elif self.direccion.x > 0:
                            #self.direccion.x = -1
                            #i.direccion.x = -1




                            #self.rect.right = i.rect.left
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )
                        
                            #self.direccion.x = 0








                            


       
          
                        


                    #elif self.direccion.x > 0:
                          #  self.direccion.x = -1




                        #    self.rect.right = i.rect.left
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )
                        
                            #self.direccion.x = 0






            












    def update(self):
        self.tiempo = pygame.time.get_ticks()
        self.estadoo()
        #self.vision()
        self.movimiento()

        if self.aceleracion > 0:
            self.aceleracion -= 0.1
        if self.aceleracion < 0:
            self.aceleracion += 0.1





        if self.inenemy == True:
            self.velocidadsum = self.velocidadab
        else:
            self.velocidadsum = self.velocidad
        if self.stun <= 0:

            self.rect.x += self.velocidadsum* self.direccion.x
        if self.stun > 0:
            self.stun-= 1
            self.direccion.x = 0
        if self.aceleracion > 10:
            self.aceleracion = 10
        if self.aceleracion  < -10:
            self.aceleracion =-10


        self.rect.x += round(self.aceleracion)
   
        self.collitionsx()
        if self.direccion.x == 1:
            self.mirando = 1
        if self.direccion.x == -1:
            self.mirando = -1 


        self.sumas()
        self.collitionsy()


 
       # print(self.estado)




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

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for i in self.spritegrup.sprites():
            if self.rect.colliderect(i.rect) and mouse[0] and pygame.time.get_ticks() - self.time > self.botoncooldown:
                self.time = pygame.time.get_ticks()
                i.animation = True

class Player(pygame.sprite.Sprite):
    def __init__(self, colisiones, enemigos, pos):
        super().__init__()
        self.aa = 0
        self.numfra = 0
        self.image = pygame.Surface((60, 70))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.sprites = (pygame.image.load("gatito.png"), pygame.image.load("gatitod.png"))

        self.image = self.sprites[1]
        self.aceleracion = 0
        self.tilin = []
        self.cooldowncol = 0
        self.pue = ""
        self.cooldowngolpe = 0
        self.invulnerable = False
        self.poder = False

       
        self.rect.topleft = player_pos
        self.colisiones = colisiones
        self.tocosuelo = False
        self.soltotecla = True
        self.tiempo = pygame.time.get_ticks()
        self.direccion = pygame.Vector2()
        self.gravedad = 3000
        self.esquivecooldown = 0
        self.saltoahor = False
        self.vida = 20
        self.intento = 0
        self.velocidad = 500
        self.enemigos = enemigos
        self.puedem = True
        self.w = 0
        self.invulnerablesq = False
        self.saltoinit = -200
        self.saltosex = 20
        self.puede = False
        self.m = 11100000000000000000000
        self.ataquecol = 0
        self.mirando = 1






        #ataquesm

        self.mcombstag = 0
        
        self.mlist = (((



            (50, (60,60), -6,1, 40, 0), 
            (50, (80,60), -8,3, 20, 50),
            (50, (100,60), -8,12, 10, 150)





            )))
        self.cooldowncombo = 0 

        spritesvisibles.add(self)
        spritesupdate.add(self)
        playergrup.add(self)

    def input(self):
        self.tilin = abs(self.direccion.x*self.velocidad*dt + abs(self.aceleracion))
        #print(self.tilin)

        keys = pygame.key.get_pressed()

        if self.invulnerablesq == False:
            self.direccion.x = keys[pygame.K_d] - keys[pygame.K_a]

        if self.direccion.x == 1:
            self.mirando = 1
        if self.direccion.x == -1:
            self.mirando = -1

        

        if keys[pygame.K_m]:
            self.m = pygame.time.get_ticks()



 

        if keys[pygame.K_a] and keys[pygame.K_d] or not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direccion.x = 0

        if self.tiempo - self.cooldowncombo > 400:
            self.mcombstag = 0

        if keys[pygame.K_m] and self.tiempo - self.ataquecol > 200 and self.puedem == True:

                


                    


                    golpe((self.rect.center[0]+self.rect.width/2*self.mirando + self.mlist[self.mcombstag][1][0] *self.mirando, self.rect.center[1] - 40), self, enemigrup, self.mlist[self.mcombstag][0], self.mlist[self.mcombstag][1], self.mlist[self.mcombstag][2], self.mlist[self.mcombstag][3]+self.tilin, self.mlist[self.mcombstag][4], self.mlist[self.mcombstag][5 ])

                    
                    if self.mcombstag == 2:
                        self.ataquecol = pygame.time.get_ticks()+500
                    else:
                        self.ataquecol = pygame.time.get_ticks()
                    self.mcombstag += 1
                    self.cooldowncombo = pygame.time.get_ticks()


        if self.mcombstag == 3:
            self.mcombstag = 0






            

            #self.ataquecol = pygame.time.get_ticks()



        

        # Almacenar el tiempo en que se presiona 'W'
        if keys[pygame.K_w]:
            self.w = pygame.time.get_ticks()

        # Permitir salto con coyote time
        if self.soltotecla and self.tiempo - self.tocosuelo < 100 and keys[pygame.K_w] and self.puede:
            #self.direccion.y += self.saltoinit
            self.direccion.y += -500
            self.tocosuelo = False
            self.soltotecla = False
            self.saltoahor = True
            #print("xulo")

        if keys[pygame.K_SPACE]  and self.tiempo - self.esquivecooldown > 1600:
                self.aceleracion = 0
                self.aceleracion = 25 * self.mirando

                self.invulnerablesq = True 
                print("uwu")
                self.esquivecooldown = pygame.time.get_ticks()


        if self.tiempo - self.esquivecooldown > 200 and self.invulnerablesq == True :
            self.invulnerablesq = False
            self.aceleracion = 0

  

 







        # Manejar intentos de salto adicionales
        if self.intento != 0:
            self.intento -= 1

        if self.soltotecla and keys[pygame.K_w] and self.puede:
            self.intento = 5



        # Controlar cooldown de salto
        if self.tiempo - self.w > 1:
            self.puede = True
        else:
            self.puede = False


        if self.tiempo - self.m > 1:
            self.puedem = True
        else:
            self.puedem = False




        if self.tiempo - self.w == 0 and self.saltoahor == True and self.saltosex != 0:
            self.direccion.y += -self.saltosex*7
            #self.direccion.y += -200
            #print(-self.saltosex*10/2)
            self.saltosex-= 1

        if 0 >= self.saltosex and self.saltoahor == True or self.tiempo - self.w > 20 and self.saltoahor == True: 
            self.saltoahor= False
            self.saltosex = 15
            #print("mal")

        #print(self.saltosex)


    def collitionsy(self):
        for i in self.colisiones.sprites():
            if self.rect.colliderect(i.rect):
                
                    if self.direccion.y > 0 :
                        self.direccion.y = 0
                        self.rect.bottom = i.rect.top
                        self.tocosuelo = pygame.time.get_ticks()
                        self.saltosex = 15
                        if self.intento != 0:
                            #self.direccion.y += self.saltoinit
                            self.direccion.y += -500
                            self.tocosuelo = False
                            self.soltotecla = False
                            self.saltoahor = True
                            #print("Intento de salto")


                    elif self.direccion.y < 0 :
                        self.direccion.y = 0
                        self.rect.top = i.rect.bottom
                        self.saltoahor = False

    def enemigoss(self):


        for i in self.enemigos.sprites():

            if self.rect.colliderect(i.rect):
                






                if self.invulnerable == False and self.invulnerablesq == False:

                    if self.rect.center[0] - i.rect.center[0] > 0:
                        
                        self.cooldowngolpe = pygame.time.get_ticks()
                        self.direccion.y = 0
                        self.aceleracion = 0


                        self.aceleracion +=  7
      
                        self.direccion.y += -1000
                        self.vida -= 1


                    elif self.rect.center[0] - i.rect.center[0] < 0:

                        self.cooldowngolpe = pygame.time.get_ticks()
                        self.direccion.y = 0
                        self.aceleracion = 0
                        self.aceleracion +=  -7


                        self.direccion.y += -1000
                        self.vida -= 1
                    else:
                        self.cooldowngolpe = pygame.time.get_ticks()
                        self.direccion.y = 0
                        self.aceleracion = 0
                        self.aceleracion +=  7* random.choice((1,-1))
                        self.direccion.y += -1000


        if self.tiempo- self.cooldowngolpe > 1000:
            self.invulnerable = False
        else:
            self.invulnerable = True



                     

   
 

    def collitionsx(self):
        self.poder = True
        for i in self.colisiones.sprites():
            if self.rect.colliderect(i.rect):

                #if self.direccion.x > 0:
                    self.pue = True
                    print(self.direccion.x, self.velocidad*dt, round(self.aceleracion))
                
                
                    if (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) < 0:

                            self.rect.left = i.rect.right
                            self.direccion.x = 0

                            #print(i.rect.x)

                            
                            print("izquierda--------------------------------------------------------------------")



                            self.aceleracion = self.aceleracion/1.6
                            self.aceleracion *= -1
                            self.poder = False
                            self.pue = "D"
                            #print(self.rect.left == i.rect.right)
                            print(i.rect.x)
                            
                            #print(f"velocidad: {self.velocidad*dt}, friccion: {self.aceleracion},")

       
          
                        


                    elif (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) > 0:




                            self.rect.right = i.rect.left
                        
                            self.direccion.x = 0
                            self.poder = False

                            
                            self.aceleracion = self.aceleracion/1.6
                            #print(i.rect.x)

     
                            self.aceleracion *= -1
                            print("derecha---------------------------------------------------------------------")

                            #print(self.rect.right == i.rect.left)
                            
                            if self.rect.colliderect(i.rect):
                                print("uwu")

                            #print(f"velocidad: {self.velocidad*dt}, friccion: {self.aceleracion},")
       







                            
                            
                            






                        

                        



                        

        if self.poder == True:
            self.aceleracion += self.direccion.x/2
                    

    def sumas(self):
        self.direccion.y += self.gravedad * dt
        self.rect.y += self.direccion.y * dt




    def update(self):
        keys = pygame.key.get_pressed()



        self.tiempo = pygame.time.get_ticks()
        self.input()
        
        self.rect.x += self.direccion.x * self.velocidad* dt
        
         #(self.direccion.x * velocidad) - self.aceleracion

        

        if  not keys[pygame.K_d] and not  keys[pygame.K_a] or keys[pygame.K_d] and  keys[pygame.K_a] or self.poder == False: 
            if self.aceleracion > 0:
               self.aceleracion -= 0.2
            if self.aceleracion < 0:
                self.aceleracion += 0.2



 
        self.rect.x += round(self.aceleracion)
        #print(self.saltoinit)




        




        self.enemigoss()
        self.collitionsx()
        
        self.sumas()
        self.collitionsy()



        





        if self.mirando == 1:
            self.image = self.sprites[1]
        elif self.mirando== -1:
            self.image = self.sprites[0]

        self.image = pygame.transform.scale(self.image, (60,70))
        self.numfra +=1
        print(f"frame: {self.numfra}")

# Instancias de las clases
#playerr = Player(spritescolision)
cursorr = Cursor(botongrup)
y = 0
x = 0
tilesize= 26
#bloquee = Bloque(1, (600, 600))

# Bucle principal del juego


for i in m1:
    
    x=0

    for b in m1[y]:
        
        if b=="X":
            bloquee = Bloque(1, (x*tilesize,y*tilesize), (tilesize,tilesize),pygame.image.load("tierra.png") )
        if b=="-":
            bloquee = Bloque(1, (x*tilesize,y*tilesize), (tilesize,tilesize),pygame.image.load("pasto.png") )
        if b=="x":
            bloquee = Bloque(1, (x*32,y*32), (240,26))
        if b =="P":
            playerr = Player(spritescolision, enemigrup, (x*32,y*32))
        if b =="E":
            enemigo1(1, (x*32, y*32), (40,60), spritescolision, playergrup, enemigrup)


        x+=1
    y+=1







while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerr.soltotecla = True



    screen.fill(((230, 230, 230)))
    spritesupdate.update()
    spritesvisibles.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()