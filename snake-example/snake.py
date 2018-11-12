import pygame, random
from pygame.locals import *

pygame.init()

# function for apple position alligned to snake
def on_grid_rand():
    x = random.randint(0, 790)
    y = random.randint(0, 590)

    return (x//10 * 10, y//10 * 10)

# assigning values for useful constants
WIDTH = 800
HEIGHT = 600

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# setting the screen.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minicurso Pygame - Snake")

# creating a snake, represented by an array of tuples.
# its initial length is 3.
snake = [(200, 200), (210, 200), (220, 200)]

# setting the skin color for snake
snake_skin = pygame.Surface((10, 10))
snake_skin.fill(COLOR_WHITE)

# setting the 'food' for snake
apple = pygame.Surface((10, 10))
apple.fill(COLOR_RED)
apple_pos = on_grid_rand()

curr_direction = RIGHT
pause = False

# setting clock.
clock = pygame.time.Clock()

# game main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                curr_direction = UP
            if event.key == pygame.K_DOWN:
                curr_direction = DOWN
            if event.key == pygame.K_LEFT:
                curr_direction = LEFT
            if event.key == pygame.K_RIGHT:
                curr_direction = RIGHT
            if event.key == pygame.K_SPACE:
                pause = (not pause)
    
    if not pause:
        if curr_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if curr_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if curr_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        if curr_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill(COLOR_BLACK)
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
    clock.tick(30)