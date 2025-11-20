import pygame
from pygame.sprite import Sprite


class Star(Sprite):
# A star class

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Start each star near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

