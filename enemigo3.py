import pygame, random, math
from ajustes import *
from dibujarlinea import*
from bala import*



class enemigo3(pygame.sprite.Sprite):
    def __init__(self, typee, pos, tamaño, colisiones, player, grupen,atravesable):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.image.fill((255, 100, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.tipo = "torreta"
        self.colisiones = colisiones
        self.animation = False
        self.velocidad = 6
        self.id = random.uniform(0, 1000000000)
        self.cooldowndisparo = 1500
        
        self.player = player
        self.atravesable = atravesable
        self.velocidadab = 0
        self.type = typee
        self.saltar = False
        self.estado = 1
        self.tiempoen = 0
        self.stun = 0
        self.aceleracion = 0
        self.enemygr = grupen
        self.direccion = pygame.Vector2()
        self.mirando = "D"
        self.direccion.x = -1
        self.cooldown4 = 0
        self.golpeado = False
        self.mirando = True
        self.cooldownlst = 0
        self.salto = False
        self.listv = []
        self.cheked = False
        self.golpeadocol = pygame.time.get_ticks()
        self.inenemy = False
        allsprites.add(self)
        self.delayattk = 0
        self.colision = False

        spritesvisibles.add(self)
        spritescolision.add(self)
        spritesupdate.add(self)
        #enemigrup.add(self)

    def sumas(self):
        #self.direccion.y += self.gravedad 




        #self.rect.y += self.gravedad
        #self.rect.y += self.direccion.y 

        if self.golpeado == True:
            if self.tiempo - self.golpeadocol > 10:
                self.golpeado = False


    def draw_linep(start_posx, start_posy, end_pos, w, parent, colisiones, width=1):
        x1 = start_posx
        y1 = start_posy
        x2 = end_pos
        y2 = w
        dx = x2 - x1
        dy = y2 - y1
        distance = int(math.hypot(dx, dy))
        angle = math.atan2(dy, dx)

        for i in range(0, distance, 35):
            x = int(x1 + math.cos(angle) * i)
            y = int(y1 + math.sin(angle) * i)
            culo((x, y), parent, colisiones)
        
        # Si el ancho:
        if width > 1:
            for offset in range(1, width):
                for i in range(distance):
                    x_offset = int(x1 + math.cos(angle) * i)
                    y_offset = int(y1 + math.sin(angle) * i)
                    
                    # Agregar instancias arriba y abajo de la línea principal
                    culo((x_offset, y_offset + offset), parent, colisiones)
                    culo((x_offset, y_offset - offset), parent, colisiones)







        





        


    def estadoo(self):



        if abs(self.rect.x - self.player.sprite.rect.x) < 700 and abs(self.rect.y- self.player.sprite.rect.y) <700 and self.tiempo - self.cooldownlst  > self.cooldowndisparo and self.player.sprite.invulnerable == False:

 
            draw_line((self.rect.center), (self.player.sprite.rect.center),self, self.colisiones)

            
            self.cooldownlst = pygame.time.get_ticks()


        print(self.listv)


        if 1 not in self.listv and len(self.listv) != 0 and abs(self.rect.x - self.player.sprite.rect.x) < 700 and abs(self.rect.y- self.player.sprite.rect.y) <1000and self.player.sprite.invulnerable == False and self.player.sprite.invulnerablesq == False and self.estado != 4 :
                self.estado = 3






        else:
            self.estado = 2



                #print("wuw------------------------------------------------------------")


  





#        if self.estado == 3 and 1 in self.listv or self.estado == 3 and abs(self.rect.x - self.player.sprite.rect.x) > 1002 or self.estado == 3 and abs(self.rect.y- self.player.sprite.rect.y) >1000 or self.estado == 3 and self.player.sprite.invulnerable == True or self.estado == 3 and self.player.sprite.invulnerablesq == True :
  #          self.direccion.x =self.mirando
    #        #print("uwu-------------------------------------------------------------------------------------")
    #        self.tiempoen = pygame.time.get_ticks()+2000
      #      self.estado = 2

        #print(self.estado, self.player.sprite.invulnerable)












        self.listv.clear()

        if self.estado == 3:
            self.image.fill((255, 200, 200))
        if self.estado != 3:
            self.image.fill((255, 100, 200))       








            


    def movimiento(self):
   # self, pos, direccion, velocidad, duracion

       # if self.tiempo - self.cooldownlst  < self.cooldowndisparo:
         #   self.estado = 1
            

        if self.estado == 3 and self.stun == False:
            #delta_x = self.rect.center[0] - self.player.sprite.rect.center[0]
            delta_x = self.player.sprite.rect.center[0] - self.rect.center[0]
            #delta_y = self.rect.center[1] - self.player.sprite.rect.center[1]
            delta_y = self.player.sprite.rect.center[1] - self.rect.center[1]

            # Calcular el ángulo en radianes usando atan2
            angulo_radianes = math.atan2(delta_y, delta_x)

            self.predict = random.choice((1, 2))

            if self.predict == 1:



                bala((self.rect.center[0], self.rect.center[1]),  1, (16*math.cos(angulo_radianes), 16*math.sin(angulo_radianes)), 2000, 1, self.id)

            if self.predict == 2:
                bala((self.rect.center[0] + 600 * self.direccion.x*-1, self.rect.center[1]),  1, (16*math.cos(angulo_radianes), 16*math.sin(angulo_radianes)), 2000, 1, self.id)












            self.cooldown4 = pygame.time.get_ticks()
           # self.estado = 1

  



        else:
            self.direccion.x = 0

      #  print(abs(abs(self.player.sprite.rect.x) - abs(self.rect.x))/16)





            




    def collitionsy(self):





        for i in self.colisiones.sprites():
            if self.rect.colliderect(i.rect):
                
                    if self.direccion.y > 0 :
                        #print(self.direccion.x, self.velocidad, round(self.aceleracion))
                        self.direccion.y = 0
                        self.saltar = True
                        self.salto = False
                        self.inenemy = False
                        self.rect.bottom = i.rect.top
                        if i.tipo == "A":
                                self.direccion.y = -10
                                self.aceleracion = 10 * random.choice((1,-1))
                                self.direccion.x *= -1
                        


                    elif self.direccion.y < 0 :
                        self.direccion.y = 0
                        self.rect.top = i.rect.bottom










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
                            if i.tipo == "A":
                                self.direccion.y = -10
                                self.aceleracion = 10
                                self.direccion.x *= -1


                
                

                    elif(self.direccion.x*self.velocidad)+round(self.aceleracion) > 0:
                        self.direccion.x = -1
                        #self.aceleracion /= 8
                        self.aceleracion *= -1
                        self.rect.right = i.rect.left
                        if i.tipo == "A":
                                self.direccion.y = -10
                                self.aceleracion = -10
                                self.direccion.x *= -1





 




                                






                            


       
          
                        


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

        self.movimiento()







   



