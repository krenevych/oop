"""

Приклад 4.2. Опишемо клас ProtectedDictInt, що є словником, у якому ключами можуть бути лише цілі числа та заборонена операція зміни значення за ключем (крім випадку додавання нової пари ключ-значення). Оформимо цей клас як обгортку навколо вбудованого типу даних dict.
Для обробки заборонених ситуацій створимо клас виключення, що
•	є нащадком класу KeyError;
•	ініціюється, якщо здійснюється спроба використання ключа, що не є цілим числом;
•	ініціюється якщо відбувається спроба змінити у словнику значення за заданим ключем;
•	генерує різні повідомлення у кожній із заборонених ситуацій.
Спочатку опишемо клас виключення, який назвемо ProtectedDictIntError.


"""


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
            raise ProtectedDictIntError(
            ProtectedDictIntError.NON_INTEGER_KEY, "NON_INTEGER_KEY")

        if key in self.__dict:  # Якщо ключ міститься у словнику,
                                # забороняємо зміну значення
            raise ProtectedDictIntError(
                  ProtectedDictIntError.CHANGE_VALUE, "CHANGE_VALUE")
        self.__dict[key] = value
    def __getitem__(self, key):
        """ Метод, що перевантажує оператор [] для читання
        :param key: Ключ
        :return: значення, що відподає ключу
        """
        if key not in self.__dict:  # ключ не містиься у словнику
            raise ProtectedDictIntError(
                     ProtectedDictIntError.MISSED_KEY, "MISSED_KEY")
        return self.__dict[key]
    def __str__(self):
        return str(self.__dict)

