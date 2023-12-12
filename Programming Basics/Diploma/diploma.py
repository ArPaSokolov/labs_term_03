from docx import Document
import openpyxl
from docxtpl import DocxTemplate

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

context = {
    "records": []
}

# Заполнение значений в записях на основе данных из строк
for i, row in enumerate(lines[1:]):
    context["records"].append(row)

doc = DocxTemplate('template.docx')

doc.render(context)
doc.save('Diploma.docx')