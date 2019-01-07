class Point2D:
    """ Клас 2-вимірна точка """

    def __init__(self, x, y):
        """ Конструктор
        :param x: х-координата точки
        :param y: у-координата точки
        """
        self._x = x  # поле координата x
        self._y = y  # поле координата y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def abs2(self):
        """ Повертає квадрат довжини радіус-вектора точки
        :return: квадрат довжини радіус-вектора точки
        """
        return self._x ** 2.0 + self._y ** 2.0
