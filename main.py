import pygame
import sys

from models.character import Player
from models.objects import Pipe, Platform
from utility.util import collide_with_object
from utility.colors import WHITE, BROWN, GREEN

pygame.init()

# Constants
WIDTH, HEIGHT = 1300, 800
FPS = 60

# Pipes and platforms
pipe1 = Pipe()
pipe2 = Pipe()
platform = Platform()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario game")

player = Player()
gravity = 0.5  # Gravity

clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    on_ground = player.rect.bottom >= HEIGHT

    if keys[pygame.K_LEFT] and player.rect.left > 0:
        player.rect.x -= player.speed
    if keys[pygame.K_RIGHT] and player.rect.right < WIDTH:
        player.rect.x += player.speed
    if keys[pygame.K_SPACE] and not player.jumping:
        player.jumping = True
        player.vertical_velocity = player.jump_height

    player.vertical_velocity += gravity  # Apply gravity
    player.rect.y += player.vertical_velocity  # Move player vertically

    if player.rect.bottom >= HEIGHT:
        player.rect.bottom = HEIGHT
        player.jumping = False
        player.vertical_velocity = 0

    collide_with_object(player, platform)
    collide_with_object(player, pipe1)
    collide_with_object(player, pipe2)

    window.fill(WHITE)
    window.blit(player.player_img, player.rect.topleft)
    pygame.draw.rect(window, GREEN, pipe1.get_rect())
    pygame.draw.rect(window, GREEN, pipe2.get_rect())
    pygame.draw.rect(window, BROWN, platform.get_rect())

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
