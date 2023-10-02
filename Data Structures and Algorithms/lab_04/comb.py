def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

    return arr


# Пример использования
array = [9, 5, 1, 8, 3, 7, 2, 6, 4]
sorted_array = comb_sort(array)
print(sorted_array)