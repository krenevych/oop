from copy import copy
from random import randint


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
        # if key not in self._dict:  # якщо ключ не містиься у словнику
        #     raise KeyError

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

    def __iter__(self):
        return ProtectedDictIntIterator(self.__dict)


class ProtectedDictIntIterator:
    """ Ітератор для класу ProtectedDictInt """

    def __init__(self, collection):
        """ Конструктор ітератора
        :param collection: посилання на колекцію
        """
        self._sorted_keys = copy(sorted(list(collection)))
        self._cursor = 0  # поточна позиція ітератора у колекції

    def __next__(self):
        try:
            key = self._sorted_keys[self._cursor]
            self._cursor += 1
            return key
        except IndexError:
            raise StopIteration


def construct():
    object_list = []

    d = ProtectedDictInt()

    for i in range(20):
        try:
            key = randint(0, 1000)
            d[key] = key
        except:
            pass

    object_list.append(d)
    object_list.append(10)
    object_list.append("1234")
    object_list.append([1, 3, 4])
    object_list.append(ProtectedDictIntIterator([1, 3]))
    object_list.append(5.3)
    object_list.append({5: 5, 23: 23, 12: 12})
    return object_list


def isIterable(obj):
    # TODO: Реалізуйте тут перевірку того, що об'єкт obj
    #       підтримує ітераційний протокол
    return False


if __name__ == "__main__":
    lst = construct()
    for obj in lst:
        if isIterable(obj):
            for it in obj:
                print(it)
