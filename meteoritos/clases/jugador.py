import pygame
from clases import disparo


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes/nave.png")
        self.imagenExplota = pygame.image.load("imagenes/naveExplota.png")
        # tomamos rectangulo imagen
        self.rect = self.imagenNave.get_rect()
        # posicion inicial nave
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocidad = 10
        self.vida = True
        self.listaDisparo = []
        self.sonidoDisparo = pygame.mixer.Sound("sonidos/disparo.aiff")

    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 490:
                self.rect.right = 490

    def disparar(self, x, y):
        if self.vida == True:
            #print("Estoy disparando")
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()

    def dibujar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenExplota, self.rect)
