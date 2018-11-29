import pygame
import os
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, bg_path, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bg_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speedx = 0
        self.speedy = 0
    
    def set_speed_x(self, speed_x):
        self.speedx = speed_x
    
    def set_speed_y(self, speed_y):
        self.speedy = speed_y
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.set_speed_x(0)
        self.set_speed_y(0)