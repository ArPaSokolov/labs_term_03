x = int(input("Введите верхнюю границу: "))
mas = []
for c in range (0, 100):
    for b in range(0, 100):
        for a in range(0, 100):
            t = 3 ** a * 5 ** b * 7 ** c
            if t <= x:
                mas.append(t)
            else:
                break
print("Числа:", sorted(mas))