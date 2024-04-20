import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка и иконки окна
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('img/42648.jpg')
pygame.display.set_icon(icon)

# Загрузка изображения цели и установка начальных параметров
target_img = pygame.image.load('img/target.png')
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_x_speed = 2  # начальная скорость движения цели по оси X
target_y_speed = 2  # начальная скорость движения цели по оси Y

# Начальное количество очков и шрифт для отображения текста
points = 0
font = pygame.font.Font(None, 36)

# Выбор случайного цвета фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Главный цикл игры
running = True
while running:
    # Заливка экрана цветом
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по цели
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                # Обновление позиции и ускорение цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                points += 1
                target_x_speed += 0.5
                target_y_speed += 0.5

    # Обновление позиции цели
    target_x += target_x_speed
    target_y += target_y_speed

    # Отражение цели, если она достигла границ экрана
    if target_x > SCREEN_WIDTH - target_width or target_x < 0:
        target_x_speed *= -1
    if target_y > SCREEN_HEIGHT - target_height or target_y < 0:
        target_y_speed *= -1

    # Отображение счёта
    score_text = font.render(f"Очки: {points}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

# Завершение работы pygame
pygame.quit()
sys.exit()