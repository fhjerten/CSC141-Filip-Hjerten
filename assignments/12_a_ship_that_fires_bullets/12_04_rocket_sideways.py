import sys
import pygame

pygame.init()

# This is for the empty window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exercise 12-5: Keys")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # When any key is pressed, it prints some code
        if event.type == pygame.KEYDOWN:
            print(event.key)

    # The white background
    screen.fill((255, 255, 255))
    pygame.display.flip()
