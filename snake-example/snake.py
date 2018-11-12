import pygame, random
from pygame.locals import *

pygame.init()

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

def text_objects(text, font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()

# generates random positions for apples
def on_grid_rand_position():
    x = random.randint(0, 790)
    y = random.randint(0, 590)

    return (x//10 * 10, y//10 * 10)

# checks collision between two cells
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minicurso Pygame - Snake")

snake = [(200, 200), (210, 200), (220, 200)]

snake_skin = pygame.Surface((10, 10))
snake_skin.fill(COLOR_WHITE)

apple = pygame.Surface((10, 10))
apple.fill(COLOR_RED)
apple_pos = on_grid_rand_position()

curr_direction = RIGHT
pause = False
game_over = False
close = False

clock = pygame.time.Clock()

# game main loop
while not close:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP) and (not curr_direction == DOWN):
                curr_direction = UP
            if (event.key == pygame.K_DOWN) and (not curr_direction == UP):
                curr_direction = DOWN
            if (event.key == pygame.K_LEFT) and (not curr_direction == RIGHT):
                curr_direction = LEFT
            if (event.key == pygame.K_RIGHT) and (not curr_direction == LEFT):
                curr_direction = RIGHT
            if event.key == pygame.K_SPACE:
                pause = (not pause)
    
    if not game_over:
        if not pause:
            initial_head_pos = snake[0]
            if curr_direction == UP:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if curr_direction == DOWN:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if curr_direction == LEFT:
                snake[0] = (snake[0][0] - 10, snake[0][1])
            if curr_direction == RIGHT:
                snake[0] = (snake[0][0] + 10, snake[0][1])
            
            snake[1] = initial_head_pos

            for i in range(len(snake) - 1, 1, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])
        
            # detects auto collision
            for i in range(1, len(snake)):
                if collision(snake[0], snake[i]):
                    game_over = True
            
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_rand_position()
            snake.append((0, 0))

        screen.fill(COLOR_BLACK)
        screen.blit(apple, apple_pos)

        for pos in snake:
            screen.blit(snake_skin, pos)
    else:
        font = pygame.font.SysFont('comicsansms', 25)
        surface_text, rect_text = text_objects("GAME OVER", font, COLOR_WHITE)
        rect_text.center = ((WIDTH / 2), (HEIGHT / 4))
        screen.blit(surface_text, rect_text)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()