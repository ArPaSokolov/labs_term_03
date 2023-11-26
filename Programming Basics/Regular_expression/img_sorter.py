import os
import re
import shutil
import random

# Получение пути к текущей папке программы
current_folder = os.path.dirname(os.path.abspath(__file__))

# Путь к папке с изображениями
image_folder = os.path.join(current_folder, "")

# Создание регулярного выражения для извлечения информации из названия файла
pattern = r"(\d{1,3})-(\d{1,2})-(\d{2})-\d+\.jpg"
count = 0 # счетчик сортировок

# Перебор файлов в папке
for filename in os.listdir(image_folder):
    full_path = os.path.join(image_folder, filename)

    # Проверка, является ли файл JPEG изображением
    if filename.endswith(".jpg"):

        # Извлечение информации из названия файла
        match = re.match(pattern, filename)
        if match:
            count += 1
            if count == 1:
                print("Сортровка началась...")
            number = match.group(1)  # Номер из названия файла (одно-, двух- или трехзначный)
            month, year = match.group(2, 3)  # День, месяц, год из названия файла

            date = input(f"Для газеты №{number} от {month}/{year} введите дату: ")

            name = f"{number}-{31}-{month}-{year}"

            # Создание пути к папке назначения
            destination_folder = os.path.join(image_folder, name)

            # Создание папки, если она не существует
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Перемещение файла в папку назначения
            shutil.move(full_path, os.path.join(destination_folder, filename))

if count == 0:
    print("Сортировка не требуется!")
else:
    print("Сортировка закончена!")

