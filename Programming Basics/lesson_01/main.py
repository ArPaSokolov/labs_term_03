# (1)

# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
#
# s = "{} делить на {} = {:08.2f}"
# t = s.format(a, b, a/b)
#
# t = f"{a} делить на {b} = {a/b:.0f}"
#
# print(t)

# (2)

# import math
# import math as m
from math import sin, cos, pi, radians

# x = int(input("Введите x: "))
#
# #
#
# # print(math.cos(x))
#
# # print(m.sin(x))
# # print(m.cos(x))
#
# # y = x * pi / 180
#
# y = radians(x)
#
# print(sin(y))
# print(cos(y))

from math import asin, degrees
b, a = map(int, input().split())

c = (a**2+b**2)**(1/2)
alpha = degrees(asin(a/c))
beta = degrees(asin(b/c))

print(f'AB = {c:.2f}')
print(f'∠A = {beta:.2f}°')
print(f'∠B = {alpha:.2f}°')
print(f'S = {1/2*a*b:.2f}')
print(f'r = {(a*b/(a+b+c)):.2f}')
print(f'R = {(c/2):.2f}')