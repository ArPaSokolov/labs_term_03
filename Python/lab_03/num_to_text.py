def num_to_text(number):
    # список текстовых представлений чисел до 20
    num_below_twenty = [
        '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять',
        'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
        'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
    ]
    # список текстовых представлений десятков
    dozens = [
        '', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
        'семьдесят', 'восемьдесят', 'девяносто'
    ]
    # список текстовых представлений сотен
    hundreds = [
        '', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот',
        'семьсот', 'восемьсот', 'девятьсот'
    ]

    # разбиваем число на тысячи, сотни, десятки и единицы
    hundred = (number % 1000) // 100
    dozen = (number % 100) // 10
    num = number % 10

    # формируем текстовое представление числа
    text = ''
    if hundred > 0: # сотни
        text += f'{hundreds[hundred]} '

    if dozen > 1: # десятки
        text += f'{dozens[dozen]} '

    if dozen == 1: # от 1 до 20
        text += f'{num_below_twenty[dozen * 10 + num]}'
    elif num > 0:
        text += f'{num_below_twenty[num]}'

    return text


# ввод данных
n = int(input("Enter a number from 1 to 1000 (not including 1000): "))
# проверка на то, чтобы число было от 1 до 1000 (не включая)
if 1 < n < 1000:
    number_text = num_to_text(n)
    print(number_text)
else:
    print("The number must be in the range from 1 to 1000 (not including 1000).")