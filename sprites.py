#!/bin/usr/env python
# -*- coding: utf-8 -*-

WIDTH = 20
HEIGHT = 20

import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, bg_color, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(bg_color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speedx = 0
    
    def set_speedx(self, speed):
        self.speedx = speed

    def update(self):
        self.rect.x += self.speedx

