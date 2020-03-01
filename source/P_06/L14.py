def singleton(cls):
    """ Декторатор, що реалізує шабон проектування Одинак """

    instances = {}  # Словник класів

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    ...


#  Спробуємо створити кілька екземлярів класу MyClass
obj1 = MyClass()
obj2 = MyClass()


#  Переконаємося, obj1 та obj2 це один і той же екземпляр класу
print(obj1 is obj2)
print(int is 10)