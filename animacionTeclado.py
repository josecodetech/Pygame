#importamos modulos necesarios
import pygame,sys
from pygame.locals import *
from random import randint
#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Animacion - Teclas")
#colores
colorFondo=(155,110,190)
colorRectangulo=(255,255,255)
#variables
velocidad=10
posX,posY=randint(1,400),randint(1,300)
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    #dibujamos rectangulo
    pygame.draw.rect(ventana,colorRectangulo,(posX,posY,70,40))
    #bucle comprueba eventos
    for evento in pygame.event.get():
        #comprobamos evento para salir
        if evento.type==QUIT:
            #detiene modulos
            pygame.quit()
            #cierra ventana
            sys.exit()
        #comprobamos tecla pulsada
        elif evento.type==pygame.KEYDOWN:
            if evento.key==K_LEFT:
                posX-=velocidad
                if posX<0:
                    posX=0
            elif evento.key==K_RIGHT:
                posX+=velocidad
                if posX>(500-70):
                    posX=500-70
            elif evento.key==K_UP:
                posY-=velocidad
                if posY<0:
                    posY=0
            elif evento.key==K_DOWN:
                posY+=velocidad
                if posY>360:
                    posY=360
    #actualiza ventana
    pygame.display.update()
    

