# ищем какое количество раз встречался символв
def search(string):
    lst = list(string) # преобразуем строку в список
    lst = [symbol.lower() for symbol in lst] # все прописные буквы делаем строчными

    symbol_set = set(lst) # превращаем список в множество, чтобы оставить каждый символ только один раз
    symbol_set.discard(" ") # по заданию не учитываем пробелы

    symbol_count = [] # список для хранения символов
    symbol_lst = [] # список для хранения количества повторений символов

    # бежим по множеству
    for symbol in symbol_set:
        symbol_count.append(lst.count(symbol)) # считаем количество повторений и кладем в список
        symbol_lst.append(symbol) # кладем в список символ, для которого считали повторения

    return symbol_count, symbol_lst


# сортируем пузырьком символы по количеству повторений
def bubble_sort(m_symbol_count, m_symbol_lst):
    n = len(m_symbol_count)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # меняем местами символы так же как и количество повторений
            if m_symbol_count[j] < m_symbol_count[j + 1]:
                m_symbol_count[j], m_symbol_count[j + 1] = m_symbol_count[j + 1], m_symbol_count[j]
                m_symbol_lst[j], m_symbol_lst[j + 1] = m_symbol_lst[j + 1], m_symbol_lst[j]

    return m_symbol_lst, m_symbol_count


# ввод данных
input_string = input("Enter a string to search: ")

# сортировка символов по количеству повторений
count, symbols = search(input_string)
sorted_symbols, sorted_count = bubble_sort(count, symbols)

# вывод
if len(sorted_symbols) == 3: # если набралось 3
    # топ 3 самых повторяющихся символов
    for i in range(3):
        print(f"Symbol '{sorted_symbols[i]}' was met {sorted_count[i]} times") # вывод данных
else:
    # выводим столько, сколько набралось
    for i in range(len(sorted_symbols)):
        print(f"Symbol '{sorted_symbols[i]}' was met {sorted_count[i]} times")  # вывод данных
