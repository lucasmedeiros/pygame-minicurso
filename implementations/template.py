#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Template ou "esqueleto" básico para um projeto com Pygame trabalhando com OO.
import pygame
from pygame.locals import *

class Game:
    screen = None
    screen_size = None
    background = None
    clock = None
    running = True

    def __init__(self, name, size, bg):
        pygame.init()
        pygame.mixer.init()

        self.screen_size = size
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.background = bg
    
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
        # TODO ainda não implementado
        pass
    
    # desenhar e renderizar
    def draw(self):
        self.screen.fill(self.background)
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
    game = Game("MODELO DE TEMPLATE- MINICURSO PYGAME",(800, 600), (255, 255, 255))
    game.loop(30)

if __name__ == "__main__":
    main()