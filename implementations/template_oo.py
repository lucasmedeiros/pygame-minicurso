#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Template ou "esqueleto" básico para um projeto com Pygame trabalhando com OO.
import pygame
from pygame.locals import *

# declaração de constantes
GAME_NAME = "MODELO DE TEMPLATE - MINICURSO DE PYGAME"

# definindo tamanho para a tela
WIDTH = 800
HEIGHT = 600

# definindo velocidade para o loop principal do jogo
FPS = 30

#definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    screen = None
    screen_size = None
    background = None
    clock = None
    running = True
    all_sprites = None

    def __init__(self, name, size, bg):
        pygame.init()
        pygame.mixer.init()
        self.screen_size = size
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.background = bg
        self.all_sprites = pygame.sprite.Group()
    
    # processar entrada (eventos)
    def handle_events(self):
        for event in pygame.event.get():
            event_type = event.type

            if event_type in (pygame.KEYDOWN, pygame.KEYUP):
                key = event.key

            if event_type == pygame.QUIT:
                self.running = False
            
            if event_type == pygame.KEYDOWN:
                if key == pygame.K_ESCAPE:
                    self.running = False
    
    # atualizar informações do jogo
    def update(self):
        self.all_sprites.update()
    
    # desenhar e renderizar
    def draw(self):
        self.screen.fill(self.background)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    
    # laço principal do jogo.
    def loop(self, fps):
        while self.running:
            self.clock.tick(fps)
            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()

def main():
    game = Game(GAME_NAME,(WIDTH, HEIGHT), WHITE)
    game.loop(30)

if __name__ == "__main__":
    main()