import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

# Находим индексы элементов, перед которыми стоит нулевой
indices = np.where(x[:-1] == 0)[0]

elements = x[indices + 1]
max_element = np.max(elements)

print("Max:", max_element)
