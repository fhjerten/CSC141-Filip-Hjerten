import sys
import pygame

from settings_14_03 import Settings
from ship_14_03 import Ship
from bullet_14_03 import Bullet
from target_14_03 import Target
from button_14_03 import Button


class TargetPractice:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Challenging Target Practice")

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        # Game state
        self.game_active = False
        self.misses_left = 3

        # Play button
        self.play_button = Button(self, "Play")

        self.clock = pygame.time.Clock()

    def run_game(self):
      # Game loop
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.target.update()
                self._update_bullets()

            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE and self.game_active:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
       # starts if play is clicked
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self._start_game()
    
    def _start_game(self):
       # Resets and starts new game
        self.game_active = True
        self.bullets.empty()
        self.misses_left = 3

        # Updated: reset target speed
        self.target.reset_speed()

    def _fire_bullet(self):
        # Creating bullets when space bar is pressed
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # Move bullets and check for hits or misses
        self.bullets.update()

        for bullet in self.bullets.copy():
            # Hit the target
            if bullet.rect.colliderect(self.target.rect):
                self.bullets.remove(bullet)

                # Updated: increase target speed with 20 % if hit
                self.target.speed *= 1.2

            # Missed 
            elif bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
                self.misses_left -= 1

                if self.misses_left <= 0:
                    self.game_active = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        if self.game_active:
            self.ship.blitme()
            self.target.draw_target()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        else:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()
