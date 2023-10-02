a = int(input("Введите a: "))
b = int(input("Введите b: "))

s = "{} делить на {} = {:08.2f}"
t = s.format(a, b, a/b)

t = f"{a} делить на {b} = {a/b:.0f}"

print(t)