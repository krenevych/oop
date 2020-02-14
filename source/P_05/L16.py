from source.P_05.L14 import Cat, Dog, Parrot
from source.P_05.L15 import Logged


# Фактично додаємо до класів Cat, Dog, Parrot
# функціонал класу Loged
class LoggedCat(Logged, Cat):
    pass


class LoggedDog(Logged, Dog):
    pass


class LoggedParrot(Logged, Parrot):
    pass


c = LoggedCat("Кузя", 4, 2)
d = LoggedDog("Барбос", 4, 1)
p = LoggedParrot("Попка", 2, 0)

c.log()  # Викликаємо метод класу Loged
d.log()  # Викликаємо метод класу Loged
p.log()  # Викликаємо метод класу Loged
