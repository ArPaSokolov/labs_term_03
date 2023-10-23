input_file = open(r"kids_input.txt", "r", encoding='utf-8') # открываем файл с числами
print("Input file opened")

try:
    kids = input_file.readlines()  # считываем первую сторки
    print("Input file read")
    print("File contents: \n", *kids) # выводим данные построчно в консоль
    data = []
    for kid in kids: # идем по строкам
        if kid:
            last_name, first_name, age = kid.split()
            data.append((last_name, first_name, int(age))) # записываем данные
    max_data = max(data, key=lambda x: x[2]) # находим максимальный возраст
    min_data = min(data, key=lambda x: x[2]) # находим минимальный возраст

except:
    print("Smth went wrong") # ошибка
    max_data = 0
    min_data = 0
finally:
    input_file.close()  # закрываем файл
    print("Input file closed")

# самый старший

output_file_e = open('kids_eldest.txt', 'w', encoding='utf-8')
print("Output file 1 opened")
try: # запись в файл
    output_file_e.write(f"Фамилия: {max_data[0]}\n")
    output_file_e.write(f"Имя: {max_data[1]}\n")
    output_file_e.write(f"Возраст: {max_data[2]}\n")
    print("Output file 1 changed")
except:
    print("Smth went wrong") # ошибка
finally:
    output_file_e.close()
    print("Output file 1 closed") # закрываем файл

# самый младший

output_file_y = open('kids_youngest.txt', 'w', encoding='utf-8')
print("Output file 2 opened")
try: # запись в файл
    output_file_y.write(f"Фамилия: {min_data[0]}\n")
    output_file_y.write(f"Имя: {min_data[1]}\n")
    output_file_y.write(f"Возраст: {min_data[2]}\n")
    print("Output file 2 changed")
except:
    print("Smth went wrong") # ошибка
finally:
    output_file_y.close()
    print("Output file 2 closed") # закрываем файл