import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    # A single raindrop 
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen

        # Load the raindrop image
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the vertical 
        self.y = float(self.rect.y)

        # Falling speed
        self.speed = 0.1

    def update(self):
        # Moving the raindrop straight down
        self.y += self.speed
        self.rect.y = self.y
