# I take my files from my main alien invasion project and adjust them based off the instructions from each exercise.
import pygame
from pygame.sprite import Sprite

class Target(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Create the target as a rectangle
        self.rect = pygame.Rect(
            0, 0,
            self.settings.target_width,
            self.settings.target_height
        )

        # Start the target on the RIGHT side.
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)

        self.direction = 1

    def update(self):
        # updates target so it move the target up and down

        # Move vertically only
        self.y += self.settings.target_speed * self.direction
        self.rect.y = self.y

        # Bounce when hitting top or bottom of screen
        if self.rect.top <= 0:
            self.direction = 1
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.direction = -1

    def draw_target(self):
        pygame.draw.rect(
            self.screen,
            self.settings.target_color,
            self.rect
        )
