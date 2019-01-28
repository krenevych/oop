class Vector2D:
    def __init__(self, x, y):
        self.x = x  # Координата x вектора
        self.y = y  # Координата y вектора

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __add__(self, other):
        """ Оператор +
        :param other: Правий операнд
        :return: Результат операції  self + other
        """
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Оператор -
        :param other:  Правий операнд
        :return: Результат операції self - other
        """
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """ Оператор *
        :param other: Правий операнд
        :return: Скалярний добуток векторів self і other
        """
        return self.x * other.x + self.y * other.y

    def __iadd__(self, other):
        """ Оператор +=
        :param other: Правий операнд
        :return: self
        """
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        """ Оператор -=
        :param other: Правий операнд
        :return: self
        """
        self.x -= other.x
        self.y -= other.y
        return self
class aaa:

    def __eq__(self, other):
        """ Оператор ==
        :param other: Правий операнд
        :return: True, якщо self == other
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """ Оператор !=
        :param other: Правий операнд
        :return: True, якщо self != other
        """
        return not self.__eq__(other)



if __name__ == "__main__":
    v1 = Vector2D(1, 1)
    v2 = Vector2D(2, 3)

    print(v1 == v2)
    print(v1 != v2)



