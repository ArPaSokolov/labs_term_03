input_file = open(r"multiplication_input.txt", "r") # открываем файл с числами
print("Input file opened")
try:
    multiplication = 1
    nums = list(input_file.readline().split())  # считываем первую сторку, записываем в список
    print("Input file read")
    print("Line contents:", *nums)
    # считаем произведение
    for n in range(len(nums)):
        multiplication *= int(nums[n])
except:
    print("Smth went wrong") # ошибка
    multiplication = "Error"
finally:
    input_file.close()  # закрываем файл с числами
    print("Input file closed")

output_file = open(r"multiplication_output.txt", "w") # открываем файл для записи ответа
print("Output file opened")

try:
    # запись в файл
    output_file.write(str(multiplication))
    print("Output file updated")
except:
    print("Smth went wrong") # ошибка
finally:
    output_file.close()
    print("Output file closed") # открываем файл с ответом

