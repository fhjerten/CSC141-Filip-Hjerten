import pygame
from pygame.sprite import Sprite


class Raindrop04(Sprite):
    # Same as Raindrop from last exercise
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen

        # Load the image
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

        # Falling speed
        self.speed = 0.2

    def update(self):
        # Move the raindrop straight down
        self.y += self.speed
        self.rect.y = self.y
