import pygame
import random

pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Змейка (начальная позиция)
snake = [(200, 200)]
dx, dy = CELL, 0

# Еда
def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:  # не на змейке
            return (x, y)

food = spawn_food()

# Счет и уровень
score = 0
level = 1
speed = 6

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill(BLACK)

    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # управление
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and dx == 0:
            dx, dy = -CELL, 0
        if event.key == pygame.K_RIGHT and dx == 0:
            dx, dy = CELL, 0
        if event.key == pygame.K_UP and dy == 0:
            dx, dy = 0, -CELL
        if event.key == pygame.K_DOWN and dy == 0:
            dx, dy = 0, CELL

    # новая голова
    head = (snake[0][0] + dx, snake[0][1] + dy)

    # ❗ Проверка стен (границы)
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False  # игра заканчивается

    # ❗ Проверка на себя
    if head in snake:
        running = False

    snake.insert(0, head)

    # если съела еду
    if head == food:
        score += 1
        food = spawn_food()

        # ❗ уровень каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 2  # ускорение
    else:
        snake.pop()

    # рисуем еду
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

    # рисуем змейку
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL, CELL))

    # текст (счет + уровень)
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()