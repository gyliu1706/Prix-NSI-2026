import pygame
from camera import camera

sprites = []
loaded = {}

class Sprite:
    def __init__(self, image, posX, posY):
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image)
            loaded[image] = self.image
        self.posX = posX
        self.posY = posY
        sprites.append(self)

    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.posX - camera.x, self.posY - camera.y))






