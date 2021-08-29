import pygame
import sys
from pygame.locals import *

# variables
ANCHO = 480
ALTO = 700

# funcion principal


def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # imagen de fondo
    fondo = pygame.image.load("imagenes/fondo.png")
    ventana.blit(fondo, (0, 0))
    # titulo
    pygame.display.set_caption("Meteoritos")
    # ciclo del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


# llamada a funcion principal
meteoritos()
