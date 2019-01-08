import turtle as t

class Circle:
    """ Клас Коло """

    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        self._x = x  # _x - координата x центру кола
        self._y = y  # _y - координата y центру кола
        self._r = r  # _r - радіус кола
        self._visible = False  # _visible - чи є коло видимим на екрані
        self._color = color    # _color - колір кола

    def _draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        t.pencolor(color)
        t.up()
        # малює починаючи знизу кола
        t.setpos(self._x, self._y - self._r)
        t.down()
        t.circle(self._r)
        t.up()

    def show(self):
        """ Зображує коло на екрані """
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        """ Ховає коло (робить його невидимим на екрані) """
        if self._visible:
            self._visible = False
            # щоб сховати коло, потрібно його
            # зобразити кольором фону.
            self._draw(t.bgcolor())

    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        vis = self._visible
        if vis:
            self.hide()
        self._x += dx
        self._y += dy
        if vis:
            self.show()


# Перевірка роботи класу
if __name__ == '__main__':
    t.home()
    t.delay(10)
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    t.mainloop()
