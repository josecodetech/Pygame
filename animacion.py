#importamos modulos necesarios
import pygame,sys
from pygame.locals import *
from random import randint
#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Animacion")
#colores
colorFondo=(155,110,190)
colorRectangulo=(255,255,255)
#variables
velocidad=2
direccion=True
posX,posY=randint(1,400),randint(1,300)
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    #dibujamos rectangulo
    pygame.draw.rect(ventana,colorRectangulo,(posX,posY,70,40))
    #algoritmo para rebote
    if direccion==True:
        if posX<(500-70):
            posX+=velocidad
        else:
            direccion=False
    else:
        if posX>1:
            posX-=velocidad
        else:
            direccion=True
    #bucle comprueba eventos
    for evento in pygame.event.get():
        #comprobamos evento para salir
        if evento.type==QUIT:
            #detiene modulos
            pygame.quit()
            #cierra ventana
            sys.exit()
    #actualiza ventana
    pygame.display.update()
    

