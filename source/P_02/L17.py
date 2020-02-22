class A:
    def method(self):
        print("Called method from class A")


class B(A):
    pass


class C():
    def method(self):
        print("Called method from class C")


class D(B, C):
    def method(self):
        super().method()
        # C.method(self)  # виклик методу method() з класу C


if __name__ == "__main__":
    d = D()
    d.method()
