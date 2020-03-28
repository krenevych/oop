class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}  # Словник

    def __setitem__(self, key, value):
        """ Метод, що перевантажує оператор [] для запису
        :param key: Ключ
        :param value: Значення
        """
        if not isinstance(key, int):  # якщо ключ не ціле число
            raise KeyError

        if key in self.__dict:  # Якщо ключ міститься у словнику, забороняємо зміну значення
            raise PermissionError

        self.__dict[key] = value

    def __getitem__(self, key):
        """ Метод, що перевантажує оператор [] для читання
        :param key: Ключ
        :return: значення, що відподає ключу
        """
        if key not in self.__dict:  # якщо ключ не містиься у словнику
            raise KeyError

        return self.__dict[key]

    def __add__(self, other):
        """ Оператор +
        :param other: словник ProtectedDictInt або кортеж з двох елементів
        :return: новий екземпляр класу ProtectedDictInt
        """
        result_dict = ProtectedDictInt()  # Результат

        # Копіюємо всі ключі та значення з поточного словника
        for key, val in self.__dict.items():
            result_dict[key] = val

        if isinstance(other, ProtectedDictInt):
            # Копіюємо всі ключі та значення зі словника other
            for key, val in other.__dict.items():
                result_dict[key] = val
        # Якщо правий операнд кортеж з двох елементів
        elif isinstance(other, tuple) and len(other) == 2:
            result_dict[other[0]] = other[1]
        else:
            raise ValueError

        return result_dict

    def __sub__(self, other):
        """ Оператор -
        :param other: Правий операнд - ключ, що треба видалити зі словника
        :return: новий екземпляр класу ProtectedDictInt
        """

        # Якщо правий операнд - ціле число, що є ключем у поточному словнику
        if isinstance(other, int) and other in self:
            result_dict = ProtectedDictInt()
            for key, val in self.__dict.items():
                if key != other:
                    result_dict[key] = val
            return result_dict
        else:
            raise ValueError

    def __contains__(self, key):
        """ Оператор in
        :param key: ключ, що перевіряється чи міститься від у словнику
        :return: True, якщо ключ key міститься у словнику
        """
        return key in self.__dict

    def __len__(self):
        """ Попертає кількість пар ключ-значення у словнику """
        return len(self.__dict)

    def __str__(self):
        """ Перетворює словник у рядок
        (наприклад, для використання у функції print) """
        return str(self.__dict)


if __name__ == "__main__":
    d = ProtectedDictInt()
    d[10] = 10
    d[11] = 11
    d[12] = 12

    try:
        d[10] = 1
    except PermissionError as e:
        print(e)

    try:
        d[12.44] = 12.44
    except KeyError as e:
        print(e)

    try:
        print(d[122])
    except KeyError as e:
        print(e)

    print(d)

    d2 = d + (1, 2)
    print(d2)

    d3 = ProtectedDictInt()
    d3[110] = 110
    d3[111] = 111
    d3[112] = 112

    d4 = d2 + d3
    print(d4)

    d5 = d4 - 10
    print(d5)

    print(len(d5))