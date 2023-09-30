# H = 34
# W = 67
#
# M = [[' '] * W for _ in range(H)]
#
# M[1][W//2] = '*'
# for i in range(H):
#     for j in range(W):
#         if j < (W - 1) and (M[i - 1][j - 1] == '*' and M[i - 1][j + 1] == ' ' or
#                             M[i - 1][j + 1] == '*' and M[i - 1][j - 1] == ' '):
#             M[i][j] = '*'
#         if i == H - 1:
#             M[i][j] = ' '
# for i in range(H):
#     for j in range(W):
#         if (M[i][j - 1] == '*' and M[i][j + 1] == '*') and \
#                 (M[i][j - 2] == ' ' and M[i][j + 2] == ' '):
#             M[i][j] = '*'
#
# for x in M:
#     print(*x)

n = int(input("Enter a depth of the Serpinsky triangle: "))

n = (3 ** n) - 1
triangle = [[1] + [0] * n for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = (triangle[i - 1][j] + triangle[i - 1][j - 1]) % 3

for i in range(0, n + 1):
    for j in range(0, n + 1):
        if triangle[i][j] == 1 or triangle[i][j] == 2:
            triangle[i][j] = "*"
        else:
            triangle[i][j] = " "

for x in triangle:
    print(*x)
