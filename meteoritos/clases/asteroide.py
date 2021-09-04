import pygame


class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenAsteroide = pygame.image.load("imagenes/asteroide.png")
        self.rect = self.imagenAsteroide.get_rect()
        self.velocidad = 5
        self.rect.top = posY
        self.rect.left = posX
        self.listaAsteroide = []

    def recorrido(self):
        self.rect.top = self.rect.top + self.velocidad

    def dibujar(self, superficie):
        superficie.blit(self.imagenAsteroide, self.rect)
