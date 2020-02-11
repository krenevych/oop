class ProtectedDictIntError(KeyError):
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
        self.__dict = {}

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise ProtectedDictIntError(ProtectedDictIntError.NON_INTEGER_KEY, "NON_INTEGER_KEY")

        if key in self.__dict:
            raise ProtectedDictIntError(ProtectedDictIntError.CHANGE_VALUE, "CHANGE_VALUE")

        self.__dict[key] = value

    def __getitem__(self, key):

        if key not in self.__dict:
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
