import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Extremely cool Sideways Shooter")
screen_rect = screen.get_rect()
bg_color = (255, 255, 255)

ship = pygame.image.load("images/ship.bmp").convert()
ship.set_colorkey(ship.get_at((0, 0)))
ship_rect = ship.get_rect()
ship_rect.midleft = screen_rect.midleft

y = float(ship_rect.y)
moving_up = False
moving_down = False
ship_speed = 5

# Bullets
bullets = []
bullet_speed = 8

# Alien image
alien_img = pygame.image.load("images/alien.bmp").convert()
alien_img.set_colorkey(alien_img.get_at((0, 0)))
alien_width, alien_height = alien_img.get_rect().size

# Aliens in list
aliens = []
alien_speed = 3

def create_fleet():
    """Create aliens along the right side."""
    for row in range(8):
        alien = pygame.Rect(0, 0, alien_width, alien_height)
        alien.right = screen_rect.right - 20
        alien.y = 50 + row * 80
        aliens.append(alien)

create_fleet()

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
                bullet = pygame.Rect(0, 0, 12, 4)
                bullet.midleft = ship_rect.midright
                bullets.append(bullet)
            elif event.key == pygame.K_q:
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    if moving_up and ship_rect.top > 0:
        y -= ship_speed
    if moving_down and ship_rect.bottom < screen_rect.bottom:
        y += ship_speed
    ship_rect.y = y

    # Move bullets
    for bullet in bullets:
        bullet.x += bullet_speed

    # Remove bullets off-screen
    for bullet in bullets[:]:
        if bullet.left >= screen_rect.right:
            bullets.remove(bullet)

    # Move aliens
    for alien in aliens:
        alien.x -= alien_speed

    # Remove aliens that leave the screen
    for alien in aliens[:]:
        if alien.right <= 0:
            aliens.remove(alien)

    # When bullet hit aliens
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                break

    screen.fill(bg_color)
    screen.blit(ship, ship_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    for alien in aliens:
        screen.blit(alien_img, alien)

    pygame.display.flip()
    clock.tick(60)
