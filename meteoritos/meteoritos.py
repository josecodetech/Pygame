import pygame,sys
from pygame.locals import *
#importamos de nuestras clases
from clases import jugador
from clases import asteroide
from random import randint
from time import clock
#variables
ANCHO=480
ALTO=700
listaAsteroide=[]
colorFuente=(120,200,40)
posX=0
posY=0
puntos=0
#booleano juego
global jugando
jugando=True

#funcion carga asteroides
def cargarAsteroides(x,y):
    meteoro=asteroide.Asteroide(x,y)
    listaAsteroide.append(meteoro)
#funcion fin de juego
def gameOver():
    global jugando
    jugando=False
    for meteoro in listaAsteroide:
        listaAsteroide.remove(meteoro)
#funcion principal
def Meteoritos():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    #sonido colision
    sonidoColision=pygame.mixer.Sound("sonidos/colision.aiff")
    #imagen de fondo
    fondo=pygame.image.load('imagenes/fondo.png')    
    #titulo del juego
    pygame.display.set_caption("Meteoritos")
    #crea objeto jugador
    nave=jugador.Nave()
    contador=0
    puntos=0
    #fuente marcador
    FuenteMarcador=pygame.font.SysFont("Arial",10)
    #sonido de fondo
    pygame.mixer.music.load("sonidos/fondo.wav")
    pygame.mixer.music.play(3) #3 repeticiones
    #ciclo del juego
    while True: 

        ventana.blit(fondo,(0,0))
        nave.dibujar(ventana) 
        #Marcador        
        TextoMarcador=FuenteMarcador.render("Puntos: "+str(puntos),0,colorFuente)
        ventana.blit(TextoMarcador,(0,0))
            #tiempo y coordenada azar asteroide
        tiempo = clock()
            #creamos asteroides cada segundo en pos azar
        if tiempo-contador > 1:
            contador=tiempo
            posX=randint(2,478)
            cargarAsteroides(posX,posY)
                #comprobamos lista asteroide
        if len(listaAsteroide)>0:
            for x in listaAsteroide:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top>700:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaAsteroide.remove(x)
                        sonidoColision.play()
                        nave.vida=False
                        gameOver()
            #comprobamos lista disparo
        if len(nave.listaDisparo)>0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top<-10:
                    nave.listaDisparo.remove(x)
                        #comprobamos si colisiona con asteroide
                else:
                    for meteoro in listaAsteroide:
                        if x.rect.colliderect(meteoro.rect):
                            sonidoColision.play()
                            puntos+=1
                            listaAsteroide.remove(meteoro)
                            nave.listaDisparo.remove(x)
                            
        nave.mover()
        
        for evento in pygame.event.get():
            if jugando==True:
                #comprobamos evento para salir
                if evento.type==QUIT:
                    #detiene modulos
                    pygame.quit()
                    #cierra ventana
                    sys.exit()
                    #comprobamos tecla pulsada
                elif evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT:                        
                        nave.rect.left-=nave.velocidad                        
                    elif evento.key==K_RIGHT:
                        nave.rect.right+=nave.velocidad
                    elif evento.key==K_SPACE:
                        x,y=nave.rect.center
                        nave.disparar(x,y)   
        if jugando==False:
            FuenteGameOver=pygame.font.SysFont("Arial",40)
            TextoGameOver=FuenteGameOver.render("Fin del juego",0,colorFuente)
            ventana.blit(TextoGameOver,(140,350))
            pygame.mixer.music.fadeout(3000)
            
        pygame.display.update()

#llamada a funcion principal

Meteoritos()
    

