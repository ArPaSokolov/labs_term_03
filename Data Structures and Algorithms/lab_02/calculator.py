def check(m_lst):
    brackets = []           # стек для хранения открывающих скобок
    if len(m_lst) > 2 and m_lst[-2] in '+-*/':
        raise ValueError("Некорректный ввод!")

    for i in m_lst:
        if '+)' in ''.join(m_lst) or '-)' in ''.join(m_lst) or '*)' in ''.join(m_lst) or '/)' in ''.join(m_lst):
            raise ValueError("Некорректный ввод!")
        if i in '([{':              # если символ - открывающая скобка, добавляем ее в стек
            brackets.append(i)
        elif i in ')]}':            # если символ - закрывающая скобка:
            if not brackets:            # стек пуст, закрывающая скобка без пары
                raise ValueError("Некорректный ввод!")
            if (i == ')' and brackets[-1] == '(') or (i == ']' and brackets[-1] == '[') or (i == '}' and brackets[-1] == '{'):
                                        # если закрывающая скобка и верхний элемент стека образуют пару,
                                        # удаляем верхний элемент стека
                brackets.pop()
    if brackets:
        raise ValueError("Некорректный ввод!") # осталась скобка без пары
def evaluate_rpn(m_lst):
    stack_number = []
    stack_symbol = []
    fool = 0                  # счетчик на идущие подряд знаки
    for item in m_lst:
        if item in '1234567890':        # если символ - число
            stack_number.append(int(item))
            fool = False

        elif item in '+-':            # если символ - плюс или минус
            fool += 1
            if len(stack_symbol) == 0:      # если стек со знаками пуст
                stack_symbol.append(item)
            else: # в стеке что-то есть
                while len(stack_symbol) != 0 and stack_symbol[-1] in '+-*/':
                    # извлекаем из стека со знаками все, что имеет равный или больший приоритет
                    stack_number.append(stack_symbol[-1])
                    stack_symbol.pop()
                    # положим сверху текущий знак
                stack_symbol.append(item)

        elif item in '*/':            # если символ - произведение или деление
            fool += 1
            if len(stack_symbol) == 0 or stack_symbol[-1] in '+-':  # если стек со знаками пуст или содержит знаки меньшего приоритета
                stack_symbol.append(item)
            else:                                                   # если содержит знаки равного приоритета
                while len(stack_symbol) != 0 and stack_symbol[-1] in '*/':
                    # извлекаем из стека со знаками все, что имеет равный или меньший приоритет
                    stack_number.append(stack_symbol[-1])
                    stack_symbol.pop()
                stack_symbol.append(item)

        elif item == '(':             # если символ - (
            # сразу после скобки знака быть не может
            stack_symbol.append(item)
        elif item == ')': # если символ - )
            while stack_symbol[-1] != '(':
                stack_number.append(stack_symbol[-1])
                stack_symbol.pop()
            stack_symbol.pop()

        elif item == '=':             # если символ - равно
            while len(stack_symbol) != 0:    # символы закончились - извлекаем остатки стека
                stack_number.append(stack_symbol[-1])
                stack_symbol.pop()
        if fool > 1: # больше одного знака подряд
            raise ValueError("Некорректный ввод!")
    print(stack_number)
    return stack_number

def calculate(m_lst):
    stack = []  # стек для хранения чисел
    for item in m_lst:
        if item == '+':
            b = stack.pop()
            a = stack.pop()
            result = a + b
            stack.append(result)
        elif item == "-":
            b = stack.pop()
            a = stack.pop()
            result = a - b
            stack.append(result)
        elif item == "*":
            b = stack.pop()
            a = stack.pop()
            result = a * b
            stack.append(result)
        elif item == "/":
            b = stack.pop()
            a = stack.pop()
            if int(b) == 0:
                raise ValueError("Деление на ноль!")
            else:
                result = a / b
                stack.append(result)
        else:
            stack.append(int(item))

    return stack

lst = list(input("Введите пример: ")) # вводим строку
try:
    check(lst)
    print(calculate(evaluate_rpn(lst)))
except ValueError as e:
    print(e)