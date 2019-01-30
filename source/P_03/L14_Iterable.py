class Iterable:
    """ Клас Ітерований об'єкт """

    def __init__(self):
        self.__container = []  # Список елементів колекції

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(self.__container)

    def append(self, value):
        self.__container.append(value)

    def __setitem__(self, key, value):
        assert isinstance(key, int)
        assert key >= 0

        if key < len(self):
            self.__container[key] = value
        else:
            self.__container.append(value)

    def __getitem__(self, item):
        assert isinstance(item, int)
        assert item >= 0
        return self.__container[item]

    def __iter__(self):
        """ Спеціальний метод, що повертає ітератор для колекції
        :return: вбудований ітератор списку
        """
        return iter(self.__container)  # вбудований ітератор списку


if __name__ == "__main__":

    c = Iterable()
    c.append(1)
    c.append(2)
    c.append(3)
    c.append(4)

    # Неявне створення ітератора для колекції та виклику функції next()
    for i in c:
        print(i)


