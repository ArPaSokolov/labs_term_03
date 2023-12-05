import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Параметры сигнала-
amplitude = 1.0  # Амплитуда
duration = 2.0  # Продолжительность в секундах
frequency = 1.0  # Частота в Гц

# Генерация времени
sampling_rate = 1000  # Частота дискретизации в Гц
num_samples = int(duration * sampling_rate)
time = np.linspace(0, duration, num_samples, endpoint=False)

# Создание сигнала
signal_rect = amplitude * signal.square(2 * np.pi * frequency * time)

# Отрисовка
plt.plot(time, signal_rect)
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.title('Прямоугольный сигнал')
plt.grid(True)
plt.show()
