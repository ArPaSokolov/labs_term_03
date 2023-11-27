import numpy as np
import matplotlib.pyplot as plt

# Создание данных для графиков
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z1 = X**2 + Y**2  # MSE
Z2 = np.log10(Z1)  # MSE с логарифмическим масштабом

# Первый график без логарифмического масштаба
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('MSE')
ax1.set_title('MSE')

# Второй график с логарифмическим масштабом
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(MSE)')
ax2.set_title('MSE (в логарифмическом масштабе)')

plt.subplots_adjust(wspace=1, left=0.1, right=0.8)
plt.show()
