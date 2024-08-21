import pygame, random, math
from ajustes import *
from dibujarlinea import*


class enemigo2(pygame.sprite.Sprite):
    def __init__(self, typee, pos, tamaño, colisiones, player, grupen, atravesable):
        super().__init__()
        self.image = pygame.Surface(tamaño)
        self.image.fill((255, 100, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.colisiones = colisiones
        self.animation = False
        self.velocidad = 6
        self.tipo = "2"
        self.atravesable = atravesable
        self.id = random.uniform(0, 1000000000)
        self.gravedad = 1
        self.player = player
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
        self.salto = False
        self.listv = []
        self.golpeadocol = pygame.time.get_ticks()
        self.inenemy = False
        allsprites.add(self)
        self.delayattk = 0

        spritesvisibles.add(self)
        #spritescolision.add(self)
        spritesupdate.add(self)
        enemigrup.add(self)

    def sumas(self):
        if self.direccion.y > 20:
            self.direccion.y = 20

        self.direccion.y += self.gravedad 




        #self.rect.y += self.gravedad
        self.rect.y += self.direccion.y 

        if self.golpeado == True:
            if self.tiempo - self.golpeadocol > 10:
                self.golpeado = False







        





        


    def estadoo(self):
        if 1 not in self.listv and len(self.listv) != 0 and abs(self.rect.x - self.player.sprite.rect.x) < 300 and abs(self.rect.y- self.player.sprite.rect.y) <600and self.player.sprite.invulnerable == False and self.player.sprite.invulnerablesq == False and self.estado != 4:
                self.estado = 3

                #print("wuw------------------------------------------------------------")

        if abs(self.rect.x - self.player.sprite.rect.x) < 502 and abs(self.rect.y- self.player.sprite.rect.y) <500:

 
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


        if self.estado == 3 and 1  in self.listv or self.estado == 3 and abs(self.rect.x - self.player.sprite.rect.x) > 502 or self.estado == 3 and abs(self.rect.y- self.player.sprite.rect.y) >502 or self.estado == 3 and self.player.sprite.invulnerable == True or self.estado == 3 and self.player.sprite.invulnerablesq == True:
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

        elif self.estado == 3 and self.stun == False and self.saltar == True and self.tiempo - self.cooldown4 > 2000:

            if self.player.sprite.rect.center[0] - self.rect.center[0] < -50:

                self.velocidad = 4 


                self.salto = True
                self.direccion.y = -20


                self.direccion.x = -1
                self.aceleracion =   ((6* abs(abs(self.player.sprite.rect.x) - abs(self.rect.x)) /90* self.direccion.x)/2.1)+2*self.direccion.x
                if self.aceleracion > -8:
                    self.aceleracion = -8




            elif self.player.sprite.rect.center[0] - self.rect.center[0]> 50:
                self.velocidad = 4
                
                self.direccion.x = 1
                self.salto = True
                salto =  -abs(abs(self.player.sprite.rect.x) - abs(self.rect.x))/14
                if salto < -20:
                    salto = -20
                self.direccion.y = -20
                self.aceleracion = ((6* abs(abs(self.player.sprite.rect.x) - abs(self.rect.x)) /87* self.direccion.x)/2.1)+2*self.direccion.x
                if self.aceleracion <8:
                    self.aceleracion = 8

            self.estado = 4
            self.saltar = False
            self.cooldown4 = pygame.time.get_ticks()

        elif self.estado == 4 and self.stun == False and self.tiempo - self.cooldown4 > 400:
            self.estado = 2



        else:
            self.direccion.x = 0

       # print(abs(abs(self.player.sprite.rect.x) - abs(self.rect.x))/16)





            




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

                            #i.direccion.y += self.direccion.y
                            i.direccion.y += self.direccion.y 
                            self.direccion.y = 0 




                            




                            
                    elif self.direccion.y > 0:

                            self.rect.bottom = i.rect.top

                            self.direccion.y =0
                            if i.saltar == True:

                                self.saltar = True










                            #self.inenemy = True


        if self.rect.bottom - i.rect.top == 0:
            self.direccionen = i.direccion.x 
            self.inenemy = True
            #print("jjj")

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


                    elif (self.direccion.x*self.velocidad)+round(self.aceleracion) == 0 and self.inenemy == True:
                        pass





 

        for i in self.enemygr.sprites():
            if self.rect.colliderect(i.rect):
                if self.id != i.id and i.tipo != "bala":
                    print(self.id)
                    #if self.direccion.x< 0:
                         #   self.direccion.x = 1
                            
                            #i.direccion.x = -1
                            #print(abs(abs(self.rect.x) - abs(i.rect.x)) <  abs(abs(self.rect.x) - abs(self.player.sprite.rect.x)) )


                           # self.rect.left = i.rect.right
                            #self.direccion.x = 0

                    if (self.direccion.x*self.velocidad)+round(self.aceleracion) < 0:
                            print("izquierda--------------------------------------------------------------------")
                            self.rect.left = i.rect.right+2
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
                            self.rect.right = i.rect.left-2
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
            self.aceleracion -= 0.2
        if self.aceleracion < 0:
            self.aceleracion += 0.2








        if self.inenemy == True:
            self.velocidadsum = self.velocidadab

        else:
            self.velocidadsum = self.velocidad
        if self.stun <= 0:

            self.rect.x += self.velocidadsum* self.direccion.x
        if self.stun > 0:
            self.stun-= 1
            self.direccion.x = 0
        if self.aceleracion > 10 and self.salto == False:
            self.aceleracion = 10

        if self.aceleracion  < -10 and self.salto == False:
            self.aceleracion =-10

        if self.aceleracion > 20 and self.salto == True:
            self.aceleracion = 20
        
        if self.aceleracion  < -20 and self.salto == True:
            self.aceleracion =-20




        self.rect.x += round(self.aceleracion)
   
        self.collitionsx()
        if self.direccion.x == 1:
            self.mirando = 1
        if self.direccion.x == -1:
            self.mirando = -1 


        self.sumas()
        self.collitionsy()