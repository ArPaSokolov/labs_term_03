import random

number1 = random.randint(1, 100)  # Генерируем число
number2 = random.randint(1, 100)

print(f"Получите число {number2}")
print("Из:", number1)

while True:
    a = random.randint(1, 10)
    b = random.randint(-10, -1)
    print("Выберите одно из действий:")
    print(f"1. Изменить число на {a}")
    print(f"2. Изменить число на {b}")
    print("3. Выйти из игры")

    choice = input("Введите номер действия: ")

    if choice == "1":
        number1 += a
        print(f"Число изменено на {a}.")
    elif choice == "2":
        number1 += b
        print(f"Число изменено на {b}.")
    elif choice == "3":
        print("Вы вышли из игры.")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
    if number2 == number1:
        print("Победа.")
        break
    else:
        print("Число:", number1)

    print()  # Пустая строка для разделения ходов
