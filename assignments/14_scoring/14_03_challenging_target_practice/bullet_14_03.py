# same as 14_02
# I take my files from my main alien invasion project and adjust them based off the instructions from each exercise.
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # Class to manage bullets fired from the ship

    def __init__(self, ai_game):
       
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Same size as before, just used horizontally now.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        # CHANGED FOR this exercise, start the bullet at the ship's RIGHT side.
        self.rect.midleft = ai_game.ship.rect.midright 


        # CHANGED FOR this exercise, we care about x instead of y.
        self.x = float(self.rect.x)

    def update(self):
# Changed this, from vertical to horizontal movement.

        self.x += self.settings.bullet_speed 
        # Update the rect position.
        self.rect.x = self.x 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
