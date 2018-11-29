#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import subprocess
import os
from sprites import *

GAME_NAME = "Thin Ice"

WIDTH = 380
HEIGHT = 320

FPS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SQUARE_SIZE = 20

SPEED_INCREASE_AMOUNT = 20

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, "Images")
FONTS_FOLDER = os.path.join(GAME_FOLDER, "Fonts")
LEVELS_FOLDER = os.path.join(GAME_FOLDER, "Levels")
SOUNDS_FOLDER = os.path.join(GAME_FOLDER, "Sounds")

LEVEL_NAMES = ["level1", "level2", "level3",
                "level4", "level5", "level6",
                "level7", "level8", "level9"]

EMPTY_SQUARE = pygame.image.load(os.path.join(IMG_FOLDER, "EmptySquare.png"))
WATER_SQUARE = pygame.image.load(os.path.join(IMG_FOLDER, "Water.png"))
ICE_SQUARE = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
GOAL_SQUARE = pygame.image.load(os.path.join(IMG_FOLDER, "FinishSquare.png"))
WALL_SQUARE = pygame.image.load(os.path.join(IMG_FOLDER, "Wall.png"))
ICE_SQUARE.fill(WHITE)

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(GAME_NAME)

        self.running = True
        self.win = False
        self.all_sprites = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            event_type = event.type

            if event_type == pygame.QUIT:
                self.running = False

        key_state = pygame.key.get_pressed()
        
        if key_state[pygame.K_RIGHT]:
            right_x_index = (self.player.rect.x + SQUARE_SIZE) // SQUARE_SIZE
            right_y_index = self.player.rect.y // SQUARE_SIZE

            if self.m[right_y_index][right_x_index] in ["2", "3"]:
                self.player.set_speed_x(SPEED_INCREASE_AMOUNT)
                self.break_ice()

        elif key_state[pygame.K_LEFT]:
            left_x_index = (self.player.rect.x - SQUARE_SIZE) // SQUARE_SIZE
            left_y_index = self.player.rect.y // SQUARE_SIZE

            if self.m[left_y_index][left_x_index] in ["2", "3"]:
                self.player.set_speed_x(-SPEED_INCREASE_AMOUNT)
                self.break_ice()

        elif key_state[pygame.K_DOWN]:
            down_x_index = self.player.rect.x // SQUARE_SIZE
            down_y_index = (self.player.rect.y + SQUARE_SIZE) // SQUARE_SIZE

            if self.m[down_y_index][down_x_index] in ["2", "3"]:
                self.player.set_speed_y(SPEED_INCREASE_AMOUNT)
                self.break_ice()

        elif key_state[pygame.K_UP]:
            up_x_index = self.player.rect.x // SQUARE_SIZE
            up_y_index = (self.player.rect.y - SQUARE_SIZE) // SQUARE_SIZE

            if self.m[up_y_index][up_x_index] in ["2", "3"]:
                self.player.set_speed_y(-SPEED_INCREASE_AMOUNT)
                self.break_ice()

    def update(self):
        self.all_sprites.update()

        player_x_index = self.player.rect.x // SQUARE_SIZE
        player_y_index = self.player.rect.y // SQUARE_SIZE

        if self.m[player_y_index][player_x_index] == "3":
            self.win = True
        
        if self.win:
            print "parabens!"
            # TODO ação para quando vencer (passar nível)

    def draw(self):

        for i in range(15):
            for j in range(19):
                if self.m[i][j]=="0":
                    self.screen.blit(EMPTY_SQUARE,(j*SQUARE_SIZE,i*SQUARE_SIZE))
                elif self.m[i][j]=="1":
                    self.screen.blit(WATER_SQUARE,(j*SQUARE_SIZE,i*SQUARE_SIZE))
                elif self.m[i][j]=="2":
                    self.screen.blit(ICE_SQUARE,(j*SQUARE_SIZE,i*SQUARE_SIZE))
                elif self.m[i][j]=="3":
                    self.screen.blit(GOAL_SQUARE,(j*SQUARE_SIZE,i*SQUARE_SIZE))
                elif self.m[i][j]=="4":
                    self.screen.blit(WALL_SQUARE,(j*SQUARE_SIZE,i*SQUARE_SIZE))

        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def loop(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def run(self):
        self.curr_level_index = 0
        self.level_path = os.path.join(LEVELS_FOLDER, LEVEL_NAMES[self.curr_level_index] + ".txt")
        self.m = list(map(lambda x:list(x), open(self.level_path, "r").read().splitlines()))

        bg_path = os.path.join(IMG_FOLDER, "Player.png")
        pos = open(self.level_path, "r").read().splitlines()[15].split(" ")
        player_x = int(pos[0]) * SQUARE_SIZE
        player_y = int(pos[1]) * SQUARE_SIZE
        self.player = Player(bg_path, (player_x, player_y))
        self.all_sprites.add(self.player)

        pygame.mixer.music.load(os.path.join(SOUNDS_FOLDER, "GameMusic.mp3"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.65)

        self.loop()
        pygame.quit()
    
    def break_ice(self):
        player_x_index = self.player.rect.x // SQUARE_SIZE
        player_y_index = self.player.rect.y // SQUARE_SIZE

        self.m[player_y_index][player_x_index] = "1"

def main():
    game = Game()
    game.run()
    subprocess.call(['./clean.sh'])

if __name__ == "__main__":
    main()
