# Множественное наследование
class A:
    def foo(self):
        print("метод фу")

    def hello(self):
        print("класс А")

class B:
    def bar(self):
        print("метод бар")

    def hello(self):
        print("класс Б")


class C(A, B): # <------ что стоит первым, то первым и выводится
    def abc(self):
        print("метод абц")


x = C()
x.foo()
x.bar()
x.abc()
x.hello() # == A.hello(x)
B.hello(x)
