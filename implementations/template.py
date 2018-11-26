#!/usr/bin/env python
# -*- coding: utf-8 -*-

# esqueleto para projetos em pygame
import pygame
from pygame.locals import *

# definindo o nome do jogo
GAME_NAME = "Template do Projeto - Minicurso de Pygame"

# definindo tamanho para a tela
WIDTH = 480
HEIGHT = 600

# taxa de FPS em que o programa será atulizado
FPS = 30

# definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    # TODO iniciar o jogo

    def __init__(self):
        pygame.init() # inicia pygame
        pygame.mixer.init() # inicia mixer (sons do pygame)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)

        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
    
    # manipula os eventos
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # atualizações do jogo
    def update(self):
        self.all_sprites.update()

    # desenhar / renderizar no jogo
    def draw(self):
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    # loop principal do jogo
    def loop(self):
        while self.running:
            self.clock.tick(FPS)

            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()

def main():
    game = Game()
    game.loop()

if __name__ == "__main__":
    main()