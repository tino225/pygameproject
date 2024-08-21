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
"X                         E                 XX",
"X                                            X",
"X                                    E       X",
"X                                            X",
"X                          E                 X",
"X                                            X",
"X       E                                    X",
"X                                            X",
"X                          X                 X",
"X                                            X",
"X                                    E       X",
"X        X                                   X",
"X                                            X",
"X                       E                    X",
"X                                            X",
"X                                            X",
"X   P             E                          X",
"X   X                                        X",
"X   X                                   E    X",
"X  X                                         X",
"X  X                                         X",
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
        self.image = pygame.Surface((4,4))
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


class cuulo(pygame.sprite.Sprite):
    def __init__(self,pos, generador, colisiones):
        super().__init__()
        self.image = pygame.Surface((1,1))
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
        pass


def draw_line(start_pos, end_pos, parent, colisiones, width=1):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    distance = int(math.hypot(dx, dy))
    angle = math.atan2(dy, dx)

    for i in range(0, distance, 30):
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
        self.id = random.uniform(0, 10000000000000000000000000000)
        self.gravedad = 10
        self.player = player
        self.velocidadab = 0
        self.type = typee
        self.estado = 1
        self.tiempoen = 0
        self.aceleracion = 0
        self.enemygr = grupen
        self.direccion = pygame.Vector2()
        self.mirando = "D"
        self.direccion.x = -1
        self.mirando = True
        self.listv = []
        self.inenemy = False

        spritesvisibles.add(self)
        #spritescolision.add(self)
        spritesupdate.add(self)
        enemigrup.add(self)

    def sumas(self):
        self.direccion.y += self.gravedad 
        self.rect.y += self.gravedad
        #print(self.mirando)






        





        


    def estadoo(self):
        if 1 not in self.listv and len(self.listv) != 0 and abs(self.rect.x - self.player.sprite.rect.x) < 400 and abs(self.rect.y- self.player.sprite.rect.y) <300and self.player.sprite.invulnerable == False and self.player.sprite.invulnerablesq == False:
                self.estado = 3
                print("wuw------------------------------------------------------------")

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
            print("uwu-------------------------------------------------------------------------------------")
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





        if self.estado == 1 and self.tiempo - self.tiempoen > 800:
                
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
            #self.velocidad = 2
            self.direccion.x = self.mirando

        elif self.estado == 3:

            if self.player.sprite.rect.center[0] - self.rect.center[0] < 0:
                self.velocidad = 5
                
                self.direccion.x = -1


            if self.player.sprite.rect.center[0] - self.rect.center[0]> 0:
                self.velocidad = 5
                
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
                            print("wwwwwwwwwwwwwwwwwwwwwwww")
                            #self.inenemy = True



        if  i.rect.top -  self.rect.bottom ==0:
            self.inenemy = True

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
                            self.aceleracion /= 8
                            self.aceleracion *= -1
                            
                            



                            self.rect.left = i.rect.right
                            print((self.direccion.x, self.velocidad), round(self.aceleracion))
                            print("uwu")


                
                

                    elif(self.direccion.x*self.velocidad)+round(self.aceleracion) > 0:
                        self.direccion.x = -1
                        self.aceleracion /= 8
                        self.aceleracion *= -1
                        self.rect.right = i.rect.left





 

        for i in self.enemygr.sprites():
            if self.rect.colliderect(i.rect):
                if self.id != i.id:
                    #if self.direccion.x< 0:
                         #   self.direccion.x = 1
                            
                            #i.direccion.x = -1
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )


                           # self.rect.left = i.rect.right
                            #self.direccion.x = 0

                    if (self.direccion.x*self.velocidad)+round(self.aceleracion) < 0:
                            self.rect.left = i.rect.right
                            self.direccion.x *= -1
                            i.direccion.x = -1
                            self.aceleracion = 6
                            #i.direccion.x = -1
                            i.aceleracion = -4
                            
                    elif (self.direccion.x*self.velocidad)+round(self.aceleracion) > 0:
                            self.rect.right = i.rect.left
                            self.direccion.x *= -1
                            self.aceleracion = -6
                            i.direccion.x = 1

                            #i.direccion.x = 1
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
            self.aceleracion -= 0.2
        if self.aceleracion < 0:
            self.aceleracion += 0.2





        if self.inenemy == True:
            self.velocidadsum = self.velocidadab*2
            print("uwu")
        else:
            self.velocidadsum = self.velocidad
        self.rect.x += self.velocidadsum* self.direccion.x 
        self.rect.x += round(self.aceleracion)
   
        self.collitionsx()
        if self.direccion.x == 1:
            self.mirando = 1
        if self.direccion.x == -1:
            self.mirando = -1 
        self.sumas()
        self.collitionsy()


 
        print(self.estado)








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
        self.rect.center = pos
        self.sprites = (pygame.image.load("gatito.png"), pygame.image.load("gatitod.png"))

        self.image = self.sprites[1]
        self.aceleracion = 0
        self.tilin = []
        self.cooldowncol = 0
        self.pue = ""
        self.cooldowngolpe = 0
        self.invulnerable = False
       
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
        self.w = 0
        self.invulnerablesq = False
        self.saltoinit = -200
        self.saltosex = 20
        self.puede = False
        self.mirando = "D"
        spritesvisibles.add(self)
        spritesupdate.add(self)
        playergrup.add(self)

    def input(self):
        keys = pygame.key.get_pressed()

        if self.invulnerablesq == False:
            self.direccion.x = keys[pygame.K_d] - keys[pygame.K_a]

        if self.direccion.x == 1:
            self.mirando = 1
        if self.direccion.x == -1:
            self.mirando = -1


 

        if keys[pygame.K_a] and keys[pygame.K_d] or not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direccion.x = 0

        

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


                        self.aceleracion +=  10
      
                        self.direccion.y += -1000
                        self.vida -= 1


                    elif self.rect.center[0] - i.rect.center[0] < 0:

                        self.cooldowngolpe = pygame.time.get_ticks()
                        self.direccion.y = 0
                        self.aceleracion = 0
                        self.aceleracion +=  -10


                        self.direccion.y += -1000
                        self.vida -= 1
                    else:
                        self.cooldowngolpe = pygame.time.get_ticks()
                        self.direccion.y = 0
                        self.aceleracion = 0
                        self.aceleracion +=  10* random.choice((1,-1))
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
                    print(self.direccion.x, self.velocidad, self.aceleracion)
                
                
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