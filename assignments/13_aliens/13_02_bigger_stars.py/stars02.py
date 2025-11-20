import sys
import pygame
from random import randint

from star02 import Star02

# Same as first assignment, but change create_star to change how stars are placed

class Stars02:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Stars 13-2")

        self.bg_color = (230, 230, 230)

        self.stars = pygame.sprite.Group()

        self._create_grid()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
        # Creates the grid
        star = Star02(self)
        star_width, star_height = star.rect.size

        # How many stars fit horizontally
        available_space_x = 700 - (2 * star_width)
        number_cols = available_space_x // (2 * star_width)

        # How many stars fit vertically.
        available_space_y = 600 - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row in range(number_rows):
            for col in range(number_cols):
                self._create_star(col, row)

    def _create_star(self, col, row):
        star = Star02(self)
        star_width, star_height = star.rect.size

        star.rect.x = star_width + 2 * star_width * col
        star.rect.y = star_height + 2 * star_height * row

        # Adding a small random offset
        star.rect.x += randint(-10, 10)
        star.rect.y += randint(-10, 10)

        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = Stars02()
    ai.run_game()
