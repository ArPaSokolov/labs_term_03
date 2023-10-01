n = int(input("Enter a depth of the Serpinsky triangle: "))

n = (2 ** n) - 1 # каждые 2 ** n строчек в тр Паскаля = 1 уровень глубины в тр Серпинского

p_triangle = [[1] + [0] * n for i in range(n + 1)]  # создаем матрицу под тр Паскаля
s_triangle = [[""] * (n + 1) for x in range(n + 1)] # создаем матрицу под тр Серпинского

for i in range(1, n + 1):
    for j in range(1, i + 1):
        p_triangle[i][j] = (p_triangle[i - 1][j] + p_triangle[i - 1][j - 1]) % 2 # заполняем тр Паскаля 1 и 0

for i in range(0, n + 1): # заполняем матрицу для тр Серпинского
    for j in range(0, n + 1):
        if p_triangle[i][j] == 1: # любая единица или двойка в тр Паскаля = * в тр Серпинского
            s_triangle[i][j] = "*"
        else:
            s_triangle[i][j] = " " # иначе - пробел

for x in s_triangle: # выводим тр Серпинского
    print(*x)