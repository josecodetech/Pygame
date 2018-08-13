#importamos modulos necesarios
import pygame,sys
from pygame.locals import *

#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Carga Imagen")
#color de fondo
colorFondo=(90,110,190)
imagen=pygame.image.load("imagenes/imagen.png")
posX,posY=90,80
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    ventana.blit(imagen,(posX,posY))
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
    

