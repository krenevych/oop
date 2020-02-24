from source.P_02.L12_Figure import Figure
from turtle import *


class Quadrate(Figure):
    """ Клас Квадрат """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижнього кута квадрата,
        довжину його сторони і колір.
        :param x: координата x лівого нижнього кута квадрата
        :param y: координата y лівого нижнього кута квадрата
        :param a: довжина сторони квадрата
        :param color: колір квадрата
        """
        super().__init__(x, y, color)   # Обов’язковий виклик конструктора базового класу
        self._a = a  # _a - довжина сторони квадрата

    def _draw(self, color):
        """ Допоміжний метод, що зображує квадрат заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # встановлюємо позицію лівого нижнього кута квадрата
        setpos(self._x, self._y)
        setheading(0)
        down()
        forward(self._a)  # перша сторона квадрата,
        left(90)
        forward(self._a)  # друга сторона квадрата
        left(90)
        forward(self._a)  # третя сторона квадрата
        left(90)
        forward(self._a)  # четверта сторона квадрата
        up()


# Перевірка роботи класу
if __name__ == '__main__':
    home()
    delay(30)
    q = Quadrate(0, 0, 150, "red")
    q.show()
    q.move(0, 140)
    q.hide()
    mainloop()
