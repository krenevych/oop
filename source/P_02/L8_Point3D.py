from source.P_02.L7_Point2D import Point2D


class Point3D(Point2D):
    """ Клас 2-вимірна точка """

    def __init__(self, x, y, z):
        """ Конструктор
        :param x: х-координата точки
        :param y: у-координата точки
        :param z: z-координата точки
        """
        super().__init__(x, *y)  # Виклик конструктора
                                 # базового класу
        self._z = z  # Координата z

    def getZ(self):
        return self._z

    def abs2(self):
        """ Заміщений метод, що повертає квадрат
            довжини радіус-вектора 3-вимірної точки
        :return: квадрат довжини радіус-вектора
        """
        return super().abs2() + self._z ** 2
