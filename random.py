#importamos modulos necesarios
import pygame,sys
from pygame.locals import *
from random import randint
#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Rectangulos")
#color de fondo
colorFondo=(155,110,190)
colorRectangulo=(10,170,90)

#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    for i in range(5):
        posX,posY=randint(1,400),randint(1,300)
        pygame.draw.rect(ventana,colorRectangulo,(posX,posY,70,40))
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
    

