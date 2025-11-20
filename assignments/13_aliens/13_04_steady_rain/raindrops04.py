import sys
import pygame

from raindrop04 import Raindrop04


class Raindrops04:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Raindrops 13-4")

        self.bg_color = (230, 230, 230)

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
        # Create a grid
        raindrop = Raindrop04(self)
        drop_width, drop_height = raindrop.rect.size

        # How many drops fit horizontally
        available_space_x = 800 - (2 * drop_width)
        number_cols = available_space_x // (2 * drop_width)

        # How many drops fit vertically
        available_space_y = 600 - (2 * drop_height)
        number_rows = available_space_y // (2 * drop_height)

        # The full grid
        for row in range(number_rows):
            for col in range(number_cols):
                self._create_raindrop(col, row)

    def _create_raindrop(self, col, row):
        # Create one raindrop
        raindrop = Raindrop04(self)
        drop_width, drop_height = raindrop.rect.size

        raindrop.rect.x = drop_width + 2 * drop_width * col
        raindrop.rect.y = drop_height + 2 * drop_height * row

        raindrop.y = float(raindrop.rect.y)

        self.raindrops.add(raindrop)

    def _create_top_row(self):

# I added this for this exercise
        raindrop = Raindrop04(self)
        drop_width, drop_height = raindrop.rect.size

        # How many drops fit across the screen.
        available_space_x = 800 - (2 * drop_width)
        number_cols = available_space_x // (2 * drop_width)

        for col in range(number_cols):
            new_drop = Raindrop04(self)
            new_drop.rect.x = drop_width + 2 * drop_width * col
            new_drop.rect.y = drop_height
            new_drop.y = float(new_drop.rect.y)
            self.raindrops.add(new_drop)

    def _update_raindrops(self):
        # Move all raindrops down
        self.raindrops.update()

# I changed this, if a raindrop reaches the bottom it gets removed and creates new row
        row_reached_bottom = False

        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= 600:
                self.raindrops.remove(raindrop)
                row_reached_bottom = True

        if row_reached_bottom:
            self._create_top_row()

    def _update_screen(self):
        # Redraw the screen
        self.screen.fill(self.bg_color)

        # Draw all raindrops
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    game = Raindrops04()
    game.run_game()

