import sys
import pygame
from star import Star


class Stars:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Stars")

        self.bg_color = (230, 230, 230)

        self.stars = pygame.sprite.Group()
        self._create_grid()

    def run_game(self):
   
# I am starting the "loop" for the stars.
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_grid(self):
# Creates the grid
        star = Star(self)
        star_width, star_height = star.rect.size

        # Determining how many stars will fit in the screen
        available_space_x = 800 - (2 * star_width)
        number_cols = available_space_x // (2 * star_width)

        available_space_y = 600 - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row in range(number_rows):
            for col in range(number_cols):
                self._create_star(col, row)

    def _create_star(self, col, row):
  # Creates a star and places it.
        star = Star(self)
        star_width, star_height = star.rect.size

        star.rect.x = star_width + 2 * star_width * col
        star.rect.y = star_height + 2 * star_height * row

        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ai = Stars()
    ai.run_game()
