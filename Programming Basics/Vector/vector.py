import math

class Vector:
    def __init__(self, *coords): # конструктор
        if len(coords) == 3:
            self.x, self.y, self.z = coords
        elif len(coords) == 1:
            self.x, self.y, self.z = coords[0]
        else:
            self.x = self.y = self.z = 0

    def length(self):  # длина
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __abs__(self): # модуль
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other): # сложение
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other): # вычитание
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self): # унарный минус
        return Vector(-1 * self.x, -1 * self.y, -1 * self.z)

    def __mul__(self, other): # произведение
        if isinstance(other, int): # если число => умножение на число
            return Vector(self.x * other, self.y * other, self.z * other)

        elif isinstance(other, Vector): # если вектор => скалярное произведение
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __xor__(self, other): # векторное произведение
        new = Vector
        new.x = self.y * other.z - self.z * other.y
        new.y = self.z * other.x - self.x * other.z
        new.z = self.x * other.y - self.y * other.x
        return Vector(new.x, new.y, new.z)

    def __or__(self, other): # коллинеарность
        return self.x / other.x == self.y / other.y == self.z / other.z

    @staticmethod
    def triple_product(a, b, c): # смешанное произведение
        return a * (b ^ c)

    @staticmethod
    def are_complanar(a, b, c): # компланарность
        return Vector.triple_product(a, b, c) == 0

    def __str__(self): # вывод координат вектора
        return f"({self.x}, {self.y}, {self.z})"


# демонстрация
v1 = Vector(5, 2, 3)
v2 = Vector(3, 1, 2)
print("v1 =", v1)
print("v2 =", v2)
print("length v1 =", Vector.length(v1))
print("length v2 =", Vector.length(v2))
print()

print("v1 =", v1)
print("v2 =", v2)
v3 = v1 + v2
print("v3 = v1 + v2 =", v3)
print()

print("v1 =", v1)
print("v2 =", v2)
v3 = v1 - v2
print("v3 = v1 - v2 =", v3)
print()

print("v1 =", v1)
v4 = -v1
print("-v1 =", v4)
print()

print("v1 =", v1)
print("v2 =", v2)
v3 = v1 * v2
print("v3 = v1 * v2 =", v3)
print()

print("v1 =", v1)
v3 = v1 * 2
print("v3 = v1 * 2 =", v3)
print()

print("v1 =", v1)
print("v2 =", v2)
print("Are v1, v2, v3 collinear:", v1 | v2)
print()

print("v1 =", v1)
print("v2 =", v2)
print("v3 =", v3)
print("Triple product v1, v2, v3 =", Vector.triple_product(v1, v2, v3))
print()

print("v1 =", v1)
print("v2 =", v2)
print("v3 =", v3)
print("Are v1, v2, v3 complanar:", Vector.are_complanar(v1, v2, v3))
