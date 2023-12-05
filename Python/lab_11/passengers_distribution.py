import matplotlib.pyplot as plt
import csv
from datetime import datetime

# Чтение файла
data = []
with open('passengers.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропуск заголовка
    for row in csv_reader:
        date = datetime.strptime(row[0], '%Y-%m')
        passengers = int(row[1])
        data.append((date, passengers))

# Линейный график пассажиропотока за все время
x = [i[0] for i in data]
y = [i[1] for i in data]

# Гистограмма пассажиров по месяцам в 1951-1955 гг.
selected_data = [i for i in data if i[0].year in range(1951, 1956)]
months = [i[0].strftime('%Y-%m') for i in selected_data]
passengers = [i[1] for i in selected_data]

# Два графика в одном окне
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))

# График
axs[0].plot(x, y)
axs[0].set_xlabel('Год')
axs[0].set_ylabel('Число пассажиров')
axs[0].set_title('За все время')
axs[0].tick_params(axis='both', which='major', labelsize=5)

# Гистограмма
axs[1].bar(months, passengers)
axs[1].set_xlabel('Год-месяц')
axs[1].set_ylabel('Число пассажиров')
axs[1].set_title('По месяцам 1951-1955 гг')
axs[1].tick_params(rotation=45, axis='both', which='major', labelsize=5)

plt.show()
