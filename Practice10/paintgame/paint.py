import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

color = BLACK
tool = "brush"

drawing = False
start_pos = None

screen.fill(WHITE)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 🎮 выбор инструментов
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"
            if event.key == pygame.K_b:
                tool = "brush"

            # 🎨 выбор цвета
            if event.key == pygame.K_1:
                color = BLACK
            if event.key == pygame.K_2:
                color = RED
            if event.key == pygame.K_3:
                color = BLUE
            if event.key == pygame.K_4:
                color = GREEN

        # мышь нажата
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # мышь отпущена
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # 📦 прямоугольник
            if tool == "rect":
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        start_pos[0],
                        start_pos[1],
                        end_pos[0] - start_pos[0],
                        end_pos[1] - start_pos[1]
                    ),
                    2
                )

            # 🔵 круг
            if tool == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

    # ✏️ рисование кистью и ластик
    if drawing:
        mouse = pygame.mouse.get_pos()

        if tool == "brush":
            pygame.draw.circle(screen, color, mouse, 5)

        if tool == "eraser":
            pygame.draw.circle(screen, WHITE, mouse, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()