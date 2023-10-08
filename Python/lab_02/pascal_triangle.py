n = int(input("Enter a depth of the Pascal triangle: ")) # вводим количество строчек в треугольнике Паскаля

triangle = [[1] + [0] * n for i in range(n + 1)] # заполняем первый столбец матрицы N*N единицами, остальное - нулями

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1] # получаем текущий элемент из суммы двух стоящих сверху

for i in triangle:
    new_i = [j for j in i if j != 0] # получаем новые строки без нулей
    print(*new_i, sep="\t") # выводим тр Паскаля
