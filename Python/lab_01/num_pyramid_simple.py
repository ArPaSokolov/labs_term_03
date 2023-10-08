n = int(input("Enter N: "))
width = n * 2 - 1

for k in range(1, n + 1):
    x = str()
    x += " " * (width - k)
    for i in range(k, 1, -1):
        x += str(i)
    for j in range(1, k + 1):
        x += str(j)
    print(x)