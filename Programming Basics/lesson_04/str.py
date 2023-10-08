#================== str ======================#

s = "Мама мыла раму"
print("s = ", s)
print("len(s) = ", len(s))
print("s[0] = ", s[0])
try:
    print("s[1] = 'f'", end=" : ")
    s[1] = "f"
except:
    print("TypeError: objet does not support item assignment")
print()

A = "ABC"
B = "DEF"
print("A = ", A)
print("B = ", B)
print()

C = A + B
print("A + B = ", C)

#================== преобразование ======================#
L1 = ["Мама", "мыла", "раму"]
S = "_!_".join(L1)
print(S)
print()

L2 = [100, 200, 300]
S = "_!_".join(map(str, L2))
print(S)