import pickle

# Чтение данных из текстового файла и формирование списка кортежей
items = []
with open('input.txt', 'r') as file:
    for line in file:
        name, price, is_sale = line.strip().split()
        price = int(price)
        is_sale = bool(int(is_sale))
        items.append((name, price, is_sale))

# Сортировка списка по названию товара
items.sort(key=lambda x: x[0])

# Запись данных в новый текстовый файл
with open('output1.txt', 'w') as file:
    for item in items:
        file.write(f"{item[0]} {item[1]} {int(item[2])}\n")

# Запись данных в новый бинарный файл
with open('output2.bin', 'wb') as file:
    pickle.dump(items, file)

# Чтение данных из бинарного файла и обработка
with open('output2.bin', 'rb') as file:
    items = pickle.load(file)

# Сортировка списка по возрастанию цены
items.sort(key=lambda x: x[1])

# Запись данных в новый текстовый файл
with open('output3.txt', 'w') as file:
    for item in items:
        file.write(f"{item[0]} {item[1]} {int(item[2])}\n")
