import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Movimiento Teclas")
colorFondo = (1, 150, 70)
colorFigura = (255, 255, 255)
# variables
velocidad = 15
direccion = True
posX, posY = randint(1, 400), randint(1, 300)

while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana, colorFigura, (posX, posY, 40, 40))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        # detectar pulsacion teclas para mover la figura
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:
                posX -= velocidad
                if posX < 0:
                    posX = 0
            elif evento.key == K_RIGHT:
                posX += velocidad
                if posX > (500-40):
                    posX = 500-40
            elif evento.key == K_UP:
                posY -= velocidad
                if posY < 0:
                    posY = 0
            elif evento.key == K_DOWN:
                posY += velocidad
                if posY > (400-40):
                    posY = 400-40
    pygame.display.update()
 
