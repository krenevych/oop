
class Polynom:
    """ Клас для моделювання роботи з поліномами"""

    def __init__(self):
        """ Конструктор """
        self._coeffs = {} # словник коефіцієнтів

    def set(self, power, coef):
        """ Встановлює коефіцієнт при відповідному степені

        :param power: степінь
        :param coef:  коефіцієнт
        """
        self._coeffs[power] = coef

    def __call__(self, x):
        """ Магічний метод - обчислює значення полінома

        :param x: значення незалежної змінної
        :return: значення полінома у точці х
        """
        res = 0
        for i, a in self._coeffs.items():
            res += a * x ** i
        return res


p = Polynom()
# Задамо поліном p = x^2 + 2x + 1
p.set(0, 1)
p.set(1, 2)
p.set(2, 1)

x = float(input("x="))

# f = p(x)  # виклик метода __call__(self, x)
f = p.__call__(x)  # виклик спеціального метода як звичайного метода
print("p(%f)=%f" % (x, f))
