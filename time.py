#importamos modulos necesarios
import pygame,sys
from pygame.locals import *
#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Tiempo")
#colores
colorFondo=(155,250,190)
colorTexto=(10,150,255)
#fuente
fuente=pygame.font.SysFont('Arial',30)
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    #tiempo 
    tiempo=pygame.time.get_ticks()/1000
    texto=fuente.render("Tiempo: "+str(tiempo),0,colorTexto)
    #mostramos texto con el tiempo
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
    

