import pygame
import sys
import random
from pygame.locals import *


pygame.init()

WIDTH, HEIGHT = 400, 600

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0 , 0)

# Загружаем картинки
car_img = pygame.image.load("car.png").convert_alpha()
coin_img = pygame.image.load("coin.png").convert_alpha()
speed = 5

#Задний фон

bg = pygame.image.load("road.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_y = 0
#Размеры
car_img = pygame.transform.scale(car_img, (40, 60))
coin_img = pygame.transform.scale(coin_img, (30, 30))
coin_img.set_colorkey((255, 255, 255))

#Рект для машины
car = pygame.Rect(180, 500, 40, 60)

coins = []
coin_timer = 0

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()


running = True 
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.x -= speed
    if keys[pygame.K_RIGHT]:
        car.x += speed

    # Ограничение по экрану
    car.x = max(0, min(WIDTH - car.width, car.x))

    #Движения заднего фона
    bg_y += 5
    if bg_y >= HEIGHT:
        bg_y = 0


    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y - HEIGHT))

    # Генерация монет
    coin_timer += 1
    if coin_timer > 60:
        coin_x = random.randint(20, WIDTH - 20)
        coins.append(pygame.Rect(coin_x, 0, 20, 20))
        coin_timer = 0

    # Движение монет
    for coin in coins:
        coin.y += 5

    # Проверка столкновения
    for coin in coins[:]:
        if car.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Удаление ушедших монет
    coins = [c for c in coins if c.y < HEIGHT]

    # Рисуем машину
    screen.blit(car_img, (car.x, car.y))

    # Рисуем монеты
    for coin in coins:
        screen.blit(coin_img, (coin.x, coin.y))


    #Счет (справа сверху)
    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()