#----------------------------------------------Декоратор-------------------------------------------#
#Входной параметр ФУНКЦИЯ, выходное тоже функция
#Пример 1
# def decor(func): #Функция внутри функции
#     def wrapper(a,b):
#         print("Прелюдия")
#         print(func(a, b))
#         print("Занавес")
#     return wrapper
#
# @decor  #Сразу применить decor к summa
# def summa(x, y):
#     return x + y
#
#
# # new_summa = decor(summa)  #new_summa - новая функция   Если есть @decor над названием функции то так лучше не делать
# # new_summa(10, 20)
#
# summa(10, 20)

#Пример 2
# def protect(password):  #До связи Арсений если ты будешь это читать
#     def decor(func):
#         pwd = input("Введите пароль: ")
#         if pwd == password:
#             def wrapper(a, b):
#                 print("Прелюдия")
#                 print(func(a, b))
#                 print("Занавес")
#             return wrapper
#         else:
#             def do_nothing(a, b):
#                 print('Надо было вводить правильный пароль!')
#             return do_nothing
#     return decor
#
#
# @protect('12345abc')
# def summa(a, b):
#     return a + b
#
#
# summa(10, 20)
# summa(50, 60)
#-----------------------------------------Побитовые записи----------------------------------------------------#
# A = [240, 86, 21, 255, 0, 128, 192] #В диапазоне [32; 127] будут выдаваться символы аски таблицы
# B = bytes(A) #Не изменяемые массив
# print(B)
#
# n = len(B)
# print(n)
#
# B = bytearray(A) #Можно менять
# print(B)
#
# B[2] = 100
# print(B)
#
# B.append(40)
# print(B)
#Примеры
# x = 987654
# A = []
# while x > 0: #Получаем число в битовой записи
#     A.append(x % 256)
#     x = x// 256
# print(A)
# B = bytes(A)
# print(B)
#
# y = 0
# r = 1
# for b in B: #Перевод из байтов в число
#     y += b * r
#     r *= 256
#
# print(y)
#Новый пример
# x = 987654
# B =x.to_bytes(4, "little") #Что-то типо соритировок
# print(B)
# C =x.to_bytes(4, "big")
# print(C)
#
# D = int.from_bytes(B, "little") #Восстановление из битовой записи в интовую
# print(D)
#Новый пример
# s = 'Фэйсом об table.'
# for x in s: #Значения символов в таблице Unicode
#     print(ord(x), end=' ')
#
# for x in s: #Где второй нолик значит занимает символ один байт (Хз к чему это)
#     n = ord(x)
#     print(n % 256, n // 256, end=' ')
#Я уже не знаю что это
# s = 'Фэйсом об table.'
# A = []
# for x in s:
#     A.append(ord(x) % 256)
#     A.append(ord(x) // 256)
# print(A)
# print(bytes(A))

#Значения символов в utf-8
# s = 'Фэйсом об table.'
# print(s.encode("utf-8")) #В utf-8. Сама строка при это не меняется
#
# B = s.encode("utf-8")
# print(str(B, "utf-8")) #Из utf-8

#Всё, до связи.
#upd: Я ничего не понимаю, так что удачи
#upd: Мы тут вроде загружали информацию в виде байтов
# A = [
#     ("Гречка", 95, 2), #Буквы занимают 2 байта, а пробел 1 байт
#     ("Огурцы", 55, 3),
#     ("Пиво", 119, 5),
#     ("Хлеб", 49, 3),
#     ("Шоколад Аленка", 100, 2)
# ]
#
# fin = open("Продукты.bin", "wb", ) #Сначала название, потом wb - открыть как бинарный на запись
#
# n = len(A)
# B = n.to_bytes(4, "little")
# fin.write(B)
#
# for name, price, quantity in A:
#     B = name.encode("utf-8")
#     size = len(B)
#     C = size.to_bytes(4, "little")
#     fin.write(C)
#     fin.write(B)
#
#     B = price.to_bytes(4, "little")
#     fin.write(B)
#
#     B = quantity.to_bytes(4, "little")
#     fin.write(B)
#
# fin.close()
#Делаем обратное (читаем из бинарного файла)
#upd: Нахуй оно нам надо
# A = [
#     ("Гречка", 95, 2), #Буквы занимают 2 байта, а пробел 1 байт
#     ("Огурцы", 55, 3),
#     ("Пиво", 119, 5),
#     ("Хлеб", 49, 3),
#     ("Шоколад Аленка", 100, 2)
# ]
# fin = open("Продукты.bin", "rb")
#
# B = fin.read(4)
# n = int.from_bytes(B, "little")
#
# for _ in range(n):
#     C = fin.read(4)
#     size = int.from_bytes(C, "little")
#     B = fin.read(size)
#     item = str(B, "utf-8")
#
#     B = fin.read(4)
#     price = int.from_bytes(B, "little")
#
#     B = fin.read(4)
#     quantity = bool.from_bytes(B, "little")
#
#     print(item, price, quantity)
# fin.close()