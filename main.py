
import pygame
import sys

from models.objects import Pipe, Platform

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Pipes and platforms
pipe1 = Pipe(200, 400, 50, 200)
pipe2 = Pipe(500, 350, 50, 250)
platform = Platform( 300, 300, 100, 20)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario game")

try:
    player_img = pygame.image.load("path.png")
except:
    player_img = pygame.Surface((40, 60))
    player_img.fill((255, 79, 0))

player_rect = player_img.get_rect()
player_speed = 5
player_vel_y = 0  # Vertical velocity
jumping = False   # Jump state
gravity = 0.5     # Gravity
jump_height = -15  # Jump velocity

clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    on_ground = player_rect.bottom >= HEIGHT

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.y += player_speed
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        player_vel_y = jump_height

    player_vel_y += gravity  # Apply gravity
    player_rect.y += player_vel_y  # Move player vertically

    if player_rect.bottom >= HEIGHT:
        player_rect.bottom = HEIGHT
        jumping = False
        player_vel_y = 0

    if player_rect.colliderect(platform.x, platform.y, platform.width, platform.height):
        player_rect.y = platform.y - player_rect.height  # Set player on top of the platform
        jumping = False  # Reset jumping state
        player_vel_y = 0  # Reset vertical velocity

    window.fill(WHITE)
    window.blit(player_img, player_rect.topleft)
    pygame.draw.rect(window, (0, 255, 0), (pipe1.x, pipe1.y, pipe1.width, pipe1.height))
    pygame.draw.rect(window, (0, 255, 0), (pipe2.x, pipe2.y, pipe2.width, pipe2.height))
    pygame.draw.rect(window, (139, 69, 19), (platform.x, platform.y, platform.width, platform.height))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()



