import pygame, random, math
from ajustes import *
from claseboton import *
from hitbox import *
from bala import *
from culo import*
from golpe import*
from enemigo1 import*
from dibujarlinea import*
from hitbox2 import *
from particula import *
from pilar import *
from enemigo2 import *
from enemigo3 import*
from cursor import *
from golpee import *
from camara import *
from player import*




class Player(pygame.sprite.Sprite):
    def __init__(self,posh, colisiones, enemigos, pos):
        super().__init__()
        self.aa = 0
        self.numfra = 0
        self.image = pygame.Surface((50, 70))
        self.rect = self.image.get_rect()
        self.da = ""
        self.partcol = 0
        self.rect.center = pos
        self.image.fill((255,200,100))
        #self.sprites = (pygame.image.load("spriteiniti.png"), pygame.image.load("spriteinit.png"))
        
        self.typi = "player"
        #self.image = self.sprites[1]
        self.mano = 0
        self.aceleracion = 0
        self.soltos = True
        self.tilin = []
        self.partsalto = False
        self.s = 0
        self.cooldowncol = 0
        self.ultimosuelo = 0
        self.col = 0
        self.offset = 0
        self.dashcay = False
        self.cooldownb = 0
        self.pue = ""
        self.gravedadre = 3000
        self.cooldowngolpe = 0
        self.invulnerable = False
        self.tiempos = 0
        self.partcolsalt = 0
        self.tiempoe = 0
        self.soltoe = True
        self.poder = False
       # self.dibujo = Dibujo(self.rect.center, (50,70), (pygame.image.load("spriteinit.png")))

        allsprites.add(self)


       
        self.rect.topleft = posh
        self.colisiones = colisiones
        self.tocosuelo = False
        self.cooldownbl = 0
        self.soltotecla = True
        self.tiempo = pygame.time.get_ticks()
        self.direccion = pygame.Vector2()
        self.tint = 0
        self.c = 0
        self.gravedad = 3000
        self.esquivecooldown = 0
        self.saltoahor = False
        self.vida = 20
        self.intento = 0
        self.velocidad = 500
        self.ss = 0
        self.tiempoe = 0
        self.enemigos = enemigos
        self.puedem = True
        self.w = 0
        self.invulnerablesq = False
        self.saltoinit = -200
        self.saltosex = 20
        self.puede = False
        self.mochila = [""]
        self.m = 11100000000000000000000
        self.ataquecol = 0

        self.mirando = 1
        self.tipoo = 0






        #ataquesm

        self.mcombstag = 0
        
        self.mlist = (((

            #

            (50, (80,90), -6, 6, 10, 0, (self.rect.width/2, 40),0), 
            (50, (100,90), -8,6, 5, 0, (self.rect.width/2, 40),0),
            (50, (120,90), -8,12, 0, 100, (self.rect.width/2 , 40),0),
            (50, (120,60), -8,12, 0, 100, (self.rect.width/2 , 40),0),
            (10, (80,60), 8,0, 0, 0, (0 , -40), -1200)





            )))
        self.cooldowncombo = 0 

        spritesvisibles.add(self)
        spritesupdate.add(self)
        playergrup.add(self)

    def input(self):
        for i in objgrup.sprites():
            if self.rect.colliderect(i.rect):
                if len(self.mochila) < 3:
                    self.mochila.append(i.content)
                    i.kill()
                else:
                    pass

        self.tilin = abs(self.direccion.x*self.velocidad*dt + abs(self.aceleracion))
        #print(self.tilin)

        keys = pygame.key.get_pressed()

        if self.invulnerablesq == False:
            self.direccion.x = keys[pygame.K_d] - keys[pygame.K_a]

        if self.direccion.x == 1:
            self.mirando = 1
        if self.direccion.x == -1:
            self.mirando = -1

        

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.m = pygame.time.get_ticks()




        if keys[pygame.K_e] and self.puedee == True and self.soltoe == True:
            if self.mano != len(self.mochila)-1:
                self.mano+=1
            else:
                self.mano = 0


        if keys[pygame.K_s] :
            self.tiempos = pygame.time.get_ticks()


        if keys[pygame.K_s] and self.puedes == True and self.soltos == True:

            self.ss += 1
            self.puedes = False
            self.soltos = False
            self.c = pygame.time.get_ticks()
            if self.ss >= 2:
                self.direccion.y = 2500
                self.aceleracion = 0
                self.direccion.x = 0
                self.dashcay = True
                self.ss = 0
                print("pñssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssdsdsdsdsfsfsfsfsfsfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdffdfdfdfdfdfdfd")

        if self.tiempo - self.c > 200:
            self.ss = 0

        print(self.ss)





        if keys[pygame.K_e]:
            self.tiempoe = pygame.time.get_ticks()

 

        if keys[pygame.K_a] and keys[pygame.K_d] or not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direccion.x = 0

        if self.tiempo - self.cooldowncombo > 450:
            self.mcombstag = 0

        if self.mochila[self.mano] =="":


            if keys[pygame.K_LEFT] and self.tiempo - self.ataquecol > 50 and self.puedem == True or keys[pygame.K_DOWN] and self.tiempo - self.ataquecol > 200 and self.puedem == True or keys[pygame.K_RIGHT] and self.tiempo - self.ataquecol > 50 and self.puedem == True or keys[pygame.K_UP] and self.tiempo - self.ataquecol > 200 and self.puedem == True:

                    


                        

                    if keys[pygame.K_LEFT]:


                        

                        golpe((self.rect.center[0]+ self.mlist[self.mcombstag][6][0]*-1+  self.mlist[self.mcombstag][1][0] *-1, self.rect.center[1] - 40), self, enemigrup, self.mlist[self.mcombstag][0], self.mlist[self.mcombstag][1], self.mlist[self.mcombstag][2], self.mlist[self.mcombstag][3]+self.tilin, self.mlist[self.mcombstag][4], self.mlist[self.mcombstag][5], -1,self.mlist[self.mcombstag][7])




                    elif keys[pygame.K_RIGHT]:
     
                            golpe((self.rect.center[0]+ self.mlist[self.mcombstag][6][0] + self.mlist[self.mcombstag][1][0] *1, self.rect.center[1] - 40), self, enemigrup, self.mlist[self.mcombstag][0], self.mlist[self.mcombstag][1], self.mlist[self.mcombstag][2], self.mlist[self.mcombstag][3]+self.tilin, self.mlist[self.mcombstag][4], self.mlist[self.mcombstag][5], 1,self.mlist[self.mcombstag][7])

                    elif keys[pygame.K_DOWN] :
                            self.mcombstag = 4

                            golpe((self.rect.center[0]+ 0 + self.mlist[self.mcombstag][1][0] *1, self.rect.center[1] - 400), self, enemigrup, self.mlist[self.mcombstag][0], self.mlist[self.mcombstag][1], self.mlist[self.mcombstag][2], self.mlist[self.mcombstag][3]+self.tilin, self.mlist[self.mcombstag][4], self.mlist[self.mcombstag][5],3, self.mlist[self.mcombstag][7])
                            self.mcombstag = 0
                        




                    
                    if self.mcombstag == 2:
                            self.ataquecol = pygame.time.get_ticks()+500
                    else:
                            self.ataquecol = pygame.time.get_ticks()

                    self.mcombstag += 1
                    self.cooldowncombo = pygame.time.get_ticks()



        elif self.mochila[self.mano] =="B":
            a = 0

            if keys[pygame.K_RIGHT] and self.tiempo - self.cooldownbl > 400 or keys[pygame.K_LEFT] and self.tiempo - self.cooldownbl > 400 or keys[pygame.K_UP] and self.tiempo - self.cooldownbl > 400 or keys[pygame.K_DOWN] and self.tiempo - self.cooldownb > 600:
                
                if keys[pygame.K_RIGHT] and self.tiempo - self.cooldownbl > 400:
                    
                    a = Hitbox2(1, (self.rect.center[0]+80,self.rect.y+40), (40,60),pygame.image.load("tierra.png"), "P", (40,40), 600)
                    self.cooldownbl = pygame.time.get_ticks()

                elif keys[pygame.K_LEFT] and self.tiempo - self.cooldownbl > 400:
                    a = Hitbox2(1, (self.rect.center[0]-80,self.rect.y+40), (40,60),pygame.image.load("tierra.png"), "P", (40,40), 600)
                    self.cooldownbl = pygame.time.get_ticks()

                elif keys[pygame.K_UP] and self.tiempo - self.cooldownbl > 400:
                    a = Hitbox2(1, (self.rect.center[0],self.rect.y-40), (80,40),pygame.image.load("tierra.png"), "P", (40,40), 1200)
                    self.cooldownbl = pygame.time.get_ticks()

                elif keys[pygame.K_DOWN] and self.tiempo - self.cooldownb > 600:

                    a = Hitbox2(1, (self.rect.center[0],self.rect.y+120), (40,40),pygame.image.load("tierra.png"), "P", (40,40), 100)
                    self.cooldownb = pygame.time.get_ticks()
                if a != 0: 
                    for i in self.colisiones.sprites():
                        if a.rect.colliderect(i.rect) and i.id != a.id:
                            a.kill()
                            #a.dibujo.kill()








        if self.mcombstag == 3:
            self.mcombstag = 0






            

            #self.ataquecol = pygame.time.get_ticks()



        

        # Almacenar el tiempo en que se presiona 'W'
        if keys[pygame.K_w]:
            self.w = pygame.time.get_ticks()

        # Permitir salto con coyote time
        if self.soltotecla and self.tiempo - self.tocosuelo < 100 and keys[pygame.K_w] and self.puede:
            self.partsalto = True
            #self.direccion.y += self.saltoinit
            self.direccion.y += -500
            self.tocosuelo = False
            #self.aceleracion = 6
            self.soltotecla = False
            self.saltoahor = True
            #print("xulo")

        if keys[pygame.K_SPACE]  and self.tiempo - self.esquivecooldown > 1200:
                self.aceleracion = 0
                self.aceleracion = 20 * self.mirando

                self.invulnerablesq = True 
                print("uwu")
                self.esquivecooldown = pygame.time.get_ticks()
                self.gravedad = 1000


        if self.tiempo - self.esquivecooldown > 200 and self.invulnerablesq == True :
            self.invulnerablesq = False
            self.aceleracion = 0
            self.gravedad = self.gravedadre


        if self.partsalto == True and self.direccion.y > -5:
            self.col = 0
            self.partsalto = False

        if self.partsalto== True and self.tiempo - self.partcolsalt > 30:
                self.col += 1

                tam = (10,10)
                tam2 = (20,10)
                self.partcolsalt = pygame.time.get_ticks()
                particula(tam, (200,200,200), 0, 9, 0, 600, False, False, (self.rect.center[0], self.rect.center[1]+(40+(tam[1]/2-tam[1])) ), 0)
                if self.col == 1:
                    particula(tam2, (200,200,200), 1, 9, 0, 200, False, False, (self.rect.center[0], self.rect.center[1]+(34+(tam[1]/2-tam[1])) ), 0)
                    particula(tam2, (200,200,200), -1, 9, 0, 200, False, False, (self.rect.center[0], self.rect.center[1]+(34+(tam[1]/2-tam[1])) ), 0)




  

 







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

        if self.tiempo - self.s > 1:
            self.puedes = True
        else:
            self.puedem = False


        if self.tiempo - self.tiempoe > 1:
            self.puedee = True
        else:
            self.puedee = False




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
                        self.tint+= 1
                        if self.tint== 1:
                            tam = (15,15)



                            particula(tam, (200,200,200), 1, 1, 0.4, 1000, False, False, (self.rect.center[0]+(25+(tam[0]/2))*1, self.rect.center[1]+(20+(tam[1]/2-tam[1])) ), -6)
                            particula(tam, (200,200,200), 1, -1, 0.4, 1000, False, False, (self.rect.center[0]+(25+(tam[0]/2))*-1, self.rect.center[1]+(20+(tam[1]/2-tam[1])) ), -6)
                        self.direccion.y = 0
                        self.rect.bottom = i.rect.top
                        self.dashcay = False
                        self.tocosuelo = pygame.time.get_ticks()
                        self.saltosex = 15
                        if i.tipo == "A" or i.tipo == "sierra":
                                self.direccion.y = -1000
                                self.aceleracion = 20* random.choice((1, -1))
                        if self.intento != 0:
                            self.partsalto = True
                            #self.direccion.y += self.saltoinit
                            self.direccion.y += -500
                            self.tocosuelo = False
                            self.soltotecla = False
                            self.saltoahor = True
                            #print("Intento de salto")




                    elif self.direccion.y < 0 :
                        self.direccion.y /= 4
                        self.direccion.y *=-1
                        
                        self.rect.top = i.rect.bottom
                        self.saltoahor = False

                        


    def enemigoss(self):



        for i in self.enemigos.sprites():

            if i.atravesable == False:

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
                    if i.tipo != "sierra":

                
                        if (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) < 0:


                                self.rect.left = i.rect.right
                                self.direccion.x = 0

                                #print(i.rect.x)

                                
                                #print("izquierda--------------------------------------------------------------------")



                                self.aceleracion = self.aceleracion/1.6
                                self.aceleracion *= -1
                                self.poder = False
                                self.pue = "D"
                                if i.tipo == "A":
                                    self.direccion.y = -1000
                                    self.aceleracion = 20
                                #print(self.rect.left == i.rect.right)
                                #print(i.rect.x)
                                
                                #print(f"velocidad: {self.velocidad*dt}, friccion: {self.aceleracion},")

           
              
                            


                        elif (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) > 0:




                                self.rect.right = i.rect.left
                            
                                self.direccion.x = 0
                                self.poder = False

                                
                                self.aceleracion = self.aceleracion/1.6
                                #print(i.rect.x)

         
                                self.aceleracion *= -1
                                #print("derecha---------------------------------------------------------------------")

                                #print(self.rect.right == i.rect.left)
                                
                                #if self.rect.colliderect(i.rect):
                                   # print("uwu")

                                if i.tipo == "A":
                                    self.direccion.y = -1000
                                    self.aceleracion = -20

                                #print(f"velocidad: {self.velocidad*dt}, friccion: {self.aceleracion},")

                    if i.tipo == "sierra":
                        
                        if (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) != 0:

                            if (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) < 0 and i.direccion.x  < 0 or (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) < 0 and i.direccion.x  > 0:
                                self.rect.left = i.rect.right


                                self.aceleracion = 20
                                print("1")






                            elif (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) > 0 and i.direccion.x > 0 or (self.direccion.x*self.velocidad*dt)+round(self.aceleracion) > 0 and i.direccion.x  < 0:
                                 self.rect.right = i.rect.left
                                 self.aceleracion = -20

 




                        else:
                            if i.direccion.x > 0:

                                self.rect.left = i.rect.right
                                self.aceleracion = 10

                            else:
                                self.rect.right = i.rect.left
                                self.aceleracion = -10


           







                                
                                
                                






                        

                        



                        

        if self.poder == True:

           # if self.direccion.x ==1 :


                #if self.aceleracion < 15 :
                self.aceleracion += self.direccion.x/2.5
                    
            #elif self.direccion.x ==-1 :

               # if self.aceleracion >  -15:

                  #  self.aceleracion += self.direccion.x/2

    def sumas(self):
        self.direccion.y += self.gravedad * dt
        self.rect.y += self.direccion.y * dt




    def update(self):
        keys = pygame.key.get_pressed()
        if abs(self.direccion.y )> 2:
            self.tint = 0



        self.tiempo = pygame.time.get_ticks()
        self.input()

        if self.dashcay == True:
            self.aceleracion = 0
            self.direccion.x =0

        if self.direccion.x  != 0 and self.tiempo - self.partcol > 150 and self.direccion.y == 0 and ((self.direccion.x*self.velocidad*dt)+round(self.aceleracion)) != 0:

            self.partcol = pygame.time.get_ticks()
            tam = (25,25)
            directot = ((self.direccion.x*self.velocidad*dt)+round(self.aceleracion))/abs(((self.direccion.x*self.velocidad*dt)+round(self.aceleracion)))+0.1
            print(directot)
            particula(tam, (200,200,200), abs(directot), directot*-1, 0.4, 1000, False, False, (self.rect.center[0]+(25+(tam[0]/2))*(directot*-1), self.rect.center[1]+(34+(tam[1]/2-tam[1])) ), -3)


        self.rect.x += self.direccion.x * self.velocidad* dt


        
         #(self.direccion.x * velocidad) - self.aceleracion

        

        if  not keys[pygame.K_d] and not  keys[pygame.K_a] or keys[pygame.K_d] and  keys[pygame.K_a] or self.direccion.x == 0  or self.poder == False: 
            if self.aceleracion > 0:
                self.aceleracion -= 0.2
            if self.aceleracion < 0:
                self.aceleracion += 0.2



            if self.aceleracion <-15  and self.invulnerablesq == False:
                    
                    self.aceleracion = -15


            if self.aceleracion >  15 and self.invulnerablesq == False:

                    self.aceleracion  = 15

        #bprint(self.rect.x, self.aceleracion)
 
        self.rect.x += round(self.aceleracion)
        #print(self.saltoinit)




        




        self.enemigoss()
        self.collitionsx()
        
        self.sumas()
        self.collitionsy()






        



      #  self.dibujo.rect.center = self.rect.center

        if self.mirando == 1:
            pass
            #self.image = self.sprites[1]
        elif self.mirando== -1:
            pass
            #self.image = self.sprites[0]

        if self.mochila[self.mano] =="B" and self.da == "":
            self.da = Dibujo((self.rect.center), (20,20), "")
        if self.mochila[self.mano] =="B":
            self.da.rect.center = (self.rect.center[0], self.rect.center[1]+40)

        if self.da != "" and self.mochila[self.mano] !="B":
            self.da.kill()
            self.da = ""



        self.numfra +=1
        print(f"frame: {self.numfra}")
        self.offsetx = screen.get_width()/2 - self.rect.x
        self.offsety = screen.get_height()/2 - self.rect.y