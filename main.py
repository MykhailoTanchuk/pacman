import sys

import pygame

from constants import *
from ghosts import Ghost
from maze import Maze
from pacman import Pacman

# Ініціалізація Pygame
pygame.init()

# Розміри екрану
SCREEN_WIDTH = MAZE_WIDTH * 40  # Розмір екрану залежить від розміру лабіринту
SCREEN_HEIGHT = MAZE_HEIGHT * 40
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Ініціалізація об'єктів гри
pacman = Pacman(1 * 40, 1 * 40)  # Початкові координати Пакмена
maze = Maze()  # Генеруємо статичний лабіринт

agg_x = 9 * 40
agg_y = 9 * 40
rand_x = 10 * 40
rand_y = 10 * 40
caut_x = 11 * 40
caut_y = 11 * 40

# Ініціалізація привидів з різними поведінками
ghosts = [
    Ghost(agg_x, agg_y, RED, 'aggressive'),  # Агресивний привид
    Ghost(rand_x, rand_y, GREEN, 'random'),  # Випадковий привид
    Ghost(caut_x, caut_y, PINK, 'cautious')  # Обережний привид
]

# Лічильник для контролю швидкості привидів
ghost_move_counter = 0
ghost_move_interval = 40  # Привиди починають рухатися кожні 40 кадрів
min_ghost_move_interval = 15  # Мінімальна швидкість привидів (15 кадрів)

# Таймер для підвищення складності
difficulty_timer = 0
difficulty_increase_interval = 5000  # Підвищувати складність кожні 5 секунд (5000 мс)


# Основна функція гри
def game_loop():
    global ghost_move_counter, ghost_move_interval, difficulty_timer
    running = True
    start_time = pygame.time.get_ticks()  # Початковий час гри

    while running:
        # Отримуємо всі події
        events = pygame.event.get()

        # Обробка подій
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # Оновлення стану гри
        pacman.update(maze, events)

        # Видалення фішок, якщо Пакмен на них
        maze.remove_pellet(pacman)

        # Перевірка на перемогу
        if maze.all_pellets_collected():
            print("Ви виграли!")
            running = False  # Завершуємо гру при виграші

        # Оновлення привидів
        if ghost_move_counter % ghost_move_interval == 0:
            for ghost in ghosts:
                ghost.update(maze, pacman)
        ghost_move_counter += 1

        # Перевірка на зіткнення Пакмена з привидами
        for ghost in ghosts:
            if pacman.grid_x == ghost.grid_x and pacman.grid_y == ghost.grid_y:
                print("Пакмена спіймали! Ви програли.")
                running = False  # Завершуємо гру при програші

        # Очищення екрану
        screen.fill(BLACK)

        # Малювання лабіринту
        maze.draw(screen)

        # Малювання Пакмена
        pacman.draw(screen)

        # Малювання привидів
        for ghost in ghosts:
            ghost.draw(screen)

        # Оновлення екрану
        pygame.display.flip()

        # Оновлення гри відповідно до FPS
        clock.tick(FPS)


# Запуск гри
if __name__ == "__main__":
    game_loop()
