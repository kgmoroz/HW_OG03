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

# Загрузка изображения цели, прицела и звукового файла
target_img = pygame.image.load('img/target.png')
crosshair_img = pygame.image.load('img/crosshair.png')
shoot_sound = pygame.mixer.Sound('img/shoot.wav')  # Загрузка звукового файла

# Установка начального положения и размеров цели
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Установка начальных скоростей движения цели по осям X и Y
speed_step = 0.02
target_x_speed = speed_step
target_y_speed = speed_step

# Скрыть стандартный курсор мыши
pygame.mouse.set_visible(False)

# Начальное количество очков и настройка шрифта для вывода текста
points = 0
font = pygame.font.Font(None, 36)

# Выбор случайного цвета фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Главный цикл игры
running = True
while running:
    screen.fill(color)  # Заполнение фона цветом

    # Обработка событий pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                # Перемещение цели на новую случайную позицию
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                points += 1  # Увеличение количества очков
                target_x_speed += speed_step * (
                    1 if target_x_speed > 0 else -1)  # Увеличение скорости движения по X с учетом направления
                target_y_speed += speed_step * (
                    1 if target_y_speed > 0 else -1)  # Увеличение скорости движения по Y с учетом направления
                shoot_sound.play()  # Воспроизведение звука выстрела

    # Обновление позиции цели
    target_x += target_x_speed
    target_y += target_y_speed

    # Отражение цели от границ экрана
    if target_x > SCREEN_WIDTH - target_width or target_x < 0:
        target_x_speed *= -1
    if target_y > SCREEN_HEIGHT - target_height or target_y < 0:
        target_y_speed *= -1

    # Отрисовка текста очков и скорости
    score_text = font.render(f"Очки: {points}", True, (255, 255, 255))
    speed_text = font.render(f"Скорость: {abs(target_x_speed):.2f}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 50))

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Отрисовка прицела на позицию курсора
    cross_x, cross_y = pygame.mouse.get_pos()
    screen.blit(crosshair_img, (cross_x - 16, cross_y - 16))

    # Обновление экрана
    pygame.display.update()

# Выход из игры и закрытие программы
pygame.quit()
sys.exit()