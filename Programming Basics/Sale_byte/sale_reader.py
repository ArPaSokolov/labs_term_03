# Читаем данные из исходного текстового файла
data = []
with open('sales.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if len(line) == 0: # если конец файла
            break
        elements = line.split()  # Разделяем строку по пробелам
        name = elements[0]
        price = int(elements[1])
        if elements[2] == '1':
            sale = bool(int(elements[2]))
        else:
            sale = bool(0)
        item = (name, price, sale)
        data.append(item)

# Сортируем данные по названию товара в алфавитном порядке
sorted_data = sorted(data, key=lambda x: x[0])

# Записываем отсортированные данные в новый текстовый файл
with open('sales_alphabet.txt', 'w', encoding='utf-8') as file:
    for item in sorted_data:
        line = f"{item[0]} {item[1]} {item[2]}\n"
        file.write(line)

# Записываем отсортированные данные в новый бинарный файл
with open('sales_alphabet.bin', 'wb') as file:
    for name, price, sale in sorted_data:
        name_bytes = name.encode('utf-8')

        n = len(name_bytes)
        size = n.to_bytes(4, "little")

        price_bytes = price.to_bytes(4, "little")
        sale_bytes = sale.to_bytes(1, "little")
        file.write(size + name_bytes + price_bytes + sale_bytes)

# Читаем данные из полученного бинарного файла
with open("sales_alphabet.bin", "rb") as file:

    data = []
    while file:
        size = int.from_bytes(file.read(4), "little")
        if not size:
            break

        name = str(file.read(size), "utf-8")
        price = int.from_bytes(file.read(3), "little")
        sale = bool.from_bytes(file.read(2), "little")
        item = (name, price, sale)
        data.append(item)

# Сортируем данные по возрастанию цены
sorted_data_by_price = sorted(data, key=lambda x: x[1])

# Записываем отсортированные данные в новый текстовый файл
with open('sales_price.txt', 'w', encoding='utf-8') as file:
    for item in sorted_data_by_price:
        line = f"{item[0]} {item[1]} {item[2]}\n"
        file.write(line)
