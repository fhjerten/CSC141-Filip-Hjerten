# I take my files from my main alien invasion project and adjust them based off the instructions from each exercise.
import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # I changed this line: 
        self.rect.midleft = self.screen_rect.midleft

        # Store floats for the ship's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # We move up and down only
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update (self):

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
