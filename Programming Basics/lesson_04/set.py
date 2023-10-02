#================== set ======================#

A = {100, 200, 300, "eee"}                # множество
print(type(A))
print(len(A))
print(A)
print()

B = {100, 200, 300, "eee", 100, "eee"}
print(type(B))
print(len(B))
print(B)
print()

C = {}                                    # словарь, а не множество
print(type(C))
print()

D = set()                                 # множество
print(type(D))
print()

if "eee" in A:
    print("'eee' есть в множестве А")
    print()

if 100 in A:
    A.discard(100)
    print("100 был удален")
    print()

print("Множество:")
for x in A:
    print(x)
print()


print("Множество:")
A.add(700)
for x in A:
    print(x)
print()

#========== операции над множествами ==========#

A = {100, 200, 300, 400}
B = {300, 400, 500, 600}
print("A = ", A)
print("B = ", B)
print()

C = A & B
print("A & B = ", C)
print()

C = A | B
print("A | B = ", C)
print()

C = A - B
print("A - B = ", C)
print()

C = A ^ B
print("A ^ B = ", C)
print()

D = {100, 200, 300}
E = {100, 200, 300}
F = {200, 300}
G = {200, 300, 400, 500}
print("D = ", D)
print("E = ", E)
print()

print("D == E = ", D == E)
print()

print("D > E = ", D > E)
print()

print("D < E = ", D < E)
print()

print("D = ", D)
print("F = ", F)
print()

print("D == F = ", D == F)
print()

print("D > F = ", D > F)
print()

print("D < F = ", D < F)
print()

print("D = ", D)
print("G = ", G)
print()

print("D == G = ", D == G)
print()

print("D > G = ", D > G)
print()

print("D < G = ", D < G)
print()