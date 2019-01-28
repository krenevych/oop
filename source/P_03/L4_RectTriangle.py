class RectTriangle:
    """ Клас прямокутний трикутник """

    def __init__(self, a, b):
        self._a = a  # поле _a - перший катет
        self._b = b  # поле _b - другий катет

    def __str__(self):
        return ("Прямокутний трикутник з катетами %f та %f"
                % (self._a, self._b))


t = RectTriangle(3, 4)

print(t)  # Тут замість t викликається метод t.__str__()
