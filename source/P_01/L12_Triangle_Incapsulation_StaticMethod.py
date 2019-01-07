class Triangle:
    def __init__(self, a, b=0, c=0):
        """ Конструктор трикутника з можливістю копіювання
        :param a: перша сторона трикутника або екземпляр класу
        :param b: друга сторона трикутника
        :param c: третя сторона трикутника
        """
        if isinstance(a, Triangle):  # гілка копіювання
            self._a = a._a  # приватне поле _a –
            # копія поля _а трикутника a
            self._b = a._b  # приватне поле _b -
            # копія поля _b трикутника a
            self._c = a._c  # приватне поле _c -
            # копія поля _c трикутника a
        else:
            # перевіримо чи можна створити такий трикутник
            assert self.isExist(a, b, c)
            self._a = a  # приватне поле _a
            self._b = b  # приватне поле _b
            self._c = c  # приватне поле _c

    ...

    @staticmethod
    def isExist(a, b, c):
        """ Перевіряє, чи можна створити
        тикутник з заданими сторонами
        :param a: перша сторона трикутника
        :param b: друга сторона трикутника
        :param c: третя сторона трикутника
        :return: True, якщо трикутник з сторонами a, b, c існує
        """
        return a + b > c and a + c > b and c + b > a

    ...

    def set_a(self, a):
        """ Встановити сторону a трикутника
        :param a: сторона трикутника
        """
        # перевіримо чи існуватиме такий трикутник
        assert self.isExist(a, self._b, self._c)
        self._a = a

    def set_b(self, b):
        """ Встановити сторону b трикутника
        :param b: сторона трикутника
        """
        # перевіримо чи існуватиме такий трикутник
        assert self.isExist(self._a, b, self._c)
        self._b = b

    def set_c(self, c):
        """ Встановити сторону c трикутника
        :param c: сторона трикутника
        """
        # перевіримо чи існуватиме такий трикутник
        assert self.isExist(self._a, self._b, c)
        self._c = c

    def get_a(self):
        """ Повертає сторону a трикутника
        :return: Значення сторони a
        """
        return self._a

    def get_b(self):
        """ Повертає сторону b трикутника
        :return: Значення сторони b
        """
        return self._b

    def get_c(self):
        """ Повертає сторону c трикутника
        :return: Значення сторони c
        """
        return self._c

    def perimeter(self):
        """ Обчислює периметр трикутника
        :return: периметр трикутника
        """
        # периметр це сума сторін трикутника
        return self._a + self._b + self._c

    def square(self):
        """ Обчислює площу трикутника за формулою Герона
        :return: площу трикутника
        """
        p = self.perimeter() / 2.0  # обчислимо півпериметр
        res = p * (p - self._a) * (p - self._b) * (p - self._c)
        return res ** 0.5


if __name__ == "__main__":
    # Перевірка чи існує трикутник зі сторонами 4, 5, 6
    Triangle.isExist(4, 5, 6)  # через ім'я класу

    t = Triangle(3, 4, 5)
    # Перевірка чи існує трикутник зі сторонами 4, 5, 6
    t.isExist(4, 5, 6)  # через екземпляр класу
