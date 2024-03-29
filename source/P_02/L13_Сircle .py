from source.P_02.L12_Figure import Figure
from turtle import *


class Circle (Figure):
    """ Клас Коло """

    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        super().__init__(x, y, color)    # Обов’язковий виклик конструктора базового класу
        self._r = r  # _r - радіус кола

    def _draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()


# Перевірка роботи класу
if __name__ == '__main__':
    home()
    delay(10)
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    mainloop()
