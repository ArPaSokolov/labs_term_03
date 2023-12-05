import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000

# Генерация выборки из нормального распределения
samples = np.random.normal(mean, std_dev, num_samples)

# Отрисовка нормального распределения
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.title('Нормальное распределение')
plt.hist(samples, bins=100, density=True, alpha=0.75)
plt.show()
