import numpy as np

x = input("Enter vector: ").split()
values, counts = np.unique(x, return_counts=True)

print("Уникальные значения:", values)
print("Количество повторений:", counts)
