class Vector2D:
    def __init__(self, x, y):
        self.x = x  # Координата x вектора
        self.y = y  # Координата y вектора

    def __abs__(self):
        """ Визначає довжину вектора
        :return: довжину вектора
        """
        return (self.x ** 2.0 + self.y ** 2.0) ** 0.5


if __name__ == "__main__":
    v = Vector2D(3, 4)
    print(abs(v))
