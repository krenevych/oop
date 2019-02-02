class FactorialGenerator:
    """ Клас генератор факторіалів натуральни чисел
        1, 1, 2, 6, 24, ...     """

    def __init__(self, n):
        """ Конструктор генератора
        :param n: Номер найбільшого елементу послідовності
        """
        self._n = n  # Номер найбільшого члена послідовності
        self._k = 0  # Номер поточного члена послідовності
        self._f = 1  # Поточний член послідовності

    def __iter__(self):
        """ Спеціальний метод, що повертає ітератор
        :return: посилання на себе """
        return self

    def __next__(self):
        if self._k == 0:
            self._k = 1
            return 1
        elif self._k <= self._n:
            self._f *= self._k
            self._k += 1
            return self._f
        else:
            raise StopIteration


for f in FactorialGenerator(5):
    print(f)

f = FactorialGenerator(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
