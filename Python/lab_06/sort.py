def sort(lst): # сортировка выбором
    for i in range(0, len(lst)):
        for n in range(i + 1, len(lst)):
            if int(lst[n]) < int(lst[i]):
                lst[n], lst[i] = int(lst[i]), int(lst[n])
    return lst

# открываем файл с числами
input_file = open(r"sort_input.txt", "r")
print("Input file opened")
try:
    multiplication = 1
    nums = list(input_file.read().split("\n"))  # считываем первую сторку, записываем в список
    print("Input file read")
    print("Read data:", *nums)
    nums = sort(nums)
except:
    print("Smth went wrong") # ошибка
    nums = 0
finally:
    # закрываем файл с числами
    input_file.close()
    print("Input file closed")


# открываем файл для записи ответа
output_file = open(r"sort_output.txt", "w")
print("Output file opened")

try:
    # запись в файл
    for i in nums:
        output_file.write(str(i))
        output_file.write("\n")
    print("Output file updated")
    print("Written data:", *nums)
except:
    print("Smth went wrong") # ошибка
finally:
    # заткрываем файл с ответом
    output_file.close()
    print("Output file closed")
