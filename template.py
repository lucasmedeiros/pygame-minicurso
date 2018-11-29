#!/bin/usr/env python
# -*- coding: utf-8 -*-
import pygame as pg

GAME_NAME = "Template básico - minicurso de PyGame"

WIDTH = 480
HEIGHT = 600

FPS = 30

#definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:

    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(GAME_NAME)

        self.running = True
        self.win = False

        self.all_sprites = pg.sprite.Group()

        self.clock = pg.time.Clock()

    def handle_events(self):
        for event in pg.event.get():
            event_type = event.type

            if event_type == pg.QUIT:
                self.running = False
            
            if event_type == pg.KEYDOWN:
                key = event.key

                if key == pg.K_ESCAPE:
                    self.running = False
    
    def update(self):
        pg.display.update()
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill(WHITE)[
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        
    
    def loop(self):
        
        while self.running:
            self.clock.tick(FPS)

            self.handle_events()
            self.update()
            self.draw()

    def run(self):

        self.loop()


def main():
    game = Game()
    game.run()
    pg.quit()

if __name__ == "__main__":
    main()