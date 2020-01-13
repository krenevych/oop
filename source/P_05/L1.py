from abc import ABCMeta, abstractmethod


class Pet(metaclass = ABCMeta):
    def __init__(self, name):
        """ Конструктор
        :param name: Кличка тварини
        """
        self._name = name  # приватне поле - кличка тварини

    @abstractmethod
    def voice(self): # абстрактний метод
        pass         # порожня реалізація


    def getName(self):
        """ Повертає кличку тварини
        :return: кличку тварини
        """
        return self._name


# pet = Pet("Pet")

class Cat(Pet):
    pass


c = Cat("Кузя")
