n = int(input("Enter N: "))
f = 0
# while f <= n:
#     x = []

for k in range(1, n + 1):
    for i in range(1, k + 1):
        print(i, end=" ")
    for i in range(k - 1, 0, -1):
        print(i, end=" ")
    print()

    # for i in range(1, f, -1):
    #     x.append(i)
    # for j in range(1, f):
    #     x.append(j)
    # print(x)
    # f += 1
