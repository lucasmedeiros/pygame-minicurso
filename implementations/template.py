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

# definição taxa de FPS em que o programa será atulizado
FPS = 30

# definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    """
        classe usada para representar o jogo e todas as suas funcionalidades

        Attributes
        ----------
        screen : pygame.Surface
            uma superfície para a tela principal do jogo
        running : bool
            valor que representa se o loop está rodando ou não
        all_sprites : pygame.sprite.Group
            grupo de sprites utilizados no jogo.
    """

    def __init__(self):
        pygame.init() # inicia pygame
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)

        self.running = True
        self.all_sprites = pygame.sprite.Group()
    
    def handle_events(self):
        """
            handle_events() -> None gerencia os eventos do jogo
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """
            update() -> None atualiza todas as informações do jogo
        """
        self.all_sprites.update()
        pygame.display.update()

    def draw(self):
        """
            draw() -> None desenha todos os sprites na tela
        """
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def loop(self):
        """
            loop() -> None roda o loop principal do jogo
        """

        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)

            self.handle_events()
            self.update()
            self.draw()
    
    def run(self):
        # TODO coisas para fazer antes do loop iniciar

        self.loop()

        # TODO coisas para fazer depois que o loop acabar

        pygame.quit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()