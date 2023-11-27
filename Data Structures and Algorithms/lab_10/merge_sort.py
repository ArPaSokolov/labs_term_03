# Выполняет слияние двух отсортированных списков left и right в один отсортированный список.
# Создает пустой список merged и устанавливает начальные индексы для left (left_index) и right (right_index).
# Затем сравнивает элементы с текущими индексами в left и right и добавляет меньший элемент в список merged.
# После этого индекс выбранного элемента увеличивается на 1.
# Этот процесс продолжается, пока не будут перебраны все элементы в обоих списках.
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Находит середину списка (mid) и разделяет его на две половины: левую (left_half) и правую (right_half).
# Затем рекурсивно вызывает merge_sort для каждой половины, чтобы отсортировать их.
# Наконец, вызывает функцию merge для объединения отсортированных половинок в один отсортированный список.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


array = list(map(int, input().split()))
sorted_array = merge_sort(array)
print(sorted_array)