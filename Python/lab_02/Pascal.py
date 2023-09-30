n = int(input("Введите глубину: "))


triangle = [[1] + [0] * n for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

for i in triangle:
    new_i = [j for j in i if j != 0]
    print(*new_i, sep="\t")
