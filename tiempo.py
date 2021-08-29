import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Textos")
colorFondo = (1, 150, 70)
colorCuadro01 = (255, 255, 0)
colorCuadro02 = (0, 255, 255)
colorTexto = (255, 255, 255)
# variables
velocidad = 15
direccion = True
posX01, posY01 = randint(1, 400), randint(1, 300)
posX02, posY02 = randint(1, 400), randint(1, 300)
lado = 40
cadena = "Tiempo"
tamaño = 40
tipoFuente = "Impact"
# preparacion de fuente / texto
fuente = pygame.font.SysFont(tipoFuente, tamaño)
texto = fuente.render(cadena, True, colorTexto)
while True:
    ventana.fill(colorFondo)
    # mostrar texto
    ventana.blit(texto, (10, 10))
    # tiempo
    tiempo = pygame.time.get_ticks() / 1000
    cadena = "Tiempo: "+str(tiempo)
    texto = fuente.render(cadena, True, colorTexto)
    cuadro01 = pygame.draw.rect(
        ventana, colorCuadro01, (posX01, posY01, lado, lado))
    cuadro02 = pygame.draw.rect(
        ventana, colorCuadro02, (posX02, posY02, lado, lado))
    # detecta colision
    if cuadro01.colliderect(cuadro02):
        #print(f"Colision!!! en coordenada {posX01} : {posY01}")
        #cadena = f"Colision!!! en coordenada {posX01} : {posY01}"
        #texto = fuente.render(cadena, True, colorTexto)
        posX02, posY02 = randint(1, 400), randint(1, 300)
        cuadro02.left = posX02-(lado/2)
        cuadro02.top = posY02-(lado/2)
    # detecta movimiento raton
    posX01, posY01 = pygame.mouse.get_pos()
    cuadro01.left = posX01 - (lado / 2)
    cuadro01.top = posY01 - (lado / 2)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
