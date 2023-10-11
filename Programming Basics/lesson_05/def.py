def exp_1_digits(n):
    global base
    while n > 0:
        print(n % base)
        n = n // base
    base += 1


def exp_2_digits(n, base):
    s = 0
    while n > 0:
        d = n % base
        s += d
        n = n // base
    return s


def exp_3_sum_and_pro(n, base):
    s = 0
    p = 1
    while n > 0:
        d = n % base
        s += d
        p *= d
        n = n // base
    return s, p


def exp_4_digits(n, base):
    A = []
    while n > 0:
        d = n % base
        A.append(d)
        n = n // base
    return A[::-1]


def exp_5_digits(n, base):
    while n > 0:
        d = n % base
        A.append(d)
        n = n // base


def exp_6_append():
    n = 0
    while n <= 100_000_000_000: # ломается!!!!
        A.append(n)
        n += 1


print("================== Experiment 1 ====================")
base = 8
exp_1_digits(123456)
print("base = ", base)
print()

print("================== Experiment 2 ====================")
y = exp_2_digits(123456, 8)
print("y = ", y)
print()

print("================== Experiment 3 ====================")
a, b = exp_3_sum_and_pro(123456, 8)
print("sum = ", a, "pro = ", b)
print()

print("================== Experiment 4 ====================")
D = exp_4_digits(123456, 8)
print("D = ", D)
print()

print("================== Experiment 6 ====================") # фокусы
A = []
exp_5_digits(123456, 8)
print("A = ", A)
print()

print("================== Experiment 5 ====================")
print("A1 = ", id(A))
exp_6_append()
print("A2 = ", id(A))
print()
