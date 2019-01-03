class A:
    def __private(self):  # Зовсім приватний метод
        print("Хей, я ЗОВСІМ приватний метод!")


a = A()
# a.__private()
a._A__private()   # Виклик методу __private через модифіковане ім'я


