import pygame
import sys
from clock import draw_clock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    draw_clock(screen, WIDTH // 2, HEIGHT // 2)

    pygame.display.flip()
    clock.tick(1)  # обновление каждую секунду