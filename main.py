
import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario game")

try:
    player_img = pygame.image.load("path.png")
except:
    player_img = pygame.Surface((40, 60))
    player_img.fill((255, 0, 0))

player_rect = player_img.get_rect()
player_speed = 5

clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.y += player_speed

    win.fill(WHITE)
    win.blit(player_img, player_rect.topleft)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()



