# сортирует парами
# хорошо подходит для случаев, когда большие числа находятся в начале
# фактор уменьшения интервала влияет на производительность алгоритма

s = list(map(int, input("Enter list of numbers: ").split()))

gap = len(s) - 1
while gap > 0:

    for i in range(0, len(s) - gap):
        if s[i] > s[i + gap]:
            s[i], s[i + gap] = s[i + gap], s[i]
    gap = int(gap // 1.25)

print("Sorted list: ", *s)
