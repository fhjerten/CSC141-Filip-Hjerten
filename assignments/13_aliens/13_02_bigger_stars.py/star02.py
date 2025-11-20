import pygame
from pygame.sprite import Sprite


class Star02(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        # Use the main game's screen
        self.screen = ai_game.screen

        # Load the star image
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
