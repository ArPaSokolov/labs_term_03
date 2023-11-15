import numpy as np

a = np.arange(16).reshape(4, 4)
print("Old:")
print(a)

a[[0, 2]] = a[[2, 0]]

print("New:")
print(a)
