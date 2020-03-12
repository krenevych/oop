


class Singleton:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    ...


#  Спробуємо створити кілька екземлярів класу MyClass
obj1 = Singleton()
obj2 = Singleton()


#  Переконаємося, obj1 та obj2 це один і той же екземпляр класу
print(obj1 is obj2)