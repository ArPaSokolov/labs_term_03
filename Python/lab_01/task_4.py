n = int(input("Enter N: "))
if n > 9:
    width = (9 + (n - 9) * 2) * 2
else:
    width = n * 2 - 1

for k in range(1, n + 1):
    x = str()
    for i in range(k, 1, -1):
        x += str(i)
    for j in range(1, k + 1):
        x += str(j)
    print(x.center(width))
    if k > 8:
        print()
print(width)