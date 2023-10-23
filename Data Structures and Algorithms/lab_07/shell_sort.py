# сортировки вставками с постепенно уменьшающимся шагом
# сначала сортирует элементы на удаленных позициях, что помогает сделать часть массива частично отсортированной
# тем самым уменьшиает количество сдвигов и сравнений элементов в последующей фазе сортировки

s = list(map(int, input("Enter list of numbers: ").split()))

n = len(s)
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = s[i]
        j = i
        while j >= gap and s[j - gap] > temp:
            s[j] = s[j - gap]
            j -= gap
        s[j] = temp
    gap //= 2

print("Sorted list: ", *s)
