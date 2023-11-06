import csv
import os
import random


def show(file_path, output_type='top', num_rows=5):
    with open(file_path, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
        header = data[0]
        rows = data[1:]

        if output_type == 'top':
            output_data = rows[:num_rows]
        elif output_type == 'bottom':
            output_data = rows[-num_rows:]
        elif output_type == 'random':
            if num_rows > len(rows):
                print("Not enough rows in the data.")
                return
            output_data = random.sample(rows, num_rows)
        else:
            print("Invalid output type.")
            return

        column_width = [max(len(str(row[i])) for row in output_data + [header]) for i in range(len(header))]

        for i, field in enumerate(header):
            print(field.ljust(column_width[i]), end='\t')
        print()

        for row in output_data:
            for i, value in enumerate(row):
                print(value.ljust(column_width[i]), end='\t')
            print()
        print()


def info(file_path):
    with open(file_path, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
        header = data[0]
        rows = data[1:]

        num_rows = len(rows)
        num_columns = len(header)

        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_columns}")

        for i, field in enumerate(header):
            non_empty_values = sum(1 for row in rows if row[i])

            if rows[0][i].isdigit():
                data_type = "int"
            else:
                data_type = "str"

            print("{:<10}\t{:<10}\t{:<10}".format(field, non_empty_values, data_type))
        print()


def del_nan(file_path):
    with open(file_path, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)
        header = data[0]
        rows = data[1:]

        num_rows = len(rows)
        rows_without_nan = [row for row in rows if all(field for field in row)]
        num_rows_without_nan = len(rows_without_nan)
        with open(file_path, 'w',  encoding="utf-8", newline='') as output_file:
            writer = csv.writer(output_file, delimiter=',')
            writer.writerow(header)
            writer.writerows(rows_without_nan)
        print(f"{num_rows - num_rows_without_nan} rows deleted successfully\n")


def make_ds(file_path):
    output_dir = os.path.join(os.path.dirname(file_path), 'Workdata')
    print("'Workdata' folder added")
    learning_dir = os.path.join(output_dir, 'Learning')
    print("'Learning' folder added")
    testing_dir = os.path.join(output_dir, 'Testing')
    print("'Testing' folder added")

    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    with open(file_path, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
        header = data[0]
        rows = data[1:]

        random.shuffle(rows)
        num_rows = len(rows)
        num_learning = int(num_rows * 0.7)

        learning_data = rows[:num_learning]
        testing_data = rows[num_learning:]

        learning_file_path = os.path.join(learning_dir, 'train.csv')
        testing_file_path = os.path.join(testing_dir, 'test.csv')

        with open(learning_file_path, 'w', encoding="utf-8", newline='') as learning_file:
            writer = csv.writer(learning_file)
            writer.writerow(header)
            writer.writerows(learning_data)
        print(f"'train.csv' with {num_learning} rows added")

        with open(testing_file_path, 'w', encoding="utf-8", newline='') as testing_file:
            writer = csv.writer(testing_file)
            writer.writerow(header)
            writer.writerows(testing_data)
        print(f"'test.csv' with {num_rows - num_learning} rows added\n")


file_path = input("Enter path to file to read: ")

print(("Commands \
    \n'info' to print data about the contents of the file\
    \n'show' to print rows from the file\
    \n'delnan' to delete all rows with empty fields\
    \n'ds'\
    \n'end' to finish the programm\n"))

flag = True
while flag:
    command = input("Enter command: ")
    if command == "end":
        flag = False

    if command == "show":
        num_rows = int(input("Enter how many rows to show: "))
        output_type = input(f"Enter 'top'/'bottom'/'random' to count {num_rows} rows from: ")
        show(file_path, output_type, num_rows)

    if command == "info":
        info(file_path)

    if command == "delnan":
        del_nan(file_path)

    if command == "ds":
        make_ds(file_path)
