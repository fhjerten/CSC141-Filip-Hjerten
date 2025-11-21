import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Exercise 13-6 Game Over")
screen_rect = screen.get_rect()
bg_color = (255, 255, 255)

font = pygame.font.SysFont(None, 48)

ship = pygame.image.load("images/ship.bmp").convert()
ship.set_colorkey(ship.get_at((0, 0)))
ship_rect = ship.get_rect()
ship_rect.midleft = screen_rect.midleft
y = float(ship_rect.y)
ship_speed = 5
moving_up = False
moving_down = False

# Bullets
bullets = []
bullet_speed = 8

# Aliens
alien_img = pygame.image.load("images/alien.bmp").convert()
alien_img.set_colorkey(alien_img.get_at((0, 0)))
alien_rect = alien_img.get_rect()
aliens = []
alien_speed = 3

def create_fleet():
    for i in range(8):
        a = pygame.Rect(0, 0, alien_rect.width, alien_rect.height)
        a.right = screen_rect.right - 20
        a.y = 50 + i * 80
        aliens.append(a)

create_fleet()

ship_hits = 0
aliens_destroyed = 0
clock = pygame.time.Clock()

def draw_stats():
    text = f"Hits: {ship_hits}   Destroyed: {aliens_destroyed}"
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (20, 20))

def show_message(msg, color):
    img = font.render(msg, True, color)
    rect = img.get_rect(center=screen_rect.center)
    screen.blit(img, rect)
    pygame.display.flip()
    pygame.time.wait(3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_SPACE:
                b = pygame.Rect(0, 0, 12, 4)
                b.midleft = ship_rect.midright
                bullets.append(b)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    # For the ship movement
    if moving_up and ship_rect.top > 0:
        y -= ship_speed
    if moving_down and ship_rect.bottom < screen_rect.bottom:
        y += ship_speed
    ship_rect.y = y

    # Bullet movement
    for b in bullets:
        b.x += bullet_speed
    for b in bullets[:]:
        if b.left >= screen_rect.right:
            bullets.remove(b)

    # Alien movement
    for a in aliens:
        a.x -= alien_speed

    # The ship hits with aliens
    for a in aliens[:]:
        if a.colliderect(ship_rect) or a.right <= ship_rect.left:
            aliens.remove(a)
            ship_hits += 1

    # Bullet hitting the aliens
    for b in bullets[:]:
        for a in aliens[:]:
            if b.colliderect(a):
                bullets.remove(b)
                aliens.remove(a)
                aliens_destroyed += 1
                break

    # Game over / win
    if ship_hits >= 3:
        screen.fill(bg_color)
        draw_stats()
        show_message("GAME OVER: Ship hit 3 times", (255, 0, 0))
        sys.exit()
    if len(aliens) == 0 and aliens_destroyed > 0:
        screen.fill(bg_color)
        draw_stats()
        show_message("YOU WIN: All aliens destroyed", (0, 150, 0))
        sys.exit()

    # Draw
    screen.fill(bg_color)
    screen.blit(ship, ship_rect)
    for b in bullets:
        pygame.draw.rect(screen, (0, 0, 0), b)
    for a in aliens:
        screen.blit(alien_img, a)
    draw_stats()

    pygame.display.flip()
    clock.tick(60)
