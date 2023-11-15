import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, 4]  # Извлекаем столбец "species"
unique_species = np.unique(species)  # Находим уникальные значения
count_species = len(unique_species)  # Количество уникальных значений

print("Unique 'species':", unique_species)
print("Amount:", count_species)
