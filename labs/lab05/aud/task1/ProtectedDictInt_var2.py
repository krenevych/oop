class ProtectedDictInt(dict):
    """ Клас, що наслідується від стандартного класу dict """

    """ У цьому класі опишемо лише методи __setitem__, __add__ та __sub__
        Методи __len__, __contains__ та __str__ успадкуємо з базового класу """

    def __setitem__(self, key, value):
        """ Метод, що перевантажує оператор [] для запису
        :param key: Ключ
        :param value: Значення
        """
        if not isinstance(key, int):  # якщо ключ не ціле число
            raise KeyError

        if key in self:  # Якщо ключ міститься у словнику, забороняємо зміну значення
            raise PermissionError

        super().__setitem__(key, value) # Виклик методу __setitem__ з батькывського класу


    def __add__(self, other):
        """ Оператор +
        :param other: словник ProtectedDictInt або кортеж з двох елементів
        :return: новий екземпляр класу ProtectedDictInt
        """
        result_dict = ProtectedDictInt()  # Результат

        # Копіюємо всі ключі та значення з поточного словника
        for key, val in self.items():
            result_dict[key] = val

        if isinstance(other, ProtectedDictInt):
            # Копіюємо всі ключі та значення зі словника other
            for key, val in other.items():
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
            for key, val in self.items():
                if key != other:
                    result_dict[key] = val
            return result_dict
        else:
            raise ValueError


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