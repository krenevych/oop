class A:
    pass


a = A()

setattr(a, "name", "World")  # додавання нового поля у екземпляр класу
print(a.name)                # використання щойно доданого поля


def prepeared_method(self):  # функція
    if hasattr(self, "name"):   # перевіряємо чи має клас атрибут name
        print("Hello, %s!" % self.name)
    else:
        print("Hello!")


setattr(A, "method", prepeared_method)
a.method()  # Виклик методу доданого через рефлексію
