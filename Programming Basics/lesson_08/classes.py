# ----------------------Наследование-----------------------------#
class Human:
    def __init__(self, fn, ln, yb):
        self.firstname = fn
        self.lastname = ln
        self.birthyear = yb

    def get_age(self):
        return 2023 - self.birthyear

    def __str__(self):
        return f'{self.firstname} {self.lastname}, {self.birthyear} г.р.'


class Student(Human):
    def __init__(self, fn, ln, yb, sp, gr):
        super().__init__(fn, ln, yb)  # Берёт из родительского
        self.speciality = sp
        self.grade = gr

    def __str__(self):
        return super().__str__() + '\n' \
            + f"{self.speciality} {self.grade}"  # Часть берёт из родительского


class MatOb(Student):
    def __init__(self, fn, ln, yb, gr):
        super().__init__(fn, ln, yb, "МОАИС", gr)
        self.grade = gr


a = Human('Олег', 'Полковский', 1987)
print(a)
print(a.get_age())

b = Student('Демид', 'Гвозденко', 2004, 'МатОб', 2)
print(b)
print(b.get_age())

c = MatOb('Арсений', 'Соколов', 2004, 2)
print(c)
print(c.get_age())
