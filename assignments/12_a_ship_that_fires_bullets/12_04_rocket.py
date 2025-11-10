import sys
import pygame

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # I load the ship picture
        self.image = pygame.image.load('images/ship.bmp').convert()

        # I make the background of the ship transparent to the frame
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)

        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # I put how the rocket is supposed to move
        self.mv_right = False
        self.mv_left  = False
        self.mv_up    = False
        self.mv_down  = False

        self.speed = 5

    def update(self):
        if self.mv_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.mv_left and self.rect.left > 0:
            self.x -= self.speed
        if self.mv_up and self.rect.top > 0:
            self.y -= self.speed
        if self.mv_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Exercise 12-4: Rocket")

    # Create the matching background color
    BG_COLOR = (255, 255, 255)  

    rocket = Rocket(screen)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: rocket.mv_right = True
                if event.key == pygame.K_LEFT:  rocket.mv_left  = True
                if event.key == pygame.K_UP:    rocket.mv_up    = True
                if event.key == pygame.K_DOWN:  rocket.mv_down  = True
                if event.key == pygame.K_q:     pygame.quit(); sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: rocket.mv_right = False
                if event.key == pygame.K_LEFT:  rocket.mv_left  = False
                if event.key == pygame.K_UP:    rocket.mv_up    = False
                if event.key == pygame.K_DOWN:  rocket.mv_down  = False

        rocket.update()
        screen.fill(BG_COLOR)
        rocket.draw()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_game()
