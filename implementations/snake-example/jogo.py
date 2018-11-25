import sys
import random
import pygame
from pygame.locals import *

COLOR_WHITE = [255, 255, 255]

class Game:
    screen = None
    screen_size = None
    running = True
    background = None

    def __init__(self, size, bg_color):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.screen_size = self.screen.get_size()
        self.background = bg_color

        pygame.mouse.set_visible(0)
    
    def handle_events(self):
        for event in pygame.event.get():
            t = event.type

            if t in (KEYDOWN, KEYUP):
                k = event.key

            if t == pygame.QUIT:
                self.running = False
            
            elif t == pygame.KEYDOWN:
                if k == pygame.K_ESCAPE:
                    self.running = False
            
    def loop(self):
        clock = pygame.time.Clock()
        dt = 16

        while self.running:
            clock.tick(1000 / dt)

            self.handle_events()
            self.screen.fill(COLOR_WHITE)

            pygame.display.update()


def main(argv):
    game = Game((300, 300), COLOR_WHITE)
    game.loop()

if __name__ == "__main__":
    main(sys.argv)