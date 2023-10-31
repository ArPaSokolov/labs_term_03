import json
import csv

input_file_name = str(input("Enter a JSON file name to convert to CSV: ")[:-5]) # ввод
try:
    with open(f"{input_file_name}.json", "r") as json_f: # открываем файл для чтения
        data = json.load(json_f)
        print(f"{input_file_name}.json read") # лог в консоль

        output_file_name = str(list(data.keys())[0]) # ключ внешнего словаря = название файла

    with open(f"{output_file_name}.csv", "w", newline='') as csv_f: # открываем файл для записи
        writer = csv.writer(csv_f)

        for x in data:
            headers = data[x][0].keys() # ключи внутренних словарей = названия столбцов
            writer.writerow(headers) # запись названий столбцов
            for i in range(len(data[x])-1): # идем по списку словарей
                row = list() # новая строка в CSV "табличке"
                for header in data[x][i].keys(): # идем по ключам (названиям столбцов)
                    row.append(data[x][i].get(header)) # добавляем значение по ключу в строку
                writer.writerow(row) # запись значений

        print(f"{output_file_name}.csv written") # лог в консоль

except Exception as e:
    print(f"Error: {str(e)}") # ошибка
