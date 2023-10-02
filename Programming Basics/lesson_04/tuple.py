#================= tuple =====================#

C = (100, 200, 300)                    # кортеж
print(type(C))
print(C)
print()

B = [101, 202, 303]
print(type(B))
print(B)
print()

A = tuple(B)
print(type(A))
print(A)
print()

a, b, *c = 10, 20, 30, 40, 50
print(a, b, c)
print()

*a, b, c = 10, 20, 30, 40, 50
print(a, b, c)
print()

a, *b, c = 10, 20, 30, 40, 50
print(a, b, c)
print()