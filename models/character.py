from abc import ABC

import pygame


class Player(ABC):
    def __init__(self):
        try:
            self.player_img = pygame.image.load("path.png")
        except:
            self.player_img = pygame.Surface((40, 60))
            self.player_img.fill((255, 79, 0))

        self.speed = 5
        self.rect = self.player_img.get_rect()
        self.vertical_velocity = 0
        self.jump_state = False
        self.jump_height = -15

