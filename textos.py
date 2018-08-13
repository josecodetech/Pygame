#importamos modulos necesarios
import pygame,sys
from pygame.locals import *
#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Textos")
#colores
colorFondo=(155,250,190)
colorTexto=(10,150,255)
#textos
fuente=pygame.font.SysFont('Arial',30)
texto=fuente.render("Texto",0,colorTexto)
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    #mostramos texto
    ventana.blit(texto,(120,120))
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
    

