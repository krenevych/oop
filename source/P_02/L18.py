class A:

    def __init__(self, a):
        self.a = a

    def show(self):
        print("a =", self.a)


class B:
    def __init__(self, b):
        self.b = b

    def show(self):
        print("b =", self.b)


class C(A, B):

    def __init__(self, a, b, c):
        A.__init__(self, a)  # Виклик конструктора класу A
        B.__init__(self, b)  # Виклик конструктора класу B
        self.c = c

    def show(self):
        A.show(self)  # Виклик методу show класу A
        B.show(self)  # Виклик методу show класу B
        print("c =", self.c)


if __name__ == "__main__":
    d = C(1, 2, 3)
    d.show()
