import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
    ax.cla()  # Очистка текущего графика

    frequency_ratio = frame / 100  # Изменение соотношения частот от 0 до 1
    t = np.linspace(0, 2 * np.pi, 1000)  # Временные значения t для построения графика
    x = np.sin(t)  # Компонента x
    y = np.sin(frequency_ratio * t)  # Компонента y

    # Построение графика фигуры Лисажу
    ax.plot(x, y, color='blue')

    # Установка пределов осей
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)

    # Добавление заголовка и меток осей
    ax.set_title('Вращение фигуры Лисажу')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

# Создание фигуры и осей для графика
fig, ax = plt.subplots()

# Создание анимации с изменением соотношения частот
animation = FuncAnimation(fig, update, frames=100, interval=50)

# Отображение анимации
plt.show()
