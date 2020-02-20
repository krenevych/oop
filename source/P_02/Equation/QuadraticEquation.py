from source.P_02.Equation.Equation import Equation


class QuadraticEquation(Equation):
    """ Клас квадратне рівняння виду ax**2 + bx + c = 0 """

    def __init__(self, a, b, c) -> None:
        """ Конструктор

        :param a: коефіцієнт рівняння при степені 2
        :param b: коефіцієнт рівняння при x
        :param c: вільний член рівняння
        """
        super().__init__(b, c)
        self.a = a

    def d(self):
        """ Повертає дискримінант квадратного рівняння

        :return: значення дискримінанту """
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):

        if self.a == 0:   # Випадок, квадратне рівняння вироджується у лінійне
            return super().solve()
        else:
            d = self.d()  # обчислення дискримінанту
            if d < 0:  # розв'язків немає
                return []
            elif d == 0:  # один розв'язок
                return [- self.b / (2.0 * self.a)]
            else:  # два розв'язки
                sqr_d = d ** 0.5  # корінь з дискримінанту
                x1 = (- self.b - sqr_d) / (2.0 * self.a)
                x2 = (- self.b + sqr_d) / (2.0 * self.a)
                return [x1, x2]


if __name__ == "__main__":

    equation_list = []  # список рівнянь
    equation_list.append(QuadraticEquation(0, 4, 1))   # один розв'язок [-0.25]
    equation_list.append(QuadraticEquation(0, 0, 0))   # розв'язками є вся числова вісь
    equation_list.append(QuadraticEquation(0, 0, 1))   # розв'язків немає
    equation_list.append(QuadraticEquation(1, -3, 2))  # два розв'язки [1.0, 2.0]
    equation_list.append(QuadraticEquation(1, -2, 1))  # один розв'язок  [1.0]
    equation_list.append(QuadraticEquation(1, 2, 4))   # розв'язків немає
    equation_list.append(QuadraticEquation(1, 2, -3))  # два розв'язки [-3.0, 1.0]

    for eq in equation_list:
        print(eq.solve())

