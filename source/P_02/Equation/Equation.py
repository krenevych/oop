
class Equation:
    """ Клас лінійне рівняння виду bx + c = 0 """
    def __init__(self, b, c):
        """ Конструктор
        :param b: коефіцієнт рівння при x
        :param c: вільний член рівння
        """
        self.b = b
        self.c = c

    def solve(self):
        """ Повертає розв'язки рівння у вигляді кортежу
        [] - порожній список, якщо рівнняння немає жодного розв'зку b == 0, c != 0,
        ['inf'] - список, що містить один рядковий літерал 'inf',
        якщо рівнняння має безліч розв'язків b == 0, c == 0,
        [x1] - список з одного елементу, що є єдиним розв'язком рівняння
        :return: список розв'язків рівння
        """

        if self.b == 0 and self.c != 0:
            return []
        elif self.b == 0 and self.c == 0:
            return ['inf']
        else:
            return [-self.c / self.b]


if __name__ == "__main__":
    eq = Equation(1, 4)
    print(eq.solve())
    eq = Equation(0, 0)
    print(eq.solve())
    eq = Equation(0, 1)
    print(eq.solve())