class ProtectedDictIntError(KeyError):

    # Сталі для зазначення коду помилки
    NON_INTEGER_KEY = 0
    MISSED_KEY = 1
    CHANGE_VALUE = 2

    def __init__(self, err_code, message):
        """ Конструктор
        :param err_code: код помилки
        :param message: повідомлення
        """
        super().__init__()
        self.err_code = err_code
        self.message = message

    def __str__(self) -> str:
        return "ProtectedDictIntError: " + str(self.message)


class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}  # Словник

    def __setitem__(self, key, value):
        """ Метод, що перевантажує оператор [] для запису
        :param key: Ключ
        :param value: Значення
        """
        if not isinstance(key, int):  # якщо ключ не ціле число
            raise ProtectedDictIntError(ProtectedDictIntError.NON_INTEGER_KEY, "NON_INTEGER_KEY")

        if key in self.__dict:  # Якщо ключ міститься у словнику, забороняємо зміну значення
            raise ProtectedDictIntError(ProtectedDictIntError.CHANGE_VALUE, "CHANGE_VALUE")

        self.__dict[key] = value

    def __getitem__(self, key):
        """ Метод, що перевантажує оператор [] для читання
        :param key: Ключ
        :return: значення, що відподає ключу
        """
        if key not in self.__dict:  # якщо ключ не містиься у словнику
            raise ProtectedDictIntError(ProtectedDictIntError.MISSED_KEY, "MISSED_KEY")

        return self.__dict[key]

    def __str__(self):
        return str(self.__dict)


if __name__ == "__main__":
    d = ProtectedDictInt()
    d[10] = 10
    d[11] = 11
    d[12] = 12

    try:
        d[10] = 1
    except ProtectedDictIntError as e:
        print(e)

    try:
        d[12.44] = 12.44
    except ProtectedDictIntError as e:
        print(e)

    try:
        print(d[122])
    except ProtectedDictIntError as e:
        print(e)
