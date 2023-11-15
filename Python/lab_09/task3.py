import numpy as np

# Генерация массива случайных чисел из нормального распределения
array = np.random.normal(size=(10, 4))

# Нахождение минимального значения
min_value = np.min(array)

# Нахождение максимального значения
max_value = np.max(array)

# Нахождение среднего значения
mean_value = np.mean(array)

# Нахождение стандартного отклонения
standard_deviation = np.std(array)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = array[:5, :]

print("Min:", min_value)
print("Max:", max_value)
print("Mean:", mean_value)
print("Standard deviation:", standard_deviation)
print("5 rows:")
print(first_five_rows)