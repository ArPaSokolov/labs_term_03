def compress(string):

    compressed_string = "" # сжатая строка
    count = 1 # счетчик элементов

    for i in range(1, len(string)):
        # если буква повторяется
        if string[i] == string[i - 1]:
            count += 1
        # если буква не повторяется и счетчик больше одного
        elif count > 1 and string[i] != string[i - 1]:
            compressed_string += string[i - 1]
            compressed_string += str(count)
            count = 1
        # если буква не повторяется и счетчик равен одному
        elif count == 1 and string[i] != string[i - 1]:
            compressed_string += string[i - 1]
            count = 1
    # выплевываем последнюю букву
    if count == 1: # если счетчик равен одному
        compressed_string += string[i]
    else: # если счетчик больше одного
        compressed_string += string[i]
        compressed_string += str(count)

    return compressed_string


# ввод данных
input_string = input("Enter a string to compress: ")
# вывод данных
print("Compressed string: ", compress(input_string), sep="")
