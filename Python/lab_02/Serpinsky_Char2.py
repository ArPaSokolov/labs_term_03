H = 34
W = 67

M = [[' '] * W for _ in range(H)]

M[1][W//2] = '*'
for i in range(H):
    for j in range(W):
        if j < (W - 1) and (M[i - 1][j - 1] == '*' and M[i - 1][j + 1] == ' ' or
                            M[i - 1][j + 1] == '*' and M[i - 1][j - 1] == ' '):
            M[i][j] = '*'
        if i == H - 1:
            M[i][j] = ' '
for i in range(H):
    for j in range(W):
        if (M[i][j - 1] == '*' and M[i][j + 1] == '*') and \
                (M[i][j - 2] == ' ' and M[i][j + 2] == ' '):
            M[i][j] = '*'

for x in M:
    print(*x)