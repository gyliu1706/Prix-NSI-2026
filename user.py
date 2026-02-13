import pygame
from camera import camera
from sprite import Sprite
from detection_fonction import is_key_pressed


speed = 3


class Player(Sprite) :
    def __init__ (self,image,posX,posY,PV,name,classe):
        Sprite.__init__(self,image,posX,posY)
        self.PV = PV
        self.name = name
        self.classe = classe
        

    def presentation(self):
        print(f"Bonjour je suis {self.name} et je suis un {self.classe}.")

    def update(self):
        
        if is_key_pressed(pygame.K_z):
            self.posY -= speed
        if is_key_pressed(pygame.K_s):
            self.posY += speed
        if is_key_pressed(pygame.K_q):
            self.posX -= speed
        if is_key_pressed(pygame.K_d):
            self.posX += speed
        
        camera.x = self.posX - camera.width/2 + self.image.get_width()/2
        camera.y = self.posY - camera.height/2 + self.image.get_height()/2

# asset/sprite/MainCharacter.png