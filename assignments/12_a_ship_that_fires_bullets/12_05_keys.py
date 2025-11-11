# I don't know why the name of this file is 12_05_keys.py when it should be exercise 12-6 according to Python Crash Course so I do exercise 12-6 here

import sys
import pygame

pygame.init()

# I set the window
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Exercise 12-6")

screen_rect = screen.get_rect()
bg_color = (255, 255, 255)

# I get the ship, and make its background transparent
ship = pygame.image.load("images/ship.bmp").convert()
ship.set_colorkey(ship.get_at((0, 0)))
ship_rect = ship.get_rect()
ship_rect.midleft = screen_rect.midleft

# I set how the ship moves
y = float(ship_rect.y)
moving_up = False
moving_down = False
ship_speed = 5

# The bullets
bullets = []
bullet_speed = 8

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_SPACE:
                # This creates a bullet
                b = pygame.Rect(0, 0, 12, 4)
                b.midleft = ship_rect.midright
                bullets.append(b)
            elif event.key == pygame.K_q:
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    # How to move the ship
    if moving_up and ship_rect.top > 0:
        y -= ship_speed
    if moving_down and ship_rect.bottom < screen_rect.bottom:
        y += ship_speed
    ship_rect.y = y

    # How the bullets move
    for b in bullets:
        b.x += bullet_speed

    # Deleting bullets that reach end of screen
    bullets = [b for b in bullets if b.right < screen_rect.right]

    screen.fill(bg_color)
    screen.blit(ship, ship_rect)

    for b in bullets:
        pygame.draw.rect(screen, (0, 0, 0), b)

    pygame.display.flip()
    clock.tick(60)
