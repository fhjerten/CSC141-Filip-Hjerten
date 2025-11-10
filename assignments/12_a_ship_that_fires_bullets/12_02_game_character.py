import sys
import pygame

def run_game():
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Game Character")

    # I match the ship background color
    bg_color = (255, 255, 255)

    # I load in the image and make the image's background transparent
    img = pygame.image.load('images/ship.bmp').convert()
    img.set_colorkey(img.get_at((0, 0)))

    # Makes the image in center
    rect = img.get_rect()
    rect.center = screen.get_rect().center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()

        screen.fill(bg_color)
        screen.blit(img, rect)
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
