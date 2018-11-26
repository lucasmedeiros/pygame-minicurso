import pygame

WIDTH = 1000
HEIGHT = 800
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Motion Demo")
clock = pygame.time.Clock()
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 80))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -0.2
        if keys[pygame.K_RIGHT]:
            self.acc.x = 0.2
        if keys[pygame.K_UP]:
            self.acc.y = -0.2
        if keys[pygame.K_DOWN]:
            self.acc.y = 0.2

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.rect.center = self.pos

def draw_text(text, size, col, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, col)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_vectors(obj):
    draw_arrow(obj.pos, (obj.pos+obj.vel*20), GREEN, 7)
    draw_arrow(obj.pos, (obj.pos+obj.acc*400), RED, 3)

def draw_arrow(p1, p2, col, size):
    pygame.draw.line(screen, col, p1, p2, size)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_vectors(player)
    txt = "Pos: ({:.2f}, {:.2f})".format(player.pos.x, player.pos.y)
    draw_text(txt, 25, WHITE, 5, 5)
    txt = "Vel: ({:.2f}, {:.2f})".format(player.vel.x, player.vel.y)
    draw_text(txt, 25, GREEN, 5, 55)
    txt = "Acc: ({:.2f}, {:.2f})".format(player.acc.x, player.acc.y)
    draw_text(txt, 25, RED, 5, 105)
    pygame.display.flip()

pygame.quit()
