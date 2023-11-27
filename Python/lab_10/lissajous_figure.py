import numpy as np
import matplotlib.pyplot as plt

ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

num_points = 1000

t = np.linspace(0, 2 * np.pi, num_points)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Перебор соотношений частот и построение фигур Лиссажу
for i, (m, n) in enumerate(ratios):
    x = np.sin(m * t)
    y = np.sin(n * t)

    # Отрисовка фигуры Лиссажу на соответствующем подграфике
    row = i // 2  # Вычисление номера строки подграфика
    col = i % 2   # Вычисление номера столбца подграфика
    axes[row, col].plot(x, y)
    axes[row, col].set_title(f'({m}:{n})')

# Установка общего заголовка для всего ряда графиков
fig.suptitle('Фигуры Лиссажу с разными соотношениями частот')

plt.show()
