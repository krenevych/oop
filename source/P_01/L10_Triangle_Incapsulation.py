class Triangle:
    def __init__(self, a, b=0, c=0):
        """ Конструктор трикутника з можливістю копіювання
        :param a: перша сторона трикутника або екземпляр класу Triangle
        :param b: друга сторона трикутника
        :param c: третя сторона трикутника
        """

        if isinstance(a, Triangle):  # a є екземпляром Triangle
            self._a = a._a  # поле a – копія поля а трикутника a
            self._b = a._b  # поле b - копія поля b трикутника a
            self._c = a._c  # поле c - копія поля c трикутника a
        else:
            # перевіримо чи можна створити такий трикутник
            assert a + b > c and a + c > b and c + b > a
            self._a = a  # поле a - перша сторона трикутника
            self._b = b  # поле b - друга сторона трикутника
            self._c = c  # поле c - третя сторона трикутника

    def set_a(self, a):
        """ Встановити сторону a трикутника
        :param a: сторона трикутника
        """
        assert self._b + self._c > a
        self._a = a

    def set_b(self, b):
        """ Встановити сторону b трикутника
        :param b: сторона трикутника
        """
        assert self._a + self._c > b
        self._b = b

    def set_c(self, c):
        """ Встановити сторону c трикутника
        :param c: сторона трикутника
        """
        assert self._a + self._b > c
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
    t = Triangle(3, 4, 5)
    print("Площа заданого трикутника = %f" % t.square())

    t.set_c(2)
    print("Площа трикутника зі сторонами %f, %f, %f є %f"
          % (t.get_a(), t.get_b(), t.get_c(), t.square()))
