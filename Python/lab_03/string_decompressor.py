def decompress(string):
    decompressed_string = "" # восстановленная строка
    multiplier = "" # множитель

    for i in string:
        # если элемент - число
        if i in "0123456789":
            multiplier += i
        # если элемент - буква
        else:
            # если множитель есть
            if multiplier:
                decompressed_string += i * int(multiplier) # выплевываем буквы multiplier раз
                multiplier = "" # обновляем множитель
            else:
                decompressed_string += i # множителя нет, выплевываем одну букву

    return decompressed_string


# Ввод данных
input_string = input("Enter a string to decompress: ")
# Вывод данных
print("Decompressed string:", decompress(input_string))
