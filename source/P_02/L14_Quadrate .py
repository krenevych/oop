from source.P_02.L12_Figure import Figure
import turtle as t


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
        t.pencolor(color)
        t.up()
        # встановлюємо позицію лівого нижнього кута квадрата
        t.setpos(self._x, self._y)
        t.setheading(0)
        t.down()
        t.forward(self._a)  # перша сторона квадрата,
        t.left(90)
        t.forward(self._a)  # друга сторона квадрата
        t.left(90)
        t.forward(self._a)  # третя сторона квадрата
        t.left(90)
        t.forward(self._a)  # четверта сторона квадрата
        t.up()


# Перевірка роботи класу
if __name__ == '__main__':
    t.home()
    t.delay(30)
    q = Quadrate(0, 0, 150, "red")
    q.show()
    q.move(0, 140)
    q.hide()
    t.mainloop()
