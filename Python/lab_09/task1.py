# try:
#     with open("matrix.txt", "r",  encoding='utf-8') as f: # открываем файл для чтения
#         x = []
#         summ = 0
#         for line in f:
#             for num in line.split(','):
#                 x.append(int(num))
#                 summ += int(num)
#         print("Sum =", summ, "\nMax =", max(x),"\nMin =", min(x))
# except Exception as e:
#     print(e)


import numpy as np

try:
    matrix = np.loadtxt('matrix.txt', 'int', delimiter=',')
    sum_of_elements = np.sum(matrix)
    max_element = np.max(matrix)
    min_element = np.min(matrix)

    print("Sum:", sum_of_elements)
    print("Max:", max_element)
    print("Min:", min_element)

except Exception as e:
    print(e)
