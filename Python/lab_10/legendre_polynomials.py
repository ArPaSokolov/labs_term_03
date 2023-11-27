import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

def plot_legendre_polynomials():
    x = np.linspace(-1, 1, 100)  # Входные значения x для построения графика
    degrees = range(1, 8)  # Степени полиномов Лежандра для построения

    # Создание фигуры и осей для графика
    fig, ax = plt.subplots()

    # Построение графиков полиномов Лежандра различных степеней
    for degree in degrees:
        y = legendre(degree)(x)  # Вычисление значений полинома Лежандра степени degree
        ax.plot(x, y, label=f'n = {degree}')  # Построение графика с легендой

    # Добавление заголовка и легенды на график
    ax.set_title('Полиномы Лежандра')
    ax.legend()

    # Отображение графика
    plt.show()

# Вызов функции для построения графиков полиномов Лежандра
plot_legendre_polynomials()
