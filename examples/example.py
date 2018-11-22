import pygame, random
from pygame.locals import *

LARGURA = 400
ALTURA = 300

def main():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Minicurso Pygame")
    
    sair = False
    cor_branca = (255, 255, 255)
    clock = pygame.time.Clock()

    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        
        tela.fill(cor_branca)

        pygame.display.update()
        clock.tick(25)

    pygame.quit()

main()