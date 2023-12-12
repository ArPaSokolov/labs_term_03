import openpyxl
import docxtpl

# Загрузка файла Excel
workbook = openpyxl.load_workbook("pupils.xlsx")
# Получение текущего листа с таблицей
current_list = workbook.active
# Получение строк из таблицы в виде списка списков со значениями
lines = list(current_list.values)

# Создание словаря заголовков столбцов
headings = {heading: None for heading in lines[0]}
# Создание списка записей с начальными значениями из заголовков
records = [headings.copy() for row in lines[1:]]

# Заполнение значений в записях на основе данных из строк
for i, row in enumerate(lines[1:]):
    for j, value in enumerate(row):
        records[i][lines[0][j]] = value

# Создание шаблона документа Word
file = docxtpl.DocxTemplate('template_xtpl.docx')
template = {'records': records}
# Заполнение по шаблону
file.render(template)
# Сохранение заполненного документа
file.save('Diploma_xtpl.docx')
print("'Diploma.docx' generated")
