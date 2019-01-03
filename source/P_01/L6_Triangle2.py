class Triangle:
    def __init__(self, a, b=0, c=0):
        """ Конструктор трикутника з можливістю копіювання
        :param a: перша сторона трикутника або екземпляр класу Triangle
        :param b: друга сторона трикутника
        :param c: третя сторона трикутника
        """

        if isinstance(a, Triangle):  # a є екземпляром Triangle
            self.a = a.a  # поле a – копія поля а трикутника a
            self.b = a.b  # поле b - копія поля b трикутника a
            self.c = a.c  # поле c - копія поля c трикутника a
        else:
            # перевіримо чи можна створити такий трикутник
            assert a + b > c and a + c > b and c + b > a
            self.a = a  # поле a - перша сторона трикутника
            self.b = b  # поле b - друга сторона трикутника
            self.c = c  # поле c - третя сторона трикутника

    def perimeter(self):
        """ Обчислює периметр трикутника
        :return: периметр трикутника
        """
        # периметр це сума сторін трикутника
        return self.a + self.b + self.c

    def square(self):
        """ Обчислює площу трикутника за формулою Герона
        :return: площу трикутника
        """
        p = self.perimeter() / 2.0  # обчислимо півпериметр
        res = p * (p - self.a) * (p - self.b) * (p - self.c)
        return res ** 0.5

if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    print("Площа заданого трикутника = %f" % t.square())

    t1 = Triangle(t)
    t1.a = 5
    print("Площа заданого трикутника = %f" % t1.square())