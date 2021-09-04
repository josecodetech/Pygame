import pygame
import sys
from pygame.locals import *
# importar nuestras clases
from clases import jugador
from clases import asteroide
from random import randint
from time import clock
# variables
ANCHO = 480
ALTO = 700
listaAsteroide = []
puntos = 0
colorFuente = (120, 200, 40)
# booleano juego
jugando = True
# funcion principal
# carga asteroides


def cargarAsteroides(x, y):
    meteoro = asteroide.Asteroide(x, y)
    listaAsteroide.append(meteoro)


def gameOver():
    global jugando
    jugando = False
    for meteoritos in listaAsteroide:
        listaAsteroide.remove(meteoritos)


def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # imagen de fondo
    fondo = pygame.image.load("imagenes/fondo.png")
    # titulo
    pygame.display.set_caption("Meteoritos")
    # crea objeto jugador
    nave = jugador.Nave()
    contador = 0
    # sonidos
    pygame.mixer.music.load("sonidos/fondo.wav")
    pygame.mixer.music.play(3)
    sonidoColision = pygame.mixer.Sound("sonidos/colision.aiff")
    # fuente marcador
    fuenteMarcador = pygame.font.SysFont("Arial", 10)
    # ciclo del juego
    while True:

        ventana.blit(fondo, (0, 0))
        nave.dibujar(ventana)
        # tiempo
        tiempo = clock()
        # marcador
        global puntos
        textoMarcador = fuenteMarcador.render(
            "Puntos: "+str(puntos), 0, colorFuente)
        ventana.blit(textoMarcador, (0, 0))
        # creamos asteroides
        if tiempo - contador > 1:
            contador = tiempo
            posX = randint(2, 478)
            cargarAsteroides(posX, 0)

        # comprobamos lista asteroide
        if len(listaAsteroide) > 0:
            for x in listaAsteroide:
                if jugando == True:
                    x.dibujar(ventana)
                    x.recorrido()
                if x.rect.top > 700:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaAsteroide.remove(x)
                        sonidoColision.play()
                        #print("Colision nave / meteorito")
                        nave.vida = False
                        gameOver()

        # Disparo de proyectil
        if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else:
                    for meteoritos in listaAsteroide:
                        if x.rect.colliderect(meteoritos.rect):
                            listaAsteroide.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntos += 1
                            #print("Colision disparo / meteorito")
        nave.mover()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if jugando == True:
                    if evento.key == K_LEFT:
                        nave.rect.left -= nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right += nave.velocidad
                    elif evento.key == K_SPACE:
                        x, y = nave.rect.center
                        nave.disparar(x, y)
        if jugando == False:
            FuenteGameOver = pygame.font.SysFont("Arial", 40)
            textoGameOver = FuenteGameOver.render("Game Over", 0, colorFuente)
            ventana.blit(textoGameOver, (140, 350))
            pygame.mixer.music.fadeout(3000)
        pygame.display.update()


# llamada a funcion principal
meteoritos()
