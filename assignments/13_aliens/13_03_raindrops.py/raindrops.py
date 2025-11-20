import sys
import pygame

from raindrop import Raindrop


class Raindrops:
    # Create a grid of raindrops 
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Raindrops")

        self.bg_color = (230, 230, 230)

        # Group that holds all raindrops
        self.raindrops = pygame.sprite.Group()

        self._create_grid()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
        # Create a grid of raindrops that fills the screen
        raindrop = Raindrop(self)
        drop_width, drop_height = raindrop.rect.size

        available_space_x = 700 - (2 * drop_width)
        number_cols = available_space_x // (2 * drop_width)

        available_space_y = 600 - (2 * drop_height)
        number_rows = available_space_y // (2 * drop_height)

        # Create the grid
        for row in range(number_rows):
            for col in range(number_cols):
                self._create_raindrop(col, row)

    def _create_raindrop(self, col, row):
        raindrop = Raindrop(self)
        drop_width, drop_height = raindrop.rect.size

        raindrop.rect.x = drop_width + 2 * drop_width * col
        raindrop.rect.y = drop_height + 2 * drop_height * row
        raindrop.y = float(raindrop.rect.y)

        self.raindrops.add(raindrop)

    def _update_raindrops(self):
        # Move all raindrops downward
        self.raindrops.update()

        # The optional part
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= 600:
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        self.screen.fill(self.bg_color)

        # Draw all raindrops
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    game = Raindrops()
    game.run_game()
