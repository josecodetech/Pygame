#importamos modulos necesarios
import pygame,sys
from pygame.locals import *
from random import randint
#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Colision")
#colores
colorFondo=(155,110,190)
colorRectangulo1=(255,255,255)
colorRectangulo2=(255,55,0)
#variables
velocidad=10
posX,posY=randint(1,400),randint(1,300)
#rectangulos
rectangulo1=pygame.Rect(5,10,70,40)
rectangulo2=pygame.Rect(posX,posY,70,40)
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    #dibujamos rectangulo
    pygame.draw.rect(ventana,colorRectangulo1,rectangulo1)
    pygame.draw.rect(ventana,colorRectangulo2,rectangulo2)
    #comprobamos movimiento con raton
    posX,posY=pygame.mouse.get_pos()
    rectangulo1.left=posX-35
    rectangulo1.top=posY-20
    if rectangulo1.colliderect(rectangulo2):
        print("Colision")
        posX,posY=randint(1,400),randint(1,300)
        rectangulo2.left=posX-35
        rectangulo2.top=posY-20
    if posX<0:
        posX=0
    elif posX>430:
        posX=430
    elif posY<0:
        posY=0
    elif posY>360:
        posY=360
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
    

