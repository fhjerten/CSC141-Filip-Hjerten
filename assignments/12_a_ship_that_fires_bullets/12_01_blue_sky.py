import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Blue Sky")

blue = (0, 0, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(blue)
    pygame.display.flip()
