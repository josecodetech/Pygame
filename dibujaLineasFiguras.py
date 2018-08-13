#plantilla pygame
#importamos modulos necesarios
import pygame,sys
from pygame.locals import *

#colocamos init antes de usar algun modulo pygame
pygame.init()
#declaramos ventana con tupla ancho alto
ventana=pygame.display.set_mode((500,400))
#le damos un titulo
pygame.display.set_caption("Lineas y figuras")
#color de fondo
colorFondo=(1,150,70)
colorLinea=(240,92,103)
colorCirculo=(255,50,150)
colorFiguras=(210,170,30)
#se ejecutara mientras no sea falso
while True:
    #damos color de fondo a la ventana
    ventana.fill(colorFondo)
    #dibujo de lineas
    pygame.draw.line(ventana,colorLinea,(30,20),(140,100),20)
    pygame.draw.line(ventana,colorLinea,(140,100),(200,80),20)
    pygame.draw.line(ventana,colorLinea,(200,80),(260,180),20)
    #dibuja circulo dando coordenada y racio
    pygame.draw.circle(ventana,colorCirculo,(270,90),40)
    #dibuja rectangulo dando su esq superior izq el ancho y alto
    pygame.draw.rect(ventana,colorFiguras,(220,220,100,80))
    #poligono dando los puntos de union
    pygame.draw.polygon(ventana,colorFiguras,((100,90),(140,160),(60,90),(160,120)))
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
    

