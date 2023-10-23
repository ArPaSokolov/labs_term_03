# сортирует поэлементно
# каждый новый элемент "вставляется" в отсортированную часть массива
# эффективна для малых массивов или уже частично отсортированных массивов

s = list(map(int, input("Enter list of numbers: ").split()))

for i in range(1, len(s)):
    while i > 0 and s[i] < s[i - 1]:
        s[i], s[i - 1] = s[i - 1], s[i]
        i -= 1

print("Sorted list: ", *s)
