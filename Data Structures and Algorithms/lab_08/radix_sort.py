# сортирует элементы путем сравнения их разрядов, начиная с младших разрядов и двигаясь к старшим
# эффективно справляется числами, представленных в виде цифровых последовательностей (например, целых чисел или строк)

s = list(map(int, input("Enter list of numbers: ").split()))

# сортируем массив по текущему разряду
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


print("Sorted list: ", *radix_sort(s))
