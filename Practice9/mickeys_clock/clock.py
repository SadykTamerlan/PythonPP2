import pygame
import datetime
import math

def draw_clock(screen, cx, cy):
    now = datetime.datetime.now()

    minutes = now.minute
    seconds = now.second

    # углы
    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    # длина стрелок
    minute_length = 150
    second_length = 120

    # координаты
    mx = cx + minute_length * math.cos(math.radians(minute_angle))
    my = cy + minute_length * math.sin(math.radians(minute_angle))

    sx = cx + second_length * math.cos(math.radians(second_angle))
    sy = cy + second_length * math.sin(math.radians(second_angle))

    # рисуем центр
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), 10)

    # стрелки
    pygame.draw.line(screen, (0, 0, 255), (cx, cy), (mx, my), 8)  # минуты
    pygame.draw.line(screen, (255, 0, 0), (cx, cy), (sx, sy), 4)  # секунды