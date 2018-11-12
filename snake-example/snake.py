import pygame, random
from pygame.locals import *

pygame.init()

# assigning values for useful constants
WIDTH = 800
HEIGHT = 600

UPPER_BOUND_X = 790
UPPER_BOUND_Y = 590
LOWER_BOUND = 0

COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

font = pygame.font.SysFont('comicsansms', 25)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minicurso Pygame - Snake")

# creates a unique model for text display
def text_objects(text, font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()

# generates random positions for apples
def on_grid_rand_position():
    x = random.randint(LOWER_BOUND, UPPER_BOUND_X)
    y = random.randint(LOWER_BOUND, UPPER_BOUND_Y)

    # print (x)
    # print (y)

    # print (x//10 * 10)
    # print (y//10 * 10)

    return (x//10 * 10, y//10 * 10)

# checks collision between two cells
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

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

surface_gameover_text, rect_gameover_text = text_objects("GAME OVER", font, COLOR_WHITE)
rect_gameover_text.center = ((WIDTH / 2), (HEIGHT / 15))

surface_pause_text, rect_pause_text = text_objects("PAUSE", font, COLOR_WHITE)
rect_pause_text.center = ((WIDTH / 2), (HEIGHT / 15))

surface_tryagain_text, rect_tryagain_text = text_objects("[ENTER] PARA TENTAR NOVAMENTE", font, COLOR_WHITE)
rect_tryagain_text.center = ((WIDTH / 2), (HEIGHT / 2))

# game main loop
while not close:
    
    screen.fill(COLOR_BLACK)

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
            if event.key == pygame.K_SPACE and not game_over:
                pause = (not pause)
            if event.key == pygame.K_RETURN:
                game_over = False
    
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
        else:
            screen.blit(surface_pause_text, rect_pause_text)
            
        if collision(snake[0], apple_pos):
            apple_pos = on_grid_rand_position()
            snake.append((0, 0))
        
        if snake[0][0] < LOWER_BOUND or snake[0][0] > UPPER_BOUND_X or snake[0][1] < LOWER_BOUND or snake[0][1] > UPPER_BOUND_Y:
            game_over = True

        for pos in snake:
            screen.blit(snake_skin, pos)

        screen.blit(apple, apple_pos)
    else:
        screen.blit(surface_gameover_text, rect_gameover_text)
        screen.blit(surface_tryagain_text, rect_tryagain_text)
        snake = [(200, 200), (210, 200), (220, 200)]
        curr_direction = RIGHT

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()